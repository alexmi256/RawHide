"""Camera/file-format profile: reference constants harvested from the
Fujifilm GFX 100 Pixel Shift Combiner samples in ``images/``.

Static calibration fields are copied verbatim from the reference files;
:class:`CameraProfile` derives per-depth values (white/black level,
container dtype, writable plane ceiling) from them.
"""
from __future__ import annotations

from dataclasses import dataclass, field

MAX_LSB_PLANES = 16
# Frames (full-resolution raw SubIFDs sharing one file, burst/stack style).
MAX_FRAMES = 8
# Integer sample depths with real TIFF/DNG BitsPerSample support.
# 8 -> uint8 container; 10/12/14/16 -> uint16 container with packed
# BitsPerSample (tifffile packs the low N bits losslessly).
# 24/32-bit integer is NOT offered: LibRaw cannot open such DNGs
# (verified: LibRawFileUnsupportedError), so files would fail the
# "opens in a real RAW decoder" check. 32-bit float (DNG 1.4 HDR) is
# rawpy-readable but needs a separate mantissa-bit codec (future work).
SUPPORTED_BIT_DEPTHS = (8, 10, 12, 14, 16)

GFX_NATIVE_W, GFX_NATIVE_H = 11648, 8736      # GFX 100 II ~102 MP
PIXELSHIFT_W, PIXELSHIFT_H = 23296, 17472     # combiner output ~407 MP

# Candidate geometries for auto-sizing, smallest first. The first two are
# cheap demo/combiner-thumbnail scales; the last two match real GFX 100 II
# output (native sensor, Pixel Shift Combiner).
PRESET_GEOMETRIES: list[tuple[int, int, str]] = [
    (2048, 1536, "demo"),
    (4000, 3000, "combiner-scale"),
    (GFX_NATIVE_W, GFX_NATIVE_H, "gfx-native"),
    (PIXELSHIFT_W, PIXELSHIFT_H, "pixelshift"),
]

# Floor for --auto-size dimensions: JPEG-MCU-friendly, even (Bayer-safe),
# and far above the smallest sizes verified with the writer.
AUTO_MIN_W, AUTO_MIN_H = 64, 48


@dataclass(frozen=True)
class CameraProfile:
    """Static reference values for one camera/cover story."""

    make: str = "FUJIFILM"
    model: str = "GFX 100"  # combiner output identifies as GFX 100
    unique_camera_model: str = "GFX 100"
    software: str = "FUJIFILM Pixel Shift Combiner"
    dng_version: bytes = b"\x01\x04\x00\x00"
    dng_backward: bytes = b"\x01\x01\x00\x00"
    color_matrix1: list = field(default_factory=lambda: [
        (17191, 10000), (-11000, 10000), (1278, 10000),
        (-3574, 10000), (11733, 10000), (2076, 10000),
        (-2, 10000), (497, 10000), (6540, 10000),
    ])
    color_matrix2: list = field(default_factory=lambda: [
        (16212, 10000), (-8423, 10000), (-1583, 10000),
        (-4336, 10000), (12583, 10000), (1937, 10000),
        (-195, 10000), (726, 10000), (6199, 10000),
    ])
    calib_illuminant1: int = 17  # Standard light A
    calib_illuminant2: int = 21  # D65
    baseline_noise: tuple = (10000, 10000)
    baseline_sharpness: tuple = (13300, 10000)
    linear_response_limit: tuple = (10000, 10000)
    shadow_scale: tuple = (10000, 10000)
    # Combiner reference BlackLevel (256 @ 16-bit); scaled per depth.
    black_level_ref: int = 256
    # 256-byte OpcodeList3 copied verbatim from DSF0350.DNG (warp/gain ops
    # written by the combiner; static per camera generation).
    opcode_list3: bytes = bytes.fromhex(
        "00000002000000010103000000000001000000a4000000033fefefa6115f8d8b"
        "bd475000000000003d41000000000000bd3dc000000000000000000000000000"
        "00000000000000003fefefa6115f8d8bbd475000000000003d41000000000000"
        "bd3dc00000000000000000000000000000000000000000003fefefa6115f8d8b"
        "bd475000000000003d41000000000000bd3dc000000000000000000000000000"
        "00000000000000003fe00000000000003fe00000000000000000000301030000"
        "00000001000000383fad0f10239baaa43fb463dcfc19bda0bfd51fa03a2241f0"
        "3fdbc76f7c9e4ad0bfc809334b6932d03fe00000000000003fe0000000000000"
    )

    def white_level(self, bit_depth: int) -> int:
        return (1 << bit_depth) - 1

    def black_level(self, bit_depth: int) -> int:
        peak = self.white_level(bit_depth)
        return max(1, round(self.black_level_ref * peak / 65535))

    @staticmethod
    def container_bits(bit_depth: int) -> int:
        """Storage width: 8-bit fits uint8, everything else uses uint16."""
        return 8 if bit_depth <= 8 else 16

    def top_planes(self, bit_depth: int) -> int:
        """Highest writable plane count: full-range uint16 takes 16, packed
        depths are capped by their declared WhiteLevel (payload values must
        stay below 2**bit_depth)."""
        return min(MAX_LSB_PLANES, bit_depth)


DEFAULT_PROFILE = CameraProfile()
