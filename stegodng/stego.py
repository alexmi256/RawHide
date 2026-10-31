"""High-level API: :class:`DngStego` (encode/decode/generate).

Thin module-level :func:`encode` / :func:`decode` / :func:`generate_tiff`
wrappers preserve the original single-file API.
"""
from __future__ import annotations

import datetime as _dt
import itertools
import os
import random
import struct
import warnings
from typing import Any

import numpy as np
import tifffile
from PIL import Image

from . import geo
from .codec import LsbCodec, format_kb_hi, format_kb_lo
from .container import (
    DngContainer,
    XMP_LEN,
    append_ifd0_ascii,
    build_xmp,
    set_ifd0_tag,
)
from .cover import CoverGenerator
from .debugmeta import build_debug_document, crc32_hex, write_debug_metadata
from .digests import new_raw_image_digest, raw_data_unique_id
from .filetime import normalize_image_time
from .framing import PayloadFrame
from .metadata import MetadataRandomizer
from .opcodes import build_opcode_list2
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


# CFA pattern name -> (top-left, top-right, bottom-left, bottom-right)
# colour codes (0=R, 1=G, 2=B).  Default stays RGGB for byte stability.
_CFA_CODES = {
    "RGGB": (0, 1, 1, 2),
    "BGGR": (2, 1, 1, 0),
    "GRBG": (1, 0, 2, 1),
    "GBRG": (1, 2, 0, 1),
}


class _DecodeLimitError(ValueError):
    """Declared payload rejected by the cap or image capacity.

    Subclass of ValueError (so existing ``except ValueError`` callers are
    unaffected); lets ``_decode_one`` recognize limit rejections by type
    instead of fragile message-substring matching.
    """


