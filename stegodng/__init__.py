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
from .profiles import get_profile, list_profiles
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
from .container import (
    DngContainer,
    build_exif_block,
    build_xmp,
    read_exif_tags,
    read_gps,
    read_ifd,
)
from .cover import CoverGenerator, make_cover, make_thumbnail
from .digests import (
    new_raw_image_digest,
    opcode_list_fingerprint,
    raw_data_unique_id,
)
from .fidelity import AdobeProfile, FidelityConfig
from .framing import PayloadFrame
from .makernote import MakernoteConfig
from .opcodes import (
    GainMap,
    GainMapConfig,
    build_opcode_list2,
    parse_opcode_list2,
    validate_opcode_list2,
)
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
    split_album_dir,
    split_album_output,
)
from .stego import DngStego, decode, encode, encode_split, generate_tiff
from .thumbnails import ThumbnailError, ThumbnailProvider, prepare

__version__ = "1.0.0"

__all__ = [
    "AdobeProfile",
    "AutoSizer",
    "CameraProfile",
    "CoverGenerator",
    "DEFAULT_PROFILE",
    "DngContainer",
    "DngStego",
    "FidelityConfig",
    "GainMap",
    "GainMapConfig",
    "LsbCodec",
    "MakernoteConfig",
    "PayloadFrame",
    "MetadataRandomizer",
    "build_exif_block",
    "build_opcode_list2",
    "build_xmp",
    "new_raw_image_digest",
    "opcode_list_fingerprint",
    "parse_opcode_list2",
    "raw_data_unique_id",
    "read_exif_tags",
    "read_gps",
    "read_ifd",
    "validate_opcode_list2",
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
    "get_profile",
    "list_profiles",
    "make_cover",
    "make_thumbnail",
    "SPLIT_ID_FIELDS",
    "SPLIT_SEQ_FIELDS",
    "chunk_path",
    "new_split_id",
    "parse_chunk_name",
    "parse_size",
    "split_album_dir",
    "split_album_output",
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
