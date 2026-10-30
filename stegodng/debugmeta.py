"""Optional per-file debug metadata sidecar (JSON).

``--debug-metadata-output`` writes one document per encoded DNG next to
the image (same base name, ``.json`` suffix).  The document lists every
metadata value the encode used or created: resolved options and seeds,
the camera profile's static block, the randomized EXIF fields, cover and
thumbnail generation details, and a re-read inventory of the tags that
actually landed in the container.

Binary blobs (XMP packet, preview JPEG, MakerNote, opcode lists, profile
tables) are never copied into the sidecar.  Each is described by its byte
count and a CRC32, which is enough to tell two encodes apart without
making the sidecar a second copy of the file.

JSON rather than YAML is deliberate: it is stdlib-only (no PyYAML
dependency), has unambiguous types (YAML 1.1 reads ``2019:01:01
12:00:00`` as a sexagesimal integer), and is written with sorted keys so
plain ``diff``/``jq`` comparisons are meaningful.
"""
from __future__ import annotations

import dataclasses
import datetime as _dt
import json
import math
import os
import platform
import struct
import zlib
from typing import Any

import numpy as np
import tifffile

from .framing import PayloadFrame

DEBUG_SCHEMA = "stegodng-debug-metadata"
DEBUG_SCHEMA_VERSION = 1

# Values longer than this are described by size + CRC32 instead of being
# decoded into the document (keeps TileOffsets arrays, XMP, opcode lists
# and Adobe tables out of the JSON).
_VALUE_BYTES_LIMIT = 256

# TIFF datatype -> name, and the integer types' struct format.
_TYPE_NAMES = {
    1: "BYTE", 2: "ASCII", 3: "SHORT", 4: "LONG", 5: "RATIONAL",
    6: "SBYTE", 7: "UNDEFINED", 8: "SSHORT", 9: "SLONG", 10: "SRATIONAL",
    11: "FLOAT", 12: "DOUBLE", 13: "IFD", 16: "LONG8", 17: "SLONG8",
    18: "IFD8",
}
_INT_FORMATS = {1: "B", 3: "H", 4: "I", 6: "b", 8: "h", 9: "i",
                13: "I", 16: "Q", 17: "q", 18: "Q"}


def debug_metadata_path(output_path: str) -> str:
    """Sidecar path: ``out.dng`` -> ``out.json`` (extension replaced)."""
    stem, _suffix = os.path.splitext(output_path)
    return f"{stem}.json"


def crc32_hex(data: bytes | bytearray | memoryview, value: int = 0) -> str:
    """CRC32 of ``data`` as 8 lowercase hex digits (non-cryptographic)."""
    return f"{zlib.crc32(data, value) & 0xFFFFFFFF:08x}"


def crc32_array(arr: np.ndarray, chunk_rows: int = 128) -> str:
    """CRC32 over an array in row chunks (no full-frame byte copy)."""
    array = np.asarray(arr)
    if array.ndim == 0:
        return crc32_hex(np.ascontiguousarray(array).tobytes())
    crc = 0
    for start in range(0, array.shape[0], max(1, chunk_rows)):
        block = np.ascontiguousarray(array[start:start + chunk_rows])
        crc = zlib.crc32(block.tobytes(), crc)
    return f"{crc & 0xFFFFFFFF:08x}"


def _describe_bytes(data: bytes | bytearray | memoryview) -> dict[str, Any]:
    """Byte blob as size + CRC32, plus hex for short values."""
    blob = data if isinstance(data, bytes) else bytes(data)
    out: dict[str, Any] = {
        "bytes": len(blob),
        "crc32": crc32_hex(blob),
    }
    if len(blob) <= 32:
        out["hex"] = blob.hex()
    return out