class DngStego:
    """Embed and recover payloads in DNG raw sensor data."""

    def __init__(self, profile=DEFAULT_PROFILE,
                 level_policy: str = "profile") -> None:
        # Explicit None means "default story" (module wrappers pass
        # through a missing profile this way).
        self.profile = profile if profile is not None else DEFAULT_PROFILE
        if level_policy not in ("profile", "strict", "capacity"):
            raise ValueError(
                "level_policy must be profile, strict or capacity")
        self.level_policy = level_policy

    @staticmethod
    def _rgb_to_ycbcr(thumb_rgb) -> "np.ndarray":
        # tifffile stores YCbCr JPEG planes verbatim (no RGB conversion),
        # so convert up front; the tag stays YCbCr like the combiner files.
        return np.ascontiguousarray(
            np.asarray(Image.fromarray(thumb_rgb).convert("YCbCr")))

    def _thumbnail_size(self, width: int, height: int) -> tuple[int, int]:
        fidelity = self.profile.fidelity
        if fidelity and fidelity.preview_size:
            return fidelity.preview_size
        return min(4000, width), min(3000, height)

    def _levels(self, mode: str, bit_depth: int):
        white = self.profile.effective_white(bit_depth, self.level_policy)
        black = self.profile.effective_black_levels(
            mode, bit_depth, self.level_policy)
        n = 3 if mode == "linear" else 1
        return black, (white,) * n

    def _ifd0_extras(self, meta: dict, n_dummies: int = 0,
                     digest_tags: tuple | list = ()) -> list:
        fidelity = self.profile.fidelity
        adobe = fidelity is not None and fidelity.tag_conventions == "adobe"
        if adobe:
            # Adobe writes these rationals at fixed denominators; keeping
            # them (1e6 scaling, hundredth EV) avoids a batch-wide pattern.
            analog = [(1000000, 1000000)] * 3
            neutral = [(n * 100, 1000000) for n, _d in meta["as_shot_neutral"]]
            baseline = [(int(round(meta["baseline_exposure"][0] / 100)), 100)]
            shadow = [(1, 1)]
        else:
            analog = [(10000, 10000)] * 3
            neutral = meta["as_shot_neutral"]
            baseline = [meta["baseline_exposure"]]
            shadow = [self.profile.shadow_scale]
        extras = [
            (271, "s", 0, self.profile.make, True),
            (272, "s", 0, self.profile.model, True),
            (274, 3, 1, (int(meta.get("orientation", 1)),), True),
        ]
        if fidelity is None or fidelity.emit_xmp:
            extras.append((700, "B", XMP_LEN, build_xmp(), True))
        extras += [
            (50706, "B", 4, self.profile.dng_version, True),
            (50707, "B", 4, self.profile.dng_backward, True),
            (50708, "s", 0, self.profile.unique_camera_model, True),
            (50721, 10, 9, self.profile.color_matrix1, True),
            (50722, 10, 9, self.profile.color_matrix2, True),
            (50727, 5, 3, analog, True),
            (50728, 5, 3, neutral, True),
            (50730, 10, 1, baseline, True),
            (50731, 5, 1, [self.profile.baseline_noise], True),
            (50732, 5, 1, [self.profile.baseline_sharpness], True),
            (50734, 5, 1, [self.profile.linear_response_limit], True),
        ]
        if adobe:
            # Adobe re-wraps the preview JPEG with its own YCbCr
            # coefficients/positioning; without them the preview tags are
            # only half of what the reference files carry.
            extras.append((529, 5, 3, [
                (299, 1000), (587, 1000), (114, 1000)], True))
            extras.append((531, 3, 1, (1,), True))
        if fidelity is None or fidelity.emit_serials:
            extras.append((50735, "s", 0, meta["camera_serial"], True))
        if fidelity is None or fidelity.emit_lens:
            extras.append((50736, 5, 4, [
                (meta["lens_spec"][0], meta["lens_spec"][1]),
                (meta["lens_spec"][2], meta["lens_spec"][3]),
                (meta["lens_spec"][4], meta["lens_spec"][5]),
                (meta["lens_spec"][6], meta["lens_spec"][7]),
            ], True))
        extras += [
            (50739, 5, 1, shadow, True),
            (50778, 3, 1, (self.profile.calib_illuminant1,), True),
            (50779, 3, 1, (self.profile.calib_illuminant2,), True),
        ]
        if fidelity is not None and fidelity.adobe is not None:
            adobe = fidelity.adobe
            if adobe.forward_matrix1:
                extras.append((50964, 10, 9, adobe.forward_matrix1, True))
            if adobe.forward_matrix2:
                extras.append((50965, 10, 9, adobe.forward_matrix2, True))
            if adobe.name:
                extras.append((50936, "s", 0, adobe.name, True))
            if adobe.calibration_signature:
                extras.append((50932, "s", 0,
                               adobe.calibration_signature, True))
            if adobe.copyright:
                extras.append((50942, "s", 0, adobe.copyright, True))
            if adobe.embed_policy is not None:
                extras.append((50941, 4, 1, (adobe.embed_policy,), True))
            if adobe.hue_sat_map_dims is not None:
                extras.append((50937, 4, 3, adobe.hue_sat_map_dims, True))
                for tag, blob in (
                        (50938, adobe.hue_sat_map_data1),
                        (50939, adobe.hue_sat_map_data2)):
                    if blob is None:
                        continue
                    values = np.frombuffer(blob, dtype="<f4").astype(float).tolist()
                    extras.append((tag, 11, len(values), values, True))
            if adobe.look_table_dims is not None:
                extras.append((50981, 4, 3, adobe.look_table_dims, True))
                if adobe.look_table_data is not None:
                    values = np.frombuffer(
                        adobe.look_table_data, dtype="<f4").astype(float).tolist()
                    extras.append((50982, 11, len(values), values, True))
        if meta.get("noise_profile") is not None:
            extras.append((51041, 12, 6, list(meta["noise_profile"]), True))
        if meta.get("makernote"):
            # DNG 1.3: tells editors the MakerNote is safe to copy.
            extras.append((50741, 3, 1, (1,), True))
        extras.extend(digest_tags)
        if meta.get("gps") is not None:
            # Repurposed into GPSTag (34853) after the GPS IFD is appended.
            extras.append((65010, 3, 1, (0,), True))
        # Dummy private tag repurposed into ExifTag (34665) after
        # writing: tifffile filters IFD-pointer tags from extratags,
        # so the EXIF Sub-IFD offset is patched in post (same 12-byte
        # entry, no shifting required).
        extras.append((65000, 3, 1, (0,), True))
        # Reserved dummies repurposed post-write into split seq/id tags.
        for i in range(n_dummies):
            extras.append((65001 + i, 4, 1, (0,), True))
        return extras

    def _crop_rect(self, width: int, height: int) -> tuple[int, int, int, int]:
        """DefaultCropOrigin/Size as (x, y, w, h) for the current profile."""
        fidelity = self.profile.fidelity
        if fidelity and fidelity.crop_margin:
            mx, my = fidelity.crop_margin
            if width <= 2 * mx or height <= 2 * my:
                raise ValueError(
                    f"crop_margin {fidelity.crop_margin} leaves no image in "
                    f"{width}x{height}")
            return (mx, my, width - 2 * mx, height - 2 * my)
        return (0, 0, width, height)

    def _sub_extras(self, meta: dict, mode: str, width: int, height: int,
                    bit_depth: int, seed: int = 0,
                    opcode2: bytes | None = None) -> list:
        black, white_t = self._levels(mode, bit_depth)
        fidelity = self.profile.fidelity
        adobe = fidelity is not None and fidelity.tag_conventions == "adobe"
        opcode = self.profile.opcode_list3
        if mode == "linear":
            extras = [
                (50714, 4, 3, black, True),
                (50717, 4, 3, white_t, True),
                (50718, 5, 2, [(1, 1), (1, 1)], True),
                (50719, 5, 2, [(0, 1), (0, 1)], True),
                (50720, 5, 2, [(width, 1), (height, 1)], True),
                (50738, 5, 1, [(100, 100)], True),
                (50780, 5, 1, [(1, 1) if fidelity else (100, 100)], True),
                (51022, 7, len(opcode), opcode, True),
            ]
            return extras
        pattern = (self.profile.cfa_pattern or "RGGB").upper()
        codes = _CFA_CODES.get(pattern, _CFA_CODES["RGGB"])
        # Real DNGs store CFAPattern as BYTE; keep the legacy SHORT form for
        # profiles that do not declare a pattern so the GFX output stays
        # byte-identical.
        cfa_tag = ((33422, 1, 4, bytes(codes), True)
                   if self.profile.cfa_pattern
                   else (33422, 3, 4, codes, True))
        if fidelity and fidelity.black_levels:
            black_tag = (50714, 5, len(black),
                         [(v, 1) for v in black], True)
            white_tag = (50717, 3, 1, (white_t[0],), True)
        else:
            black_tag = (50714, 4, 1, black, True)
            white_tag = (50717, 4, 1, white_t, True)
        crop_x, crop_y, crop_w, crop_h = self._crop_rect(width, height)
        active = (0, 0, height, width) if crop_w != width else None
        plane_color = ((50710, 1, 3, bytes((0, 1, 2)), True) if adobe
                       else (50710, 3, 3, (0, 1, 2), True))
        extras = [
            plane_color,                      # CFAPlaneColor R,G,B
            (50711, 3, 1, (1,), True),        # CFALayout rectangular
            black_tag,
            white_tag,
            (50718, 5, 2, [(1, 1), (1, 1)], True),
            (50719, 5, 2, [(crop_x, 1), (crop_y, 1)], True),
            (50720, 5, 2, [(crop_w, 1), (crop_h, 1)], True),
            (50738, 5, 1, [(100, 100)], True),
            (50780, 5, 1, [(1, 1) if fidelity else (100, 100)], True),
            (33421, 3, 2, (2, 2), True),
            cfa_tag,
        ]
        if fidelity and fidelity.black_levels and len(black) == 4:
            extras.append((50713, 3, 2, (2, 2), True))
        if fidelity and fidelity.bayer_green_split is not None:
            extras.append((50733, 4, 1,
                           (fidelity.bayer_green_split,), True))
        if active is not None:
            extras.append((50829, 4, 4, active, True))
            extras.append((51125, 5, 4, [
                (0, 1), (0, 1), (1, 1), (1, 1)], True))
        if self.profile.gainmap is not None:
            # Pixel XL style: four per-phase GainMaps in OpcodeList2 and no
            # OpcodeList3.  The maps are regenerated per file from the
            # profile base grid so a batch never shares an identical blob.
            if opcode2 is None:
                opcode2 = build_opcode_list2(
                    width, height, seed=seed, config=self.profile.gainmap)
            extras.append((51009, 7, len(opcode2), opcode2, True))
        else:
            extras.append((51022, 7, len(opcode), opcode, True))
        return extras

    def _write_container(self, output_path: str, *, stegos: list,
                         thumb_rgb, meta: dict, width: int, height: int,
                         mode: str, bit_depth: int, compression: str,
                         frames: int, tw: int, th: int,
                         ifd0_dummies: int = 0, seed: int = 0) -> bool:
        """Write thumbnail + raw frames, patch photometrics, attach EXIF.

        ``ifd0_dummies`` reserves that many private LONG tags (65001+)
        for post-write split seq/id fields. Returns the bigtiff flag.

        The profile's MakerNote is attached here (not in ``encode``) so
        the split path, which builds its own metadata per chunk, gets it
        too; ``seed`` is the same value both callers already pass for the
        cover/gain-map/metadata stream.
        """
        self._attach_makernote(meta, seed)
        thumb_ycbcr = self._rgb_to_ycbcr(thumb_rgb)
        bytes_per_sample = 1 if bit_depth <= 8 else 2
        bigtiff = (
            width * height * (3 if mode == "linear" else 1)
            * bytes_per_sample * frames
        ) > 3_500_000_000
        photo_main = "rgb" if mode == "linear" else "cfa"  # patched to LinearRaw later
        fidelity = self.profile.fidelity
        tile = (fidelity.tile if fidelity and fidelity.tile
                else ((96, 128) if (width >= 128 and height >= 96) else None))
        # Uncompressed by default: LibRaw/rawpy (tested 0.27) decodes
        # uncompressed DNG but fails on Adobe-Deflate DNG ("unexpected EOF").
        # Deflate stays available as an opt-in for smaller files; it is still
        # lossless so the LSB payload survives either way.
        use_deflate = compression == "adobe_deflate"

        # OpcodeList2 is generated once so the RawDataUniqueID can be
        # derived from the exact blob that lands in the file.
        opcode2 = None
        if self.profile.gainmap is not None:
            opcode2 = build_opcode_list2(
                width, height, seed=seed, config=self.profile.gainmap)

        container = DngContainer(output_path)
        digest_tags: list[tuple] = []
        if fidelity is not None and fidelity.raw_digests and frames == 1:
            digest_tags = self._digest_tags(stegos[0], mode, opcode2)

        with tifffile.TiffWriter(output_path, bigtiff=bigtiff) as tif:
            ifd0_extras = self._ifd0_extras(
                meta, n_dummies=ifd0_dummies, digest_tags=digest_tags)
            tif.write(
                thumb_ycbcr, photometric="ycbcr", compression="jpeg",
                # Empty Software (profiles with no observed Software
                # string) omits tag 305 explicitly instead of relying on
                # tifffile skipping empty strings.
                software=(meta.get("software") or self.profile.software
                          or False),
                datetime=meta["datetime"],
                rowsperstrip=th,
                subfiletype=1, subifds=frames, metadata=None, extratags=ifd0_extras,
            )
            sub_extras = self._sub_extras(meta, mode, width, height,
                                          bit_depth, seed=seed,
                                          opcode2=opcode2)
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
            container.patch_linear_raw()
        if fidelity is not None:
            meta.setdefault("fidelity_layout", False)
            allow = fidelity.exif_allow
            if mode != "cfa" and allow is not None:
                allow = tuple(tag for tag in allow if tag != 41730)
            meta.setdefault("exif_allow", allow)
            meta.setdefault("emit_serials", fidelity.emit_serials)
            meta.setdefault("emit_lens", fidelity.emit_lens)
            if (mode == "cfa"
                    and (self.profile.cfa_pattern or "").upper() == "BGGR"):
                meta.setdefault(
                    "photo_cfa_pattern",
                    b"\x02\x00\x02\x00\x02\x01\x01\x00")
        container.append_exif(meta, tw, th)
        if meta.get("gps") is not None:
            container.append_gps(meta["gps"])
        if fidelity is not None and fidelity.tag_conventions == "adobe":
            self._apply_adobe_tag_conventions(container)
        return bigtiff

    def _digest_tags(self, raw, mode: str,
                     opcode2: bytes | None) -> list[tuple]:
        """NewRawImageDigest + RawDataUniqueID entries for the IFD0.

        Only valid for a single raw frame: the digest describes one raw
        image, so multi-frame files go without (see README).  The crop
        rectangle and opcode lists must be the ones actually written:
        linear raws use the full frame and only carry OpcodeList3.
        """
        height, width = raw.shape[:2]
        if mode == "cfa":
            crop_x, crop_y, crop_w, crop_h = self._crop_rect(width, height)
            lists = (None, opcode2,
                     None if self.profile.gainmap is not None
                     else self.profile.opcode_list3)
        else:
            crop_x, crop_y, crop_w, crop_h = 0, 0, width, height
            lists = (None, None, self.profile.opcode_list3)
        digest = new_raw_image_digest(raw)
        uid = raw_data_unique_id(
            digest, self.profile.unique_camera_model,
            crop_size=((crop_w, 1), (crop_h, 1)),
            crop_origin=((crop_x, 1), (crop_y, 1)),
            opcode_lists=lists,
        )
        return [
            (51111, "B", 16, digest, True),
            (50781, "B", 16, uid, True),
        ]

    @staticmethod
    def _apply_adobe_tag_conventions(container: DngContainer) -> None:
        """Match the tag inventory of Adobe re-wrapped DNGs.

        The TIFF writer always emits X/YResolution and ResolutionUnit and
        stores SubIFDs as type IFD; Adobe (and the reference files) carry
        neither, and it only writes PlanarConfiguration for multi-sample
        pages, so the raw SubIFD gets tag 284 patched in while the freed
        entry slots are still available.
        """
        ifd0 = container.ifd0_offset()
        container.drop_ifd_tags(ifd0, (282, 283, 296))
        for offset in container.subifd_offsets():
            # tifffile writes PlanarConfiguration itself for multi-sample
            # pages (linear raws); only CFA SubIFDs need it patched in,
            # and a second 284 entry would be invalid.
            missing = container.entry_uint(offset, 284) is None
            container.rewrite_ifd_entries(
                offset, drop=(282, 283, 296),
                add=[(284, 3, 1, b"\x01\x00")] if missing else [])
        if not container.is_bigtiff:
            # BigTIFF stores SubIFD offsets as IFD8 (type 18); retyping
            # those to LONG (4) makes readers take 8-byte offsets as
            # 4-byte values and corrupts the directory.
            container.set_entry_type(ifd0, 330, 4)
        # tifffile rounds a JPEG preview's RowsPerStrip up to an MCU
        # multiple (512 for a 506-row preview); the reference files store
        # the full preview height, which is still a single strip.
        height = container.entry_uint(ifd0, 257)
        if height is not None:
            container.set_entry_uint(ifd0, 278, height)

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
            # The MakerNote blob is per-file binary noise, not metadata a
            # caller wants to inspect; keep it out of the info dict.
            "metadata": {k: v for k, v in meta.items() if k != "makernote"},
        }

    def _debug_options(self, *, width: int, height: int,
                       seed: int | None, key: bytes | None,
                       lsb_planes: int, bit_depth: int, mode: str,
                       compression: str, no_randomize: bool, frames: int,
                       thumbnail: str,
                       image_time: _dt.datetime | None = None,
                       gps_radius_km: float = geo.MAX_RADIUS_KM,
                       location_seed: int | None = None) -> dict:
        """The resolved encode knobs recorded in the debug sidecar."""
        return {
            "width": width,
            "height": height,
            "seed": seed,
            "keyed": key is not None,
            "lsb_planes": lsb_planes,
            "bit_depth": bit_depth,
            "mode": mode,
            "compression": compression,
            "no_randomize": no_randomize,
            "frames": frames,
            "thumbnail": thumbnail,
            "image_time": (image_time.isoformat(timespec="seconds")
                           if image_time is not None else None),
            "gps_radius_km": gps_radius_km,
            # Split sets draw the shared fix outside the per-chunk stream;
            # record that seed so the sidecar stays reproducible.
            "location_seed": location_seed,
            "camera_profile": self.profile.slug,
            "camera_profile_name": (self.profile.display_name
                                    or self.profile.model),
            "level_policy": self.level_policy,
        }

    def _debug_sidecar(self, output_path: str, info: dict, *, options: dict,
                       meta: dict, thumbnail_requested: str,
                       thumbnail_label: str, thumbnail_rgb, stegos: list,
                       cover_seed: int | None, metadata_seed: int | None,
                       white_level: int | None, headroom: int,
                       frame_crc32: str,
                       total_payload_bytes: int | None = None,
                       split: dict | None = None,
                       context: dict | None = None) -> None:
        """Build and write the sidecar; adds ``debug_metadata_path``."""
        document = build_debug_document(
            info=info, profile=self.profile, options=options, meta=meta,
            thumbnail_requested=thumbnail_requested,
            thumbnail_label=thumbnail_label, thumbnail_rgb=thumbnail_rgb,
            stegos=stegos, cover_seed=cover_seed,
            metadata_seed=metadata_seed, white_level=white_level,
            headroom=headroom, frame_crc32=frame_crc32,
            total_payload_bytes=total_payload_bytes, split=split,
            context=context,
        )
        info["debug_metadata_path"] = write_debug_metadata(
            output_path, document)

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
        debug_metadata: bool = False,
        debug_context: dict | None = None,
        image_time: _dt.datetime | None = None,
        gps_radius_km: float = geo.MAX_RADIUS_KM,
        location: geo.Location | None = None,
    ) -> dict:
        """Embed `payload` into a new DNG file. Returns info dict.

        ``frames`` full-resolution raw SubIFDs share the file (burst/stack
        style); the framed payload is striped across them in order, so
        capacity scales ~linearly with ``frames``. Each extra frame adds a
        full raster to the file size.

        ``debug_metadata`` writes a JSON sidecar beside the output (same
        base name, ``.json``; also reported as ``debug_metadata_path`` in
        the returned dict). ``debug_context`` is optional provenance
        (e.g. the CLI input path) merged into that document; never put
        secrets such as the passphrase in it.

        ``image_time`` pins the EXIF capture time (local wall clock) and
        the matching UTC offset instead of randomizing it; ``None`` keeps
        the default seeded random timestamp.

        ``gps_radius_km`` is how far (up to 25 km) the GPS fix may sit
        from the sampled city, and ``location`` reuses a point already
        drawn for another file (split sets share one).
        """
        self._validate_options(bit_depth, lsb_planes, frames, mode,
                               compression)
        requested_seed = seed
        metadata_seed = 0 if no_randomize else requested_seed
        if metadata_seed is None:
            # Unseeded run: draw a concrete seed so the debug sidecar can
            # record (and reproduce) the metadata randomization.
            metadata_seed = random.randrange(1 << 30)
        meta = MetadataRandomizer(
            metadata_seed, self.profile,
            gps_radius_km=gps_radius_km).randomize(
                image_time=image_time, location=location)
        if seed is None:
            seed = 0

        white = (self.profile.effective_white(bit_depth, self.level_policy)
                 if self.profile.fidelity is not None
                 and self.profile.fidelity.white_level is not None else None)
        headroom = ((1 << lsb_planes) - 1
                    if white is not None
                    and white < (1 << bit_depth) - 1 else 0)
        covers = [CoverGenerator(seed + i).cover(
            height, width, mode, bit_depth,
            white_level=white, headroom=headroom) for i in range(frames)]
        n_samples = covers[0].size
        cap = LsbCodec.capacity_bytes_total(n_samples, lsb_planes, frames)
        if len(payload) > cap:
            raise ValueError(
                f"payload {format_kb_hi(len(payload))} exceeds capacity {format_kb_lo(cap)} "
                f"({width}x{height} {mode} {bit_depth}-bit, "
                f"{lsb_planes} LSB plane(s)"
                f"{f' x {frames} frames' if frames > 1 else ''})"
            )
        frame = PayloadFrame.pack(payload, key)
        frame_crc = crc32_hex(frame) if debug_metadata else ""
        stegos = LsbCodec.stripe_frames(
            covers, frame, lsb_planes, progress=progress)
        # stripe_frames embeds in place: stegos share the covers'
        # buffers, so drop the extra references promptly.
        del covers, frame

        tw, th = self._thumbnail_size(width, height)
        thumb, thumb_label = ThumbnailProvider(seed=seed).get(
            tw, th, source=thumbnail)
        bigtiff = self._write_container(
            output_path, stegos=stegos, thumb_rgb=thumb, meta=meta,
            width=width, height=height, mode=mode, bit_depth=bit_depth,
            compression=compression, frames=frames, tw=tw, th=th,
            seed=0 if seed is None else seed,
        )
        info = self._file_info(
            output_path, width=width, height=height, mode=mode,
            bit_depth=bit_depth, container=str(stegos[0].dtype),
            lsb_planes=lsb_planes, frames=frames, thumb_label=thumb_label,
            bigtiff=bigtiff, cap=cap, payload_len=len(payload), meta=meta,
        )
        if debug_metadata:
            self._debug_sidecar(
                output_path, info,
                options=self._debug_options(
                    width=width, height=height, seed=requested_seed, key=key,
                    lsb_planes=lsb_planes, bit_depth=bit_depth, mode=mode,
                    compression=compression, no_randomize=no_randomize,
                    frames=frames, thumbnail=thumbnail,
                    image_time=image_time, gps_radius_km=gps_radius_km),
                meta=meta, thumbnail_requested=thumbnail,
                thumbnail_label=thumb_label, thumbnail_rgb=thumb,
                stegos=stegos, cover_seed=seed,
                metadata_seed=metadata_seed,
                white_level=white, headroom=headroom,
                frame_crc32=frame_crc, context=debug_context,
            )
        return info

    def _attach_makernote(self, meta: dict, seed: int) -> None:
        """Add the profile's opaque MakerNote blob to ``meta`` (if any)."""
        fidelity = self.profile.fidelity
        if fidelity is not None and fidelity.makernote is not None:
            meta["makernote"] = fidelity.makernote.generate(seed)

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
        if self.profile.fidelity is not None:
            max_planes = self.profile.effective_max_planes(
                bit_depth, self.level_policy)
            if lsb_planes > max_planes:
                policy = self.profile._policy(self.level_policy)
                hint = (" Use --level-policy capacity for the full 16 planes."
                        if policy == "strict" and max_planes < MAX_LSB_PLANES
                        else "")
                raise ValueError(
                    f"lsb_planes ({lsb_planes}) exceeds this profile's "
                    f"maximum of {max_planes} at {bit_depth}-bit under the "
                    f"{policy!r} level policy.{hint}")
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
        debug_metadata: bool = False,
        debug_context: dict | None = None,
        image_time: _dt.datetime | None = None,
        gps_radius_km: float = geo.MAX_RADIUS_KM,
    ) -> list[dict]:
        """Split `payload` into ≤`split_size`-byte chunks across DNG files.

        Each chunk is an independent framed payload (own header/CRC), so a
        short last chunk needs no padding. Files are named
        ``<stem>0001<suffix>`` … (DCF-style 4-digit sequences); chunk
        order/total travel in ``split_id_field`` (shared UUID) and
        ``split_seq_field`` (``"none"`` disables either). A payload
        fitting in one chunk yields a single plain file with no split
        markers at all. Returns one info dict per file.

        ``debug_metadata`` writes one JSON sidecar per chunk (see
        :meth:`encode`); each document records its own chunk number,
        chunk-set UUID and per-chunk metadata.

        ``image_time`` applies the same pinned capture time to every
        chunk, so a split set shares one timestamp.  ``gps_radius_km``
        widens or narrows the city disk; every chunk of a set shares one
        sampled location (coordinates and altitude), as a real set would.
        """
        if isinstance(split_size, bool) or not isinstance(split_size, int) \
                or split_size <= 0:
            raise ValueError(
                f"split_size must be a positive byte count (got {split_size!r})")
        self._validate_options(bit_depth, lsb_planes, frames, mode,
                               compression)
        geo.validate_radius(gps_radius_km)
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
        shared_location = None
        location_seed = None
        if (total > 1 and self.profile.fidelity is not None
                and self.profile.fidelity.emit_gps):
            # One draw for the whole set, independent of the per-chunk
            # seeds so every file carries the same coordinates.  An
            # unseeded run still needs a fresh location seed (Random(0)
            # would repeat the same city for every unrelated set), but
            # --no-randomize keeps the reference draw at seed 0.
            location_seed = seed if seed is not None else (
                0 if no_randomize else random.randrange(1 << 30))
            location_rng = random.Random(location_seed)
            if image_time is not None:
                local, offset = normalize_image_time(image_time)
                shared_location = geo.sample_location(
                    location_rng, gps_radius_km, local_time=local,
                    offset=offset)
            else:
                shared_location = geo.sample_location(
                    location_rng, gps_radius_km)
        if total == 1:
            # Fits in one chunk: plain single file, no split markers.
            return [self.encode(
                payload, output_path, width=width, height=height, seed=seed,
                key=key, lsb_planes=lsb_planes, bit_depth=bit_depth,
                mode=mode, compression=compression,
                no_randomize=no_randomize, frames=frames,
                thumbnail=thumbnail, progress=progress,
                debug_metadata=debug_metadata,
                debug_context=debug_context, image_time=image_time,
                gps_radius_km=gps_radius_km,
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
                if seed is None and not no_randomize:
                    # Unseeded run: fresh random base per chunk so chunks
                    # share neither cover pixels nor fallback thumbnails
                    # (identical high bits across chunks would be a tell).
                    cseed = random.randrange(1 << 30)
                else:
                    cseed = (0 if seed is None else seed) + seq - 1
                meta = MetadataRandomizer(
                    cseed, self.profile,
                    gps_radius_km=gps_radius_km).randomize(
                        image_time=image_time, location=shared_location)
                split_exif: dict[int, Any] = {}
                if id_spec is not None and id_spec["ifd"] == "exif":
                    split_exif[id_spec["tag"]] = uid
                if seq_spec is not None and seq_spec["ifd"] == "exif":
                    val: Any = format_seq_value(split_seq_field, seq, total)
                    split_exif[seq_spec["tag"]] = (
                        [val] if isinstance(val, int) else list(val))
                if split_exif:
                    meta["split_exif"] = split_exif
                cs = cseed
                white = (self.profile.effective_white(
                    bit_depth, self.level_policy)
                    if self.profile.fidelity is not None
                    and self.profile.fidelity.white_level is not None
                    else None)
                headroom = ((1 << lsb_planes) - 1
                            if white is not None
                            and white < (1 << bit_depth) - 1 else 0)
                covers = [CoverGenerator(cs + f).cover(
                    height, width, mode, bit_depth,
                    white_level=white, headroom=headroom)
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
                frame_crc = crc32_hex(frame) if debug_metadata else ""
                del chunk
                stegos = LsbCodec.stripe_frames(
                    covers, frame, lsb_planes, progress=show,
                    desc=f"Embedding chunk {seq}/{total}", position=1)
                # stripe_frames embeds in place: stegos share the covers'
                # buffers, so drop the extra references promptly.
                del covers, frame
                tw, th = self._thumbnail_size(width, height)
                thumb, thumb_label = ThumbnailProvider(seed=cs).get(
                    tw, th, source=thumbnail)
                bigtiff = self._write_container(
                    path, stegos=stegos, thumb_rgb=thumb, meta=meta,
                    width=width, height=height, mode=mode, bit_depth=bit_depth,
                    compression=compression, frames=frames, tw=tw, th=th,
                    ifd0_dummies=ifd0_dummies, seed=cs,
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
                if debug_metadata:
                    self._debug_sidecar(
                        path, info,
                        options=self._debug_options(
                            width=width, height=height, seed=seed, key=key,
                            lsb_planes=lsb_planes, bit_depth=bit_depth,
                            mode=mode, compression=compression,
                            no_randomize=no_randomize, frames=frames,
                            thumbnail=thumbnail, image_time=image_time,
                            gps_radius_km=gps_radius_km,
                            location_seed=location_seed),
                        meta=meta, thumbnail_requested=thumbnail,
                        thumbnail_label=thumb_label, thumbnail_rgb=thumb,
                        stegos=stegos, cover_seed=cs,
                        metadata_seed=cseed, white_level=white,
                        headroom=headroom, frame_crc32=frame_crc,
                        total_payload_bytes=len(payload),
                        split={"chunk_seq": seq, "chunk_total": total,
                               "split_id": uid,
                               "split_id_field": split_id_field,
                               "split_seq_field": split_seq_field},
                        context=debug_context,
                    )
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
                software=self.profile.software or False, metadata=None,
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
    profile=None,
    level_policy: str = "profile",
    debug_metadata: bool = False,
    debug_context: dict | None = None,
    image_time: _dt.datetime | None = None,
    gps_radius_km: float = geo.MAX_RADIUS_KM,
) -> dict:
    """Backwards-compatible wrapper (see :meth:`DngStego.encode`)."""
    stego = (_DEFAULT if profile is None
             else DngStego(profile, level_policy=level_policy))
    return stego.encode(
        payload, output_path, width=width, height=height, seed=seed,
        key=key, lsb_planes=lsb_planes, bit_depth=bit_depth, mode=mode,
        compression=compression, no_randomize=no_randomize, frames=frames,
        thumbnail=thumbnail, progress=progress,
        debug_metadata=debug_metadata, debug_context=debug_context,
        image_time=image_time, gps_radius_km=gps_radius_km,
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
    profile=None,
    level_policy: str = "profile",
    debug_metadata: bool = False,
    debug_context: dict | None = None,
    image_time: _dt.datetime | None = None,
    gps_radius_km: float = geo.MAX_RADIUS_KM,
) -> list[dict]:
    """Backwards-compatible wrapper (see :meth:`DngStego.encode_split`)."""
    stego = (_DEFAULT if profile is None
             else DngStego(profile, level_policy=level_policy))
    return stego.encode_split(
        payload, output_path, split_size, width=width, height=height,
        seed=seed, key=key, lsb_planes=lsb_planes, bit_depth=bit_depth,
        mode=mode, compression=compression, no_randomize=no_randomize,
        frames=frames, thumbnail=thumbnail, split_id=split_id,
        split_id_field=split_id_field, split_seq_field=split_seq_field,
        progress=progress, debug_metadata=debug_metadata,
        debug_context=debug_context, image_time=image_time,
        gps_radius_km=gps_radius_km)


def generate_tiff(
    output_path: str,
    width: int = 2048,
    height: int = 1536,
    seed: int | None = None,
) -> str:
    """Backwards-compatible wrapper (see :meth:`DngStego.generate_tiff`)."""
    return _DEFAULT.generate_tiff(
        output_path, width=width, height=height, seed=seed)
