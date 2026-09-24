#!/usr/bin/env python3
from __future__ import annotations

"""RAW DNG image steganography (backwards-compatibility shim).

The implementation now lives in the :mod:`stegodng` package; this module
re-exports the original single-file API so existing code and command
lines keep working unchanged::

    python stego_dng.py encode -i secret.bin -o out.dng
    python stego_dng.py decode -i out.dng -o recovered.bin

New code should import from the package instead::

    from stegodng import DngStego, AutoSizer
"""
import argparse
import binascii
import datetime as _dt
import hashlib
import math
import os
import random
import struct
import sys
import zlib

import numpy as np
import tifffile

from stegodng.cli import main
from stegodng.codec import (
    LsbCodec,
    _embed_bitarray,
    _extract_bitarray,
    _kb,
    _kb_hi,
    _kb_lo,
    capacity_bytes,
    capacity_bytes_total,
    embed_bits,
    extract_bits,
    format_kb,
    format_kb_hi,
    format_kb_lo,
)
from stegodng.container import (
    _TYPE_SIZE,
    _append_exif,
    _build_exif_block,
    _DTYPE_NUM,
    _entry_value_ptr,
    _EXIF_TAGS,
    _exif_values,
    _find_ifd_entry,
    _ifd0_offset,
    _pack_val,
    _patch_linear_raw,
    _raw_series,
    _raw_series_all,
    _subifd_offsets,
    _tiff_is_bigtiff,
    build_exif_block,
    build_xmp,
    DngContainer,
    XMP_LEN,
)
from stegodng.cover import CoverGenerator, make_cover, make_thumbnail
from stegodng.framing import PayloadFrame
from stegodng.metadata import (
    EXPPROG_CHOICES,
    EXPOSURE_CHOICES,
    FNUMBER_CHOICES,
    ISO_CHOICES,
    LENSES,
    METERING_CHOICES,
    MetadataRandomizer,
    randomize_metadata,
)
from stegodng.profile import (
    AUTO_MIN_H,
    AUTO_MIN_W,
    DEFAULT_PROFILE,
    GFX_NATIVE_H,
    GFX_NATIVE_W,
    MAX_FRAMES,
    MAX_LSB_PLANES,
    PIXELSHIFT_H,
    PIXELSHIFT_W,
    PRESET_GEOMETRIES,
    SUPPORTED_BIT_DEPTHS,
    CameraProfile,
)
from stegodng.sizing import (
    _max_config_str,
    _risk_warnings,
    _top_planes,
    AutoSizer,
    recommend,
    recommend_config,
    risk_warnings,
)
from stegodng.split import (
    SPLIT_ID_FIELDS,
    SPLIT_SEQ_FIELDS,
    chunk_path,
    format_seq_value,
    new_split_id,
    parse_chunk_name,
    parse_seq_value,
    parse_size,
    resolve_split_fields,
)
from stegodng.stego import (
    DngStego,
    decode,
    encode,
    encode_split,
    generate_tiff,
)
from stegodng.thumbnails import ThumbnailError, ThumbnailProvider, prepare

# Framing constants (original module-level names).
MAGIC = PayloadFrame.MAGIC
VERSION = PayloadFrame.VERSION
HEADER_LEN = PayloadFrame.HEADER_LEN
FLAG_KEYED = PayloadFrame.FLAG_KEYED


def pack_frame(payload: bytes, lsb_planes: int, key: bytes | None) -> bytes:
    """Original signature (``lsb_planes`` is vestigial, kept for compat)."""
    return PayloadFrame.pack(payload, key)


def unpack_frame(stream: bytes, lsb_planes: int,
                 key: bytes | None) -> tuple[bytes, int]:
    """Original signature (``lsb_planes`` is vestigial, kept for compat)."""
    return PayloadFrame.unpack(stream, key)


def _keystream(key: bytes, length: int) -> bytes:
    return PayloadFrame._keystream(key, length)


def _rand_serial(rng, prefix: str = "") -> str:
    return MetadataRandomizer._rand_serial(rng, prefix)


def _decode_with_planes(raw, key: bytes | None, lsb_planes: int,
                        max_bytes: int) -> bytes:
    """Original single-frame signature; the class takes frame lists."""
    return DngStego._decode_with_planes([raw], key, lsb_planes, max_bytes)


# Reference profile as a plain dict (original ``STATIC`` shape).
_STATIC_PROFILE = DEFAULT_PROFILE
STATIC = {
    "make": _STATIC_PROFILE.make,
    "model": _STATIC_PROFILE.model,
    "unique_camera_model": _STATIC_PROFILE.unique_camera_model,
    "software": _STATIC_PROFILE.software,
    "dng_version": _STATIC_PROFILE.dng_version,
    "dng_backward": _STATIC_PROFILE.dng_backward,
    "color_matrix1": _STATIC_PROFILE.color_matrix1,
    "color_matrix2": _STATIC_PROFILE.color_matrix2,
    "calib_illuminant1": _STATIC_PROFILE.calib_illuminant1,
    "calib_illuminant2": _STATIC_PROFILE.calib_illuminant2,
    "baseline_noise": _STATIC_PROFILE.baseline_noise,
    "baseline_sharpness": _STATIC_PROFILE.baseline_sharpness,
    "linear_response_limit": _STATIC_PROFILE.linear_response_limit,
    "shadow_scale": _STATIC_PROFILE.shadow_scale,
    "black_level_ref": _STATIC_PROFILE.black_level_ref,
    "opcode_list3": _STATIC_PROFILE.opcode_list3,
}

if __name__ == "__main__":
    raise SystemExit(main())