def json_safe(value: Any) -> Any:
    """Recursively convert profile/meta values into JSON-serializable ones."""
    if isinstance(value, np.generic):
        # np.float32/float64/int64/... -> their Python scalar equivalents
        # so the finiteness check below (and json) sees a real float/int.
        value = value.item()
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else repr(value)
    if isinstance(value, (bytes, bytearray, memoryview)):
        return _describe_bytes(value)
    if isinstance(value, np.ndarray):
        if value.size <= 4096:
            return value.tolist()
        return {
            "shape": list(value.shape),
            "dtype": str(value.dtype),
            "bytes": value.nbytes,
            "crc32": crc32_array(value),
        }
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [json_safe(item) for item in value]
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return {
            field.name: json_safe(getattr(value, field.name))
            for field in dataclasses.fields(value)
        }
    return repr(value)


def profile_snapshot(profile) -> dict[str, Any]:
    """All static profile constants as a JSON-safe dict.

    Includes the per-camera pools (lenses/ISO/exposure, ...) because they
    decide which randomized values an encode can produce; byte blobs
    (opcode lists, Adobe HueSat/LookTable tables) are hashed.
    """
    if dataclasses.is_dataclass(profile):
        return json_safe(dataclasses.asdict(profile))
    return json_safe(profile)


def metadata_snapshot(meta: dict) -> dict[str, Any]:
    """The randomized metadata dict as written into the EXIF block."""
    return json_safe(meta)


def _tag_name(code: int, namespace: str) -> str:
    """Human tag name from tifffile's registries, else ``tag_<code>``."""
    registry = {
        "exif": tifffile.TIFF.EXIF_TAGS,
        "gps": tifffile.TIFF.GPS_TAGS,
    }.get(namespace)
    if registry is not None:
        name = registry.get(code, None)
        if isinstance(name, str):
            return name
    name = tifffile.TIFF.TAGS.get(code, None)
    return name if isinstance(name, str) else f"tag_{code}"


