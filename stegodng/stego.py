"""High-level API: :class:`DngStego` (encode/decode/generate).

Thin module-level :func:`encode` / :func:`decode` / :func:`generate_tiff`
wrappers preserve the original single-file API.
"""
from __future__ import annotations

import itertools
import os
import random
import struct
import warnings
from typing import Any

import numpy as np
import tifffile
from PIL import Image

from .codec import LsbCodec, format_kb_hi, format_kb_lo
from .container import (
    DngContainer,
    XMP_LEN,
    append_ifd0_ascii,
    build_xmp,
    set_ifd0_tag,
)
from .cover import CoverGenerator
from .framing import PayloadFrame
from .metadata import MetadataRandomizer
from .thumbnails import ThumbnailProvider
from .split import (
    chunk_path,
    format_seq_value,
    iter_chunk_bounds,
    new_split_id,
    parse_chunk_name,
    resolve_split_fields,
)
from .progress import bar as _progress_bar
from .progress import enabled as _progress_enabled
from .profile import (
    DEFAULT_PROFILE,
    MAX_FRAMES,
    MAX_LSB_PLANES,
    SUPPORTED_BIT_DEPTHS,
)


class _DecodeLimitError(ValueError):
    """Declared payload rejected by the cap or image capacity.

    Subclass of ValueError (so existing ``except ValueError`` callers are
    unaffected); lets ``_decode_one`` recognize limit rejections by type
    instead of fragile message-substring matching.
    """


