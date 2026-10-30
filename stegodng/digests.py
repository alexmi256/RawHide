"""Raw image digests written by Adobe-style DNG writers.

Two IFD0 tags let a tool identify a raw image without decoding it:

``NewRawImageDigest`` (tag 51111)
    The DNG SDK "fast" digest (``dng_negative::FindFastImageDigest``).
    The image is cut into 256 x 256 tiles in row-major order (edge tiles
    are truncated to the image bounds), every tile is MD5-hashed in
    planar pixel order and little-endian byte order, and the tag is the
    MD5 of the concatenated 16-byte tile digests.  This is *not* the MD5
    of the whole raster: the per-tile digesting is what makes the value
    reproducible for tile-compressed raws.

``RawDataUniqueID`` (tag 50781)
    ``dng_negative::FindRawDataUniqueID``: MD5 over the new raw digest,
    the unique camera model name (tag 50708, *not* Make/Model), the
    default crop size/origin and user crop rationals, and the fingerprint
    stream of each opcode list (``dng_opcode_list::FingerprintToStream``).
    It changes whenever the pixels, the model or the crop/opcode metadata
    changes, and it is stable for identical raw data.

Both values reproduce the tags in the Pixel XL reference DNGs; see
``tools/digests.py`` for a verifier that recomputes them from a file.
"""
from __future__ import annotations

import hashlib
import struct

import numpy as np

DIGEST_TILE = 256
NEW_RAW_IMAGE_DIGEST_TAG = 51111
RAW_DATA_UNIQUE_ID_TAG = 50781

# TIFF/EP opcode lists are stored big-endian regardless of the TIFF byte
# order; the fingerprint stream is an in-memory dng_stream (host order,
# little-endian on every platform we write for).
_LIST_COUNT = ">I"
_OPCODE_HEADER = ">IIII"
_GAIN_MAP_OPCODE = 9
_GAIN_MAP_HEADER = ">10I4dI"
_GAIN_MAP_HEADER_SIZE = struct.calcsize(_GAIN_MAP_HEADER)


def _tile_bytes(block: np.ndarray) -> bytes:
    """Tile bytes as the SDK hashes them: planar, little-endian."""
    if block.ndim == 3:
        block = np.transpose(block, (2, 0, 1))
    block = np.ascontiguousarray(block)
    return block.astype(block.dtype.newbyteorder("<"), copy=False).tobytes()


def new_raw_image_digest(raw, tile: int = DIGEST_TILE) -> bytes:
    """Return the 16-byte ``NewRawImageDigest`` for a raw image array.

    ``raw`` is ``(height, width)`` for a CFA image or
    ``(height, width, planes)`` for a linear raw.  Values are hashed in
    the array's own dtype (uint8 for 8-bit raws, uint16 otherwise), the
    same pixel type the DNG SDK picks from ``BitsPerSample``.
    """
    arr = np.asarray(raw)
    if arr.ndim not in (2, 3):
        raise ValueError("raw image must be 2-D or height x width x planes")
    if arr.size == 0:
        raise ValueError("raw image is empty")
    if tile < 1:
        raise ValueError("tile size must be positive")
    height, width = arr.shape[:2]
    digests = []
    for top in range(0, height, tile):
        for left in range(0, width, tile):
            block = arr[top:top + tile, left:left + tile]
            digests.append(hashlib.md5(_tile_bytes(block)).digest())
    return hashlib.md5(b"".join(digests)).digest()


def _gain_map_params_le(params: bytes) -> bytes:
    if len(params) < _GAIN_MAP_HEADER_SIZE:
        raise ValueError("GainMap parameters are truncated")
    header = list(struct.unpack_from(_GAIN_MAP_HEADER, params, 0))
    body = params[_GAIN_MAP_HEADER_SIZE:]
    if len(body) % 4:
        raise ValueError("GainMap map data is not a whole number of floats")
    tail = np.frombuffer(body, dtype=">f4").astype("<f4").tobytes()
    return struct.pack("<10I4dI", *header) + tail


def opcode_list_fingerprint(blob: bytes) -> bytes:
    """Return the SDK fingerprint stream for one opcode list.

    ``dng_opcode_list::FingerprintToStream`` re-serializes the list in
    host (little-endian) order: the opcode count, then per opcode the ID,
    minimum version, flags and the opcode's own parameter block.  An
    empty list contributes nothing at all.
    """
    if len(blob) < 4:
        raise ValueError("opcode list is shorter than its count field")
    count = struct.unpack_from(_LIST_COUNT, blob, 0)[0]
    if count > 64:
        raise ValueError(f"implausible opcode count {count}")
    if count == 0:
        return b""
    out = bytearray(struct.pack("<I", count))
    offset = 4
    for index in range(count):
        if offset + 16 > len(blob):
            raise ValueError(f"opcode {index}: truncated header")
        opcode, version, flags, size = struct.unpack_from(
            _OPCODE_HEADER, blob, offset)
        offset += 16
        if offset + size > len(blob):
            raise ValueError(f"opcode {index}: truncated parameters")
        params = blob[offset:offset + size]
        offset += size
        out += struct.pack("<III", opcode, version, flags)
        # dng_opcode_GainMap::PutData writes the parameter length, the
        # area spec and the gain map; the file stores the same payload
        # big-endian, so re-emit it little-endian.
        out += struct.pack("<I", size)
        if opcode == _GAIN_MAP_OPCODE:
            out += _gain_map_params_le(params)
        else:
            raise ValueError(
                f"opcode {index}: no fingerprint rule for opcode id "
                f"{opcode} (only GainMap {_GAIN_MAP_OPCODE} is handled)")
    if offset != len(blob):
        raise ValueError(
            f"{len(blob) - offset} trailing bytes after {count} opcodes")
    return bytes(out)


def raw_data_unique_id(digest: bytes, model: str,
                       crop_size: tuple[tuple[int, int], tuple[int, int]],
                       crop_origin: tuple[tuple[int, int], tuple[int, int]],
                       user_crop: tuple[tuple[int, int], ...] = (
                           (0, 1), (0, 1), (1, 1), (1, 1)),
                       opcode_lists: tuple[bytes | None, ...] = ()) -> bytes:
    """Return the 16-byte ``RawDataUniqueID`` for one raw image.

    ``digest`` is :func:`new_raw_image_digest`; ``model`` is the unique
    camera model string (DNG tag 50708, not the IFD0 Model).  The crop
    arguments are rational ``(numerator, denominator)`` pairs in DNG tag
    order (size H, size V, origin H, origin V, user crop T/L/B/R).
    ``opcode_lists`` is ``(OpcodeList1, OpcodeList2, OpcodeList3)``;
    ``None`` entries and empty lists add nothing, mirroring the SDK.
    """
    if not isinstance(digest, (bytes, bytearray)) or len(digest) != 16:
        raise ValueError("raw image digest must be 16 bytes")
    try:
        model_bytes = model.encode("ascii")
    except UnicodeEncodeError as exc:  # pragma: no cover - profiles are ASCII
        raise ValueError(f"model name must be ASCII: {exc}") from exc
    printer = hashlib.md5()
    printer.update(bytes(digest))
    printer.update(model_bytes)
    pairs = (*crop_size, *crop_origin, *user_crop)
    if len(user_crop) != 4:
        raise ValueError("user crop needs four rationals")
    for pair in pairs:
        numerator, denominator = pair
        printer.update(struct.pack("<II", int(numerator), int(denominator)))
    for blob in opcode_lists:
        if blob:
            printer.update(opcode_list_fingerprint(blob))
    return printer.digest()
