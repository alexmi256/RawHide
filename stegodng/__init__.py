"""RAW DNG image steganography.

Primary API::

    from stegodng import DngStego, AutoSizer

    stego = DngStego()
    info = stego.encode(b"secret", "out.dng")          # auto-sized
    payload = stego.decode("out.dng")

    sizer = AutoSizer()
    cfg = sizer.recommend(len(b"secret"))

The legacy ``stego_dng`` module remains as a thin compatibility shim.
"""
from .cli import main
from .codec import (
    LsbCodec,
    capacity_bytes,
    capacity_bytes_total,
    embed_bits,
    extract_bits,
    format_kb,
    format_kb_hi,
    format_kb_lo,
)
from .container import DngContainer, build_exif_block, build_xmp
from .cover import CoverGenerator, make_cover, make_thumbnail
from .framing import PayloadFrame
from .metadata import MetadataRandomizer, randomize_metadata
from .profile import (
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
from .sizing import AutoSizer, recommend, recommend_config, risk_warnings
from .split import (
    SPLIT_ID_FIELDS,
    SPLIT_SEQ_FIELDS,
    chunk_path,
    new_split_id,
    parse_chunk_name,
    parse_size,
)
from .stego import DngStego, decode, encode, encode_split, generate_tiff
from .thumbnails import ThumbnailError, ThumbnailProvider, prepare

__version__ = "1.0.0"

__all__ = [
    "AutoSizer",
    "CameraProfile",
    "CoverGenerator",
    "DEFAULT_PROFILE",
    "DngContainer",
    "DngStego",
    "LsbCodec",
    "PayloadFrame",
    "MetadataRandomizer",
    "build_exif_block",
    "build_xmp",
    "capacity_bytes",
    "capacity_bytes_total",
    "decode",
    "embed_bits",
    "encode",
    "encode_split",
    "extract_bits",
    "format_kb",
    "format_kb_hi",
    "format_kb_lo",
    "generate_tiff",
    "make_cover",
    "make_thumbnail",
    "SPLIT_ID_FIELDS",
    "SPLIT_SEQ_FIELDS",
    "chunk_path",
    "new_split_id",
    "parse_chunk_name",
    "parse_size",
    "randomize_metadata",
    "recommend",
    "recommend_config",
    "risk_warnings",
    "ThumbnailError",
    "ThumbnailProvider",
    "prepare",
    "main",
    "AUTO_MIN_H",
    "AUTO_MIN_W",
    "GFX_NATIVE_H",
    "GFX_NATIVE_W",
    "MAX_FRAMES",
    "MAX_LSB_PLANES",
    "PIXELSHIFT_H",
    "PIXELSHIFT_W",
    "PRESET_GEOMETRIES",
    "SUPPORTED_BIT_DEPTHS",
]