class DngStego:
    """Embed and recover payloads in DNG raw sensor data."""

    def __init__(self, profile=DEFAULT_PROFILE) -> None:
        self.profile = profile

    @staticmethod
    def _rgb_to_ycbcr(thumb_rgb) -> "np.ndarray":
        # tifffile stores YCbCr JPEG planes verbatim (no RGB conversion),
        # so convert up front; the tag stays YCbCr like the combiner files.
        return np.ascontiguousarray(
            np.asarray(Image.fromarray(thumb_rgb).convert("YCbCr")))

    def _levels(self, mode: str, bit_depth: int):
        peak = (1 << bit_depth) - 1
        # Scale the combiner reference BlackLevel (256 @ 16-bit).
        black_val = max(1, round(self.profile.black_level_ref * peak / 65535))
        n = 3 if mode == "linear" else 1
        return (black_val,) * n, (peak,) * n

    def _ifd0_extras(self, meta: dict, n_dummies: int = 0) -> list:
        extras = [
            (271, "s", 0, self.profile.make, True),
            (272, "s", 0, self.profile.model, True),
            (274, 3, 1, (1,), True),
            (700, "B", XMP_LEN, build_xmp(), True),
            (50706, "B", 4, self.profile.dng_version, True),
            (50707, "B", 4, self.profile.dng_backward, True),
            (50708, "s", 0, self.profile.unique_camera_model, True),
            (50721, 10, 9, self.profile.color_matrix1, True),
            (50722, 10, 9, self.profile.color_matrix2, True),
            (50727, 5, 3, [(10000, 10000)] * 3, True),
            (50728, 5, 3, meta["as_shot_neutral"], True),
            (50730, 10, 1, [meta["baseline_exposure"]], True),
            (50731, 5, 1, [self.profile.baseline_noise], True),
            (50732, 5, 1, [self.profile.baseline_sharpness], True),
            (50734, 5, 1, [self.profile.linear_response_limit], True),
            (50735, "s", 0, meta["camera_serial"], True),
            (50736, 5, 4, [
                (meta["lens_spec"][0], meta["lens_spec"][1]),
                (meta["lens_spec"][2], meta["lens_spec"][3]),
                (meta["lens_spec"][4], meta["lens_spec"][5]),
                (meta["lens_spec"][6], meta["lens_spec"][7]),
            ], True),
            (50739, 5, 1, [self.profile.shadow_scale], True),
            (50778, 3, 1, (self.profile.calib_illuminant1,), True),
            (50779, 3, 1, (self.profile.calib_illuminant2,), True),
            # Dummy private tag repurposed into ExifTag (34665) after
            # writing: tifffile filters IFD-pointer tags from extratags,
            # so the EXIF Sub-IFD offset is patched in post (same 12-byte
            # entry, no shifting required).
            (65000, 3, 1, (0,), True),
        ]
        # Reserved dummies repurposed post-write into split seq/id tags.
        for i in range(n_dummies):
            extras.append((65001 + i, 4, 1, (0,), True))
        return extras

    def _sub_extras(self, meta: dict, mode: str, width: int, height: int,
                    bit_depth: int) -> list:
        black, white_t = self._levels(mode, bit_depth)
        opcode = self.profile.opcode_list3
        if mode == "linear":
            return [
                (50714, 4, 3, black, True),
                (50717, 4, 3, white_t, True),
                (50718, 5, 2, [(1, 1), (1, 1)], True),
                (50719, 5, 2, [(0, 1), (0, 1)], True),
                (50720, 5, 2, [(width, 1), (height, 1)], True),
                (50738, 5, 1, [(100, 100)], True),
                (50780, 5, 1, [(100, 100)], True),
                (51022, 7, len(opcode), opcode, True),
            ]
        return [
            (50710, 3, 3, (0, 1, 2), True),  # CFAPlaneColor R,G,B
            (50711, 3, 1, (1,), True),        # CFALayout rectangular
            (50714, 4, 1, black, True),
            (50717, 4, 1, white_t, True),
            (50718, 5, 2, [(1, 1), (1, 1)], True),
            (50719, 5, 2, [(0, 1), (0, 1)], True),
            (50720, 5, 2, [(width, 1), (height, 1)], True),
            (50738, 5, 1, [(100, 100)], True),
            (50780, 5, 1, [(100, 100)], True),
            (33421, 3, 2, (2, 2), True),
            (33422, 3, 4, (0, 1, 1, 2), True),
            (51022, 7, len(opcode), opcode, True),
        ]

    def _write_container(self, output_path: str, *, stegos: list,
                         thumb_rgb, meta: dict, width: int, height: int,
                         mode: str, bit_depth: int, compression: str,
                         frames: int, tw: int, th: int,
                         ifd0_dummies: int = 0) -> bool:
        """Write thumbnail + raw frames, patch photometrics, attach EXIF.

        ``ifd0_dummies`` reserves that many private LONG tags (65001+)
        for post-write split seq/id fields. Returns the bigtiff flag.
        """
        thumb_ycbcr = self._rgb_to_ycbcr(thumb_rgb)
        bytes_per_sample = 1 if bit_depth <= 8 else 2
        bigtiff = (
            width * height * (3 if mode == "linear" else 1)
            * bytes_per_sample * frames
        ) > 3_500_000_000
        photo_main = "rgb" if mode == "linear" else "cfa"  # patched to LinearRaw later
        tile = (96, 128) if (width >= 128 and height >= 96) else None
        # Uncompressed by default: LibRaw/rawpy (tested 0.27) decodes
        # uncompressed DNG but fails on Adobe-Deflate DNG ("unexpected EOF").
        # Deflate stays available as an opt-in for smaller files; it is still
        # lossless so the LSB payload survives either way.
        use_deflate = compression == "adobe_deflate"

        with tifffile.TiffWriter(output_path, bigtiff=bigtiff) as tif:
            ifd0_extras = self._ifd0_extras(meta, n_dummies=ifd0_dummies)
            tif.write(
                thumb_ycbcr, photometric="ycbcr", compression="jpeg",
                software=self.profile.software, datetime=meta["datetime"],
                rowsperstrip=th,
                subfiletype=1, subifds=frames, metadata=None, extratags=ifd0_extras,
            )
            sub_extras = self._sub_extras(meta, mode, width, height,
                                                bit_depth)
            for stego in stegos:
                tif.write(
                    stego, photometric=photo_main,
                    compression="adobe_deflate" if use_deflate else None,
                    predictor=2 if use_deflate else None,
                    tile=tile, metadata=None, software=False,
                    bitspersample=bit_depth,
                    subfiletype=0, extratags=sub_extras,
                )

        if mode == "linear":
            DngContainer(output_path).patch_linear_raw()
        DngContainer(output_path).append_exif(meta, tw, th)
        return bigtiff

    def _file_info(self, output_path: str, *, width: int, height: int,
                   mode: str, bit_depth: int, container: str,
                   lsb_planes: int, frames: int, thumb_label: str,
                   bigtiff: bool, cap: int, payload_len: int,
                   meta: dict) -> dict:
        return {
            "path": output_path,
            "width": width,
            "height": height,
            "mode": mode,
            "bit_depth": bit_depth,
            "container": container,
            "lsb_planes": lsb_planes,
            "frames": frames,
            "thumbnail": thumb_label,
            "bigtiff": bigtiff,
            "capacity": cap,
            "payload_len": payload_len,
            "size": os.path.getsize(output_path),
            "metadata": meta,
        }


    def encode(
            self,
        payload: bytes,
        output_path: str,
        width: int = 2048,
        height: int = 1536,
        seed: int | None = None,
        key: bytes | None = None,
        lsb_planes: int = 1,
        bit_depth: int = 16,
        mode: str = "linear",
        compression: str = "none",
        no_randomize: bool = False,
        frames: int = 1,
        thumbnail: str = "random",
        progress: bool | None = None,
    ) -> dict:
        """Embed `payload` into a new DNG file. Returns info dict.

        ``frames`` full-resolution raw SubIFDs share the file (burst/stack
        style); the framed payload is striped across them in order, so
        capacity scales ~linearly with ``frames``. Each extra frame adds a
        full raster to the file size.
        """
        self._validate_options(bit_depth, lsb_planes, frames, mode,
                               compression)
        meta = MetadataRandomizer(0 if no_randomize else seed).randomize()
        if seed is None:
            seed = 0

        covers = [CoverGenerator(seed + i).cover(height, width, mode, bit_depth)
                  for i in range(frames)]
        n_samples = covers[0].size
        cap = LsbCodec.capacity_bytes_total(n_samples, lsb_planes, frames)
        if len(payload) > cap:
            raise ValueError(
                f"payload {format_kb_hi(len(payload))} exceeds capacity {format_kb_lo(cap)} "
                f"({width}x{height} {mode} {bit_depth}-bit, "
                f"{lsb_planes} LSB plane(s)"
                f"{f' x {frames} frames' if frames > 1 else ''})"
            )
        stegos = LsbCodec.stripe_frames(
            covers, PayloadFrame.pack(payload, key), lsb_planes,
            progress=progress)
        # stripe_frames embeds in place: stegos share the covers'
        # buffers, so drop the extra references promptly.
        del covers

        tw, th = min(4000, width), min(3000, height)
        thumb, thumb_label = ThumbnailProvider(seed=seed).get(
            tw, th, source=thumbnail)
        bigtiff = self._write_container(
            output_path, stegos=stegos, thumb_rgb=thumb, meta=meta,
            width=width, height=height, mode=mode, bit_depth=bit_depth,
            compression=compression, frames=frames, tw=tw, th=th,
        )
        return self._file_info(
            output_path, width=width, height=height, mode=mode,
            bit_depth=bit_depth, container=str(stegos[0].dtype),
            lsb_planes=lsb_planes, frames=frames, thumb_label=thumb_label,
            bigtiff=bigtiff, cap=cap, payload_len=len(payload), meta=meta,
        )

    def _validate_options(self, bit_depth: int, lsb_planes: int,
                          frames: int, mode: str, compression: str) -> None:
        if bit_depth not in SUPPORTED_BIT_DEPTHS:
            raise ValueError(f"bit_depth must be one of {SUPPORTED_BIT_DEPTHS}")
        if not (1 <= lsb_planes <= MAX_LSB_PLANES):
            raise ValueError(f"lsb_planes must be 1-{MAX_LSB_PLANES}")
        if lsb_planes > bit_depth:
            raise ValueError(
                f"lsb_planes ({lsb_planes}) exceeds bit_depth ({bit_depth}); "
                f"payload values would overflow the declared WhiteLevel. "
                f"Use --bit-depth 16 (full-range uint16, up to 16 planes) or "
                f"fewer planes.")
        if not (1 <= frames <= MAX_FRAMES):
            raise ValueError(f"frames must be 1-{MAX_FRAMES} (got {frames})")
        if mode not in ("linear", "cfa"):
            raise ValueError("mode must be 'linear' or 'cfa'")
        if compression not in ("none", "adobe_deflate"):
            raise ValueError("compression must be 'none' or 'adobe_deflate'")
        packed = (bit_depth not in (8, 16))  # uint16 container, packed BPS on disk
        if packed and compression != "none":
            raise ValueError(
                f"bit_depth {bit_depth} uses packed BitsPerSample, which tifffile "
                "cannot combine with compression; use --compression none "
                "(or bit_depth 8/16 with --compression adobe_deflate)"
            )

    def encode_split(
            self,
        payload: bytes,
        output_path: str,
        split_size: int,
        width: int = 2048,
        height: int = 1536,
        seed: int | None = None,
        key: bytes | None = None,
        lsb_planes: int = 1,
        bit_depth: int = 16,
        mode: str = "linear",
        compression: str = "none",
        no_randomize: bool = False,
        frames: int = 1,
        thumbnail: str = "random",
        split_id: str | None = None,
        split_id_field: str = "ImageUniqueID",
        split_seq_field: str = "ImageNumber",
        progress: bool | None = None,
    ) -> list[dict]:
        """Split `payload` into ≤`split_size`-byte chunks across DNG files.

        Each chunk is an independent framed payload (own header/CRC), so a
        short last chunk needs no padding. Files are named
        ``<stem>0001<suffix>`` … (DCF-style 4-digit sequences); chunk
        order/total travel in ``split_id_field`` (shared UUID) and
        ``split_seq_field`` (``"none"`` disables either). A payload
        fitting in one chunk yields a single plain file with no split
        markers at all. Returns one info dict per file.
        """
        if isinstance(split_size, bool) or not isinstance(split_size, int) \
                or split_size <= 0:
            raise ValueError(
                f"split_size must be a positive byte count (got {split_size!r})")
        self._validate_options(bit_depth, lsb_planes, frames, mode,
                               compression)
        id_spec, seq_spec = resolve_split_fields(split_id_field,
                                                 split_seq_field)
        uid = split_id if split_id is not None else new_split_id()
        if not isinstance(uid, str) or not uid:
            raise ValueError("split_id must be a non-empty string")
        try:
            uid.encode("ascii")
        except UnicodeEncodeError as exc:
            raise ValueError(
                f"split_id must be ASCII for metadata storage: {exc}") from exc
        chunks = iter_chunk_bounds(len(payload), split_size)
        # Peek the first item to learn the total without slicing any
        # payload bytes up front.
        first = next(chunks)
        _, total, _, _ = first
        if total == 1:
            # Fits in one chunk: plain single file, no split markers.
            return [self.encode(
                payload, output_path, width=width, height=height, seed=seed,
                key=key, lsb_planes=lsb_planes, bit_depth=bit_depth,
                mode=mode, compression=compression,
                no_randomize=no_randomize, frames=frames,
                thumbnail=thumbnail, progress=progress,
            )]
        ifd0_dummies = ((id_spec is not None and id_spec["ifd"] == "ifd0")
                        + (seq_spec is not None and seq_spec["ifd"] == "ifd0"))
        infos = []
        show = _progress_enabled(progress)
        with _progress_bar(total=total, desc="Encoding chunks", unit="file",
                            disable=not show) as outer:
            for seq, chunk_total, start, end in itertools.chain([first], chunks):
                assert chunk_total == total  # generator yields one fixed total
                # One chunk copy at a time: slicing all chunks up front
                # would hold a second full payload beside ``payload``.
                chunk = payload[start:end]
                chunk_len = len(chunk)
                path = chunk_path(output_path, seq)
                cseed = (None if (seed is None and not no_randomize)
                         else (0 if seed is None else seed) + seq - 1)
                meta = MetadataRandomizer(cseed).randomize()
                split_exif: dict[int, Any] = {}
                if id_spec is not None and id_spec["ifd"] == "exif":
                    split_exif[id_spec["tag"]] = uid
                if seq_spec is not None and seq_spec["ifd"] == "exif":
                    val: Any = format_seq_value(split_seq_field, seq, total)
                    split_exif[seq_spec["tag"]] = (
                        [val] if isinstance(val, int) else list(val))
                if split_exif:
                    meta["split_exif"] = split_exif
                if cseed is None:
                    # Unseeded run: fresh random base per chunk so chunks share
                    # neither cover pixels nor fallback thumbnails (identical
                    # high bits across chunks would be an obvious tell).
                    cs = random.randrange(1 << 30)
                else:
                    cs = cseed
                covers = [CoverGenerator(cs + f).cover(height, width, mode,
                                                       bit_depth)
                          for f in range(frames)]
                n_samples = covers[0].size
                cap = LsbCodec.capacity_bytes_total(n_samples, lsb_planes, frames)
                if chunk_len > cap:
                    raise ValueError(
                        f"chunk {seq}/{total} "
                        f"({format_kb_hi(chunk_len)}) exceeds per-file capacity "
                        f"{format_kb_lo(cap)} ({width}x{height} {mode} "
                        f"{bit_depth}-bit, {lsb_planes} LSB plane(s)"
                        f"{f' x {frames} frames' if frames > 1 else ''}). "
                        f"Lower --split-file to at most {format_kb_lo(cap)} or "
                        f"enlarge the geometry / add planes."
                    )
                frame = PayloadFrame.pack(chunk, key)
                del chunk
                stegos = LsbCodec.stripe_frames(
                    covers, frame, lsb_planes, progress=show,
                    desc=f"Embedding chunk {seq}/{total}", position=1)
                # stripe_frames embeds in place: stegos share the covers'
                # buffers, so drop the extra references promptly.
                del covers, frame
                tw, th = min(4000, width), min(3000, height)
                thumb, thumb_label = ThumbnailProvider(seed=cs).get(
                    tw, th, source=thumbnail)
                bigtiff = self._write_container(
                    path, stegos=stegos, thumb_rgb=thumb, meta=meta,
                    width=width, height=height, mode=mode, bit_depth=bit_depth,
                    compression=compression, frames=frames, tw=tw, th=th,
                    ifd0_dummies=ifd0_dummies,
                )
                self._write_split_tags(path, id_spec, seq_spec, split_id_field,
                                       split_seq_field, uid, seq, total)
                info = self._file_info(
                    path, width=width, height=height, mode=mode,
                    bit_depth=bit_depth, container=str(stegos[0].dtype),
                    lsb_planes=lsb_planes, frames=frames,
                    thumb_label=thumb_label, bigtiff=bigtiff, cap=cap,
                    payload_len=chunk_len, meta=meta,
                )
                info.update({"chunk_seq": seq, "chunk_total": total,
                             "split_id": uid, "split_id_field": split_id_field,
                             "split_seq_field": split_seq_field})
                infos.append(info)
                del stegos, thumb
                outer.update(1)
        return infos

    @staticmethod
    def _write_split_tags(path: str, id_spec, seq_spec, id_field: str,
                          seq_field: str, uid: str, seq: int,
                          total: int) -> None:
        """Apply IFD0-bound split markers via reserved dummy tags."""
        dummy = 65001
        if id_spec is not None and id_spec["ifd"] == "ifd0":
            append_ifd0_ascii(path, dummy, id_spec["tag"], uid)
            dummy += 1
        if seq_spec is not None and seq_spec["ifd"] == "ifd0":
            if seq_field == "ImageDescription":
                append_ifd0_ascii(path, dummy, seq_spec["tag"],
                                  f"{seq:04d}/{total:04d}")
            else:
                val = format_seq_value(seq_field, seq, total)
                if isinstance(val, int):
                    val = (val,)
                set_ifd0_tag(path, dummy, seq_spec["tag"],
                             seq_spec["dtype"], val)


    @staticmethod
    def _decode_with_planes(
        raws: list[np.ndarray],
        key: bytes | None,
        lsb_planes: int,
        max_bytes: int | None = None,
        progress: bool | None = None,
        desc: str = "Extracting",
        position: int = 0,
    ) -> bytes:
        """Single-plane-count decode attempt across ordered raw frames.

        The framed bitstream is striped over frames in write order; gather
        the needed prefix of the concatenated LSB stream. Raises ValueError
        on failure. Header is read first (144 bits, tiny); the full frame
        is then streamed via :meth:`LsbCodec.extract_stream` so large
        payloads never materialize the ~8x bit-expanded array.

        ``max_bytes`` is an opt-in safety cap (``None`` means bounded only
        by the image capacity); it guards against allocating a huge buffer
        from a bogus header before the capacity check runs.
        """
        head = LsbCodec.extract_bitarray(raws[0], lsb_planes, PayloadFrame.HEADER_LEN * 8)
        header = np.packbits(head).tobytes()
        if key:
            header = PayloadFrame._xor_data(header, key)
        if header[:4] != PayloadFrame.MAGIC:
            raise ValueError("no magic")
        (pay_len,) = struct.unpack(">Q", header[6:14])
        total_bits = (PayloadFrame.HEADER_LEN + pay_len) * 8
        if max_bytes is not None and pay_len > max_bytes:
            raise _DecodeLimitError(
                f"declared payload {format_kb_hi(pay_len)} exceeds "
                f"max_bytes limit {format_kb_lo(max_bytes)} "
                f"(pass --max-bytes larger than "
                f"{format_kb_lo(max_bytes)})")
        total_slots = sum(int(raw.size) * lsb_planes for raw in raws)
        if total_bits > total_slots:
            raise _DecodeLimitError(
                "declared payload exceeds image capacity")
        stream = LsbCodec.extract_stream(raws, lsb_planes, total_bits,
                                             progress=progress, desc=desc,
                                             position=position)
        payload, _ = PayloadFrame.unpack(stream, key)
        return payload

    def decode(
            self,
        input_path: str | list[str],
        key: bytes | None = None,
        lsb_planes: int | None = None,
        max_bytes: int | None = None,
        split_id_field: str = "ImageUniqueID",
        split_seq_field: str = "ImageNumber",
        progress: bool | None = None,
    ) -> bytes:
        """Extract a payload from one DNG, or concatenate chunked DNGs.

        Multiple inputs are treated as a chunk set and verified: split
        metadata (when the configured fields are present) must agree on
        one shared UUID with consecutive sequences, otherwise the
        filenames must form a consecutive 0001-based sequence. A lone
        file carrying split markers decodes with a partial-data warning.

        ``max_bytes`` caps the accepted declared payload per file
        (``None`` — the default — means bounded only by the image
        capacity, so any file this tool can encode also decodes).
        For untrusted files, pass an explicit ``max_bytes`` to bound
        the allocation before the capacity check runs.
        """
        if lsb_planes is not None and not (1 <= lsb_planes <= MAX_LSB_PLANES):
            raise ValueError(f"lsb_planes must be 1-{MAX_LSB_PLANES}")
        resolve_split_fields(split_id_field, split_seq_field)
        paths = [input_path] if isinstance(input_path, str) else list(input_path)
        if not paths:
            raise ValueError("no input files given")
        if len(paths) == 1:
            payload = self._decode_one(paths[0], key, lsb_planes, max_bytes,
                                       progress=progress)
            markers = DngContainer(paths[0]).split_markers(split_id_field,
                                                           split_seq_field)
            if markers["seq_present"] or markers["id_present"]:
                total = markers["total"] or "?"
                warnings.warn(
                    f"{paths[0]} carries split metadata (chunk "
                    f"{markers['seq'] or '?'} of {total}): decoding one "
                    f"chunk returns partial data; pass every chunk file to "
                    f"restore the whole payload.")
            return payload
        return self._decode_many(paths, key=key, lsb_planes=lsb_planes,
                                 max_bytes=max_bytes,
                                 id_field=split_id_field,
                                 seq_field=split_seq_field,
                                 progress=progress)

    def _decode_one(
            self,
        input_path: str,
        key: bytes | None = None,
        lsb_planes: int | None = None,
        max_bytes: int | None = None,
        progress: bool | None = None,
        desc: str = "Extracting",
        position: int = 0,
    ) -> bytes:
        """Decode a single DNG (chunk or whole payload)."""
        if lsb_planes is not None and not (1 <= lsb_planes <= MAX_LSB_PLANES):
            raise ValueError(f"lsb_planes must be 1-{MAX_LSB_PLANES}")
        raws = DngContainer(input_path).raw_frames()
        candidates = ([lsb_planes] if lsb_planes is not None
                      else list(range(1, MAX_LSB_PLANES + 1)))
        last_err: ValueError | None = None
        limit_err: ValueError | None = None
        for p in candidates:
            try:
                return self._decode_with_planes(raws, key, p, max_bytes,
                                                    progress=progress,
                                                    desc=desc,
                                                    position=position)
            except ValueError as exc:
                # A magic match with a bad length means the right plane was
                # found but the payload was rejected (cap/capacity). Surface
                # that instead of a later plane's generic "no magic", which
                # would misdirect (wrong-key hint) for non-16-plane payloads.
                if isinstance(exc, _DecodeLimitError):
                    limit_err = limit_err or exc
                last_err = exc
        if limit_err is not None:
            raise limit_err
        if lsb_planes is not None:
            raise ValueError(
                "magic not found - wrong key, wrong LSB depth/mode or no payload"
            )
        raise ValueError(
            f"no decodable payload at 1-{MAX_LSB_PLANES} LSB planes - wrong key "
            "or no payload "
            f"(last error: {last_err})"
        )

    def _decode_many(self, paths: list[str], *, key: bytes | None,
                     lsb_planes: int | None, max_bytes: int | None,
                     id_field: str, seq_field: str,
                     progress: bool | None = None) -> bytes:
        """Verify a chunk set (metadata, else filenames) and concatenate."""
        markers = []
        for p in paths:
            try:
                markers.append(DngContainer(p).split_markers(id_field,
                                                             seq_field))
            except ValueError as exc:
                raise ValueError(f"{p}: {exc}") from exc
        id_active = id_field != "none"
        seq_active = seq_field != "none"

        def _has(m: dict) -> bool:
            return ((not id_active or m["id_present"])
                    and (not seq_active or m["seq_present"]))

        def _has_any(m: dict) -> bool:
            return ((id_active and m["id_present"])
                    or (seq_active and m["seq_present"]))

        n_all = sum(1 for m in markers if _has(m))
        n_any = sum(1 for m in markers if _has_any(m))
        if id_active or seq_active:
            if n_all == len(paths):
                ordered = self._order_by_markers(paths, markers, id_active,
                                                 seq_active)
            elif n_any == 0:
                ordered = self._order_by_names(paths)
            else:
                partial = [p for p, m in zip(paths, markers)
                           if not _has(m) and _has_any(m)]
                if len(partial) == len(paths):
                    lacking = sorted(
                        {name for name, active, key in
                         (("id", id_active, "id_present"),
                          ("sequence", seq_active, "seq_present"))
                         if active and not any(m[key] for m in markers)})
                    raise ValueError(
                        "every file carries split markers, but none carries "
                        f"{' and '.join(lacking)} markers "
                        f"({', '.join(sorted(partial))}). Re-encode with "
                        f"matching --split-file-metadata-* fields, or pass "
                        f"the same field names used at encode time to "
                        f"decode.")
                missing = sorted(p for p, m in zip(paths, markers)
                                 if not _has(m))
                raise ValueError(
                    "inconsistent split metadata: these files carry chunk "
                    "markers but these do not: "
                    f"{missing}. Pass a consistent set — either every file "
                    "with markers, or plain files following the 0001 naming "
                    "convention. (If you encoded with non-default "
                    "--split-file-metadata-id/seq names, pass the same "
                    "ones to decode.)")
        else:
            ordered = self._order_by_names(paths)
        out = bytearray()
        show = _progress_enabled(progress)
        with _progress_bar(total=len(ordered), desc="Decoding chunks",
                            unit="file", disable=not show) as outer:
            for i, p in enumerate(ordered, 1):
                try:
                    out += self._decode_one(p, key, lsb_planes, max_bytes,
                                            progress=show,
                                            desc=f"Extracting chunk {i}/{len(ordered)}",
                                            position=1 if show else 0)
                except ValueError as exc:
                    raise ValueError(f"{p}: {exc}") from exc
                outer.update(1)
        return bytes(out)

    @staticmethod
    def _order_by_markers(paths: list[str], markers: list[dict],
                          id_active: bool, seq_active: bool) -> list[str]:
        """Order chunks via metadata; enforce one set + 1..N sequences."""
        if id_active:
            uids = {m["id"] for m in markers}
            if len(uids) != 1:
                detail = "; ".join(f"{p}: {m['id']}"
                                   for p, m in zip(paths, markers))
                raise ValueError(
                    "chunk files belong to different sets (shared UUIDs "
                    f"differ): {detail}. Pass chunks of one split only.")
        if seq_active:
            seqs = [m["seq"] for m in markers]
            if len(set(seqs)) != len(seqs):
                dupes = sorted(s for s in set(seqs) if seqs.count(s) > 1)
                raise ValueError(
                    f"duplicate chunk numbers "
                    f"{', '.join(f'{s:04d}' for s in dupes)}; pass each "
                    f"chunk once.")
            order = sorted(range(len(paths)), key=lambda i: seqs[i])
            if sorted(seqs) != list(range(1, len(paths) + 1)):
                if seqs and min(seqs) != 1:
                    missing = [i for i in range(1, min(seqs))]
                    raise ValueError(
                        f"chunk sequence starts at {min(seqs):04d}, not "
                        f"0001: likely missing file(s) "
                        f"{', '.join(f'{i:04d}' for i in missing)}.")
                missing = [i for i in range(1, max(seqs) + 1)
                           if i not in seqs]
                raise ValueError(
                    f"chunk numbers not consecutive "
                    f"(got {', '.join(f'{s:04d}' for s in sorted(seqs))}): "
                    f"missing chunk(s) {', '.join(f'{i:04d}' for i in missing)}.")
            totals = {m["total"] for m in markers if m["total"] is not None}
            if len(totals) > 1:
                raise ValueError(
                    f"conflicting chunk totals: {sorted(totals)}.")
            if totals and next(iter(totals)) != len(paths):
                total = next(iter(totals))
                missing = [i for i in range(1, total + 1) if i not in seqs]
                raise ValueError(
                    f"chunk metadata declares {total} total chunks but "
                    f"{len(paths)} files were given; missing chunk(s): "
                    f"{', '.join(f'{i:04d}' for i in missing)}.")
            return [paths[i] for i in order]
        # id-only markers: order still needs filenames.
        return DngStego._order_by_names(paths)

    @staticmethod
    def _order_by_names(paths: list[str]) -> list[str]:
        """Order chunk files by 4-digit names; require 1..N consecutive."""
        parsed = []
        for p in paths:
            r = parse_chunk_name(p)
            if r is None:
                raise ValueError(
                    f"{p}: no split metadata found in any file, and this "
                    f"name lacks a 4-digit sequence number like "
                    f"out0001.dng. Encode with --split-file, or pass files "
                    f"named <stem>NNNN.<ext>.")
            stem, num, suffix = r
            parsed.append((p, stem, num, suffix))
        if len({s for _, s, _, _ in parsed}) != 1 \
                or len({s for _, _, _, s in parsed}) != 1:
            detail = ", ".join(sorted({p for p, _, _, _ in parsed}))
            raise ValueError(
                f"chunk filenames mix stems/suffixes ({detail}); pass one "
                f"sequence with a shared stem like out0001.dng.")
        nums = sorted(n for _, _, n, _ in parsed)
        if len(set(nums)) != len(nums):
            dupes = sorted({n for n in nums if nums.count(n) > 1})
            raise ValueError(
                f"duplicate chunk numbers "
                f"{', '.join(f'{n:04d}' for n in dupes)}; pass each chunk "
                f"once.")
        if nums != list(range(1, len(nums) + 1)):
            if nums[0] != 1:
                missing = [i for i in range(1, nums[0])]
                raise ValueError(
                    f"chunk sequence starts at {nums[0]:04d}, not 0001: "
                    f"likely missing file(s) "
                    f"{', '.join(f'{i:04d}' for i in missing)}.")
            missing = [i for i in range(1, nums[-1] + 1) if i not in nums]
            raise ValueError(
                f"chunk numbers not consecutive "
                f"(got {', '.join(f'{n:04d}' for n in nums)}): missing "
                f"chunk(s) {', '.join(f'{i:04d}' for i in missing)}.")
        by_num = {}
        for p, _, n, _ in parsed:
            by_num[n] = p
        return [by_num[n] for n in nums]

    def generate_tiff(
            self,
        output_path: str,
        width: int = 2048,
        height: int = 1536,
        seed: int | None = None,
    ) -> str:
        """Generate a plain (non-stego) TIFF cover for testing/comparison."""
        cover8 = (CoverGenerator(seed).cover(height, width, "linear", 16) // 257).astype(np.uint8)
        with tifffile.TiffWriter(output_path) as tif:
            tif.write(
                np.ascontiguousarray(cover8), photometric="rgb",
                software=self.profile.software, metadata=None,
            )
        return output_path


_DEFAULT = DngStego()


def encode(
    payload: bytes,
    output_path: str,
    width: int = 2048,
    height: int = 1536,
    seed: int | None = None,
    key: bytes | None = None,
    lsb_planes: int = 1,
    bit_depth: int = 16,
    mode: str = "linear",
    compression: str = "none",
    no_randomize: bool = False,
    frames: int = 1,
    thumbnail: str = "random",
    progress: bool | None = None,
) -> dict:
    """Backwards-compatible wrapper (see :meth:`DngStego.encode`)."""
    return _DEFAULT.encode(
        payload, output_path, width=width, height=height, seed=seed,
        key=key, lsb_planes=lsb_planes, bit_depth=bit_depth, mode=mode,
        compression=compression, no_randomize=no_randomize, frames=frames,
        thumbnail=thumbnail, progress=progress,
    )


def decode(
    input_path: str | list[str],
    key: bytes | None = None,
    lsb_planes: int | None = None,
    max_bytes: int | None = None,
    split_id_field: str = "ImageUniqueID",
    split_seq_field: str = "ImageNumber",
    progress: bool | None = None,
) -> bytes:
    """Backwards-compatible wrapper (see :meth:`DngStego.decode`)."""
    return _DEFAULT.decode(
        input_path, key=key, lsb_planes=lsb_planes, max_bytes=max_bytes,
        split_id_field=split_id_field, split_seq_field=split_seq_field,
        progress=progress)


def encode_split(
    payload: bytes,
    output_path: str,
    split_size: int,
    width: int = 2048,
    height: int = 1536,
    seed: int | None = None,
    key: bytes | None = None,
    lsb_planes: int = 1,
    bit_depth: int = 16,
    mode: str = "linear",
    compression: str = "none",
    no_randomize: bool = False,
    frames: int = 1,
    thumbnail: str = "random",
    split_id: str | None = None,
    split_id_field: str = "ImageUniqueID",
    split_seq_field: str = "ImageNumber",
    progress: bool | None = None,
) -> list[dict]:
    """Backwards-compatible wrapper (see :meth:`DngStego.encode_split`)."""
    return _DEFAULT.encode_split(
        payload, output_path, split_size, width=width, height=height,
        seed=seed, key=key, lsb_planes=lsb_planes, bit_depth=bit_depth,
        mode=mode, compression=compression, no_randomize=no_randomize,
        frames=frames, thumbnail=thumbnail, split_id=split_id,
        split_id_field=split_id_field, split_seq_field=split_seq_field,
        progress=progress)


def generate_tiff(
    output_path: str,
    width: int = 2048,
    height: int = 1536,
    seed: int | None = None,
) -> str:
    """Backwards-compatible wrapper (see :meth:`DngStego.generate_tiff`)."""
    return _DEFAULT.generate_tiff(
        output_path, width=width, height=height, seed=seed)