def _decode_ints(typ: int, count: int, raw: bytes) -> list[int] | None:
    """All integer values of a numeric entry (no size limit)."""
    fmt = _INT_FORMATS.get(typ)
    if fmt is None:
        return None
    size = struct.calcsize(fmt)
    n = min(count, len(raw) // size)
    if n <= 0:
        return []
    return list(struct.unpack_from("<" + fmt * n, raw))


def _pointer(entries: list[tuple[int, int, int, bytes]],
             tag: int) -> int | None:
    """IFD offset from an inline pointer entry (classic or BigTIFF)."""
    for entry_tag, typ, _count, raw in entries:
        if entry_tag == tag and typ in (4, 13):
            fmt = "<Q" if len(raw) == 8 else "<I"
            return struct.unpack_from(fmt, raw)[0]
    return None


def _decode_value(typ: int, count: int, raw: bytes, tag: int) -> Any:
    """Decode one IFD value for the debug document."""
    if len(raw) > _VALUE_BYTES_LIMIT:
        return _describe_bytes(raw)
    # BigTIFF writes the Exif/GPS IFD pointers as LONG but stores the
    # 8-byte offset in the value field; read the whole field there.
    if tag in (34665, 34853) and typ in (4, 13) and len(raw) == 8:
        return struct.unpack_from("<Q", raw)[0]
    # The DNG raw digests read better as hex than as sixteen byte values.
    if tag in (51111, 50781) and typ in (1, 7) and len(raw) == 16:
        return raw.hex()
    if typ == 2:
        return raw.split(b"\x00", 1)[0].decode("ascii", "replace")
    ints = _decode_ints(typ, count, raw)
    if ints is not None:
        return ints[0] if len(ints) == 1 else ints
    if typ in (5, 10):
        fmt = "I" if typ == 5 else "i"
        n = len(raw) // 4
        nums = struct.unpack("<" + fmt * n, raw)
        pairs = [[nums[i], nums[i + 1]] for i in range(0, n, 2)]
        return pairs[0] if len(pairs) == 1 else pairs
    if typ in (11, 12):
        fmt = "f" if typ == 11 else "d"
        size = struct.calcsize(fmt)
        n = len(raw) // size
        nums = list(struct.unpack("<" + fmt * n, raw))
        return nums[0] if len(nums) == 1 else nums
    if typ == 7:
        return raw.hex() if len(raw) <= 32 else _describe_bytes(raw)
    return _describe_bytes(raw)


def _tag_snapshot(entries: list[tuple[int, int, int, bytes]],
                  namespace: str = "tiff") -> list[dict[str, Any]]:
    """One IFD as a list of {tag, name, type, count, value} records."""
    out = []
    for tag, typ, count, raw in entries:
        out.append({
            "tag": tag,
            "name": _tag_name(tag, namespace),
            "type": _TYPE_NAMES.get(typ, f"type_{typ}"),
            "count": count,
            "value": _decode_value(typ, count, raw, tag),
        })
    out.sort(key=lambda item: item["tag"])
    return out


def _preview_blob(path: str, entries: list[tuple[int, int, int, bytes]]
                  ) -> dict[str, Any] | None:
    """Read the IFD0 JPEG strips/tiles and hash their exact bytes."""
    offsets = counts = None
    for tag in (273, 324):
        for entry_tag, typ, count, raw in entries:
            if entry_tag == tag:
                offsets = _decode_ints(typ, count, raw)
                break
        if offsets:
            break
    for tag in (279, 325):
        for entry_tag, typ, count, raw in entries:
            if entry_tag == tag:
                counts = _decode_ints(typ, count, raw)
                break
        if counts:
            break
    if not offsets or not counts or len(offsets) != len(counts):
        return None
    total = 0
    crc = 0
    with open(path, "rb") as handle:
        for offset, length in zip(offsets, counts):
            if length <= 0:
                continue
            handle.seek(offset)
            chunk = handle.read(length)
            if len(chunk) != length:
                return None
            total += length
            crc = zlib.crc32(chunk, crc)
    return {"bytes": total, "crc32": f"{crc & 0xFFFFFFFF:08x}",
            "strips": len(offsets)}


def collect_written_file(path: str) -> dict[str, Any]:
    """Re-read the finished file and describe every tag on disk."""
    from .container import DngContainer, read_ifd

    entries = read_ifd(path)
    document: dict[str, Any] = {
        "ifd0": _tag_snapshot(entries, "tiff"),
    }
    try:
        document["subifds"] = [
            _tag_snapshot(read_ifd(path, offset), "tiff")
            for offset in DngContainer(path).subifd_offsets()
        ]
    except ValueError:
        document["subifds"] = []
    exif_offset = _pointer(entries, 34665)
    if exif_offset is not None:
        document["exif"] = _tag_snapshot(read_ifd(path, exif_offset), "exif")
    gps_offset = _pointer(entries, 34853)
    if gps_offset is not None:
        document["gps"] = _tag_snapshot(read_ifd(path, gps_offset), "gps")
    preview = _preview_blob(path, entries)
    if preview is not None:
        document["preview_jpeg"] = preview
    return document


def _tool_info() -> dict[str, Any]:
    import PIL

    from . import __version__

    return {
        "name": "stegodng",
        "version": __version__,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "pillow": PIL.__version__,
        "tifffile": tifffile.__version__,
    }


def _now_utc() -> str:
    return (_dt.datetime.now(_dt.timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z"))


def build_debug_document(
    *,
    info: dict,
    profile,
    options: dict,
    meta: dict,
    thumbnail_requested: str,
    thumbnail_label: str,
    thumbnail_rgb,
    stegos: list,
    cover_seed: int | None,
    metadata_seed: int | None,
    white_level: int | None,
    headroom: int,
    frame_crc32: str,
    total_payload_bytes: int | None = None,
    split: dict | None = None,
    context: dict | None = None,
) -> dict[str, Any]:
    """Build the per-file debug document (see module docstring)."""
    payload_bytes = int(info["payload_len"])
    capacity = int(info["capacity"])
    frame_records = []
    for index, stego in enumerate(stegos):
        frame_records.append({
            "index": index,
            "seed": None if cover_seed is None else cover_seed + index,
            "shape": list(stego.shape),
            "dtype": str(stego.dtype),
            "crc32": crc32_array(stego),
        })
    thumb = np.asarray(thumbnail_rgb)
    summary = {
        "output": info["path"],
        "output_bytes": int(info["size"]),
        "width": int(options["width"]),
        "height": int(options["height"]),
        "mode": options["mode"],
        "bit_depth": options["bit_depth"],
        "lsb_planes": options["lsb_planes"],
        "frames": options["frames"],
        "compression": options["compression"],
        "bigtiff": bool(info["bigtiff"]),
        "thumbnail_source": thumbnail_label,
        "payload_bytes": payload_bytes,
    }
    if split is not None:
        summary["chunk_seq"] = split["chunk_seq"]
        summary["chunk_total"] = split["chunk_total"]
    document: dict[str, Any] = {
        "schema": DEBUG_SCHEMA,
        "schema_version": DEBUG_SCHEMA_VERSION,
        "generated_at": _now_utc(),
        "tool": _tool_info(),
        "summary": summary,
        "encode": {
            "options": json_safe(options),
            "payload": {
                # Plaintext length; the CRC covers the framed bytes that
                # actually go into the LSB planes (XOR-masked when keyed),
                # so a keyed encode never leaks a plaintext fingerprint.
                "bytes": payload_bytes,
                "total_bytes": (payload_bytes if total_payload_bytes is None
                                else total_payload_bytes),
                "frame_bytes": payload_bytes + PayloadFrame.HEADER_LEN,
                "frame_crc32": frame_crc32,
            },
            "output": {
                "path": info["path"],
                "bytes": int(info["size"]),
                "bigtiff": bool(info["bigtiff"]),
                "container": info["container"],
            },
            "capacity": {
                "bytes": capacity,
                "samples_per_frame": int(stegos[0].size),
                "frames": len(stegos),
                "fill_ratio": round(payload_bytes / capacity, 6)
                if capacity else None,
            },
            "split": split,
        },
        "profile": profile_snapshot(profile),
        "cover": {
            "generator": "synthetic gradient + noise",
            "seed": cover_seed,
            "metadata_seed": metadata_seed,
            "white_level": white_level,
            "white_level_mode": ("full-container" if white_level is None
                                 else "profile-effective"),
            "headroom": headroom,
            # The frame CRC is over the raw array after LSB embedding, i.e.
            # the data written (not the pre-embedding cover).
            "frame_crc32_scope": "embedded-raw",
            "frames": frame_records,
        },
        "thumbnail": {
            "requested": thumbnail_requested,
            "source": thumbnail_label,
            "shape": list(thumb.shape),
            "dtype": str(thumb.dtype),
            "crc32": crc32_array(thumb),
        },
        "metadata": metadata_snapshot(meta),
        "file": collect_written_file(info["path"]),
    }
    if context:
        document["invocation"] = json_safe(context)
    return document


def write_debug_metadata(output_path: str, document: dict) -> str:
    """Write ``document`` next to ``output_path``; return the sidecar path."""
    path = debug_metadata_path(output_path)
    # Serialize first: a serialization failure must not truncate an
    # existing (valid) sidecar before the error is known.
    try:
        text = json.dumps(document, indent=2, sort_keys=True,
                          ensure_ascii=True, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"cannot serialize debug metadata for {output_path}: {exc}"
        ) from exc
    try:
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.write("\n")
    except OSError as exc:
        _remove_partial(path)
        raise ValueError(
            f"cannot write debug metadata {path}: {exc}") from exc
    return path


def _remove_partial(path: str) -> None:
    try:
        os.unlink(path)
    except OSError:
        pass
