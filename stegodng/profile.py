"""Camera/file-format profile: reference constants harvested from the
Fujifilm GFX 100 Pixel Shift Combiner samples in ``images/``.

Static calibration fields are copied verbatim from the reference files;
:class:`CameraProfile` derives per-depth values (white/black level,
container dtype, writable plane ceiling) from them.

Per-camera profiles live in :mod:`stegodng.profiles` (one directory per
camera, each with ``profile.json`` + ``README.md`` harvested from
``dpreview-raw`` samples). :attr:`DEFAULT_PROFILE` is the original GFX 100
combiner profile and stays byte-stable.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

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
    """Static reference values for one camera/cover story.

    The first block (make/model/software/calibration) is written verbatim
    into every output file. The second block (lenses/pools/geometry)
    drives :class:`MetadataRandomizer` and the ``--camera-profile``
    subprofile geometries; ``None`` pools fall back to the GFX reference
    pools so the default profile behaves exactly as before.
    """

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
    # -- per-camera overlay (registry profiles) -------------------------
    # CLI slug, e.g. "sony_ilce_7rm5" (+ "-native"/"-pixelshift" suffix).
    slug: str = "gfx_100"
    display_name: str = "Fujifilm GFX 100"
    # Native sensor geometry (decoded-RAW dimensions incl. masked margins).
    native_width: int | None = 11648
    native_height: int | None = 8736
    # Documented native bit depth / CFA layout (informational; encode
    # defaults stay 16-bit linear unless flags say otherwise).
    suggested_bit_depth: int = 16
    cfa_pattern: str | None = None
    crop_factor: float = 0.79  # GFX 0.79x; full-frame 1.0, APS-C ~1.5, MFT 2.0
    # Randomizer pools: None means "use the GFX reference pools".
    # lenses: ((model, min_mm, max_mm, max_aperture, lens_make), ...)
    lenses: tuple | None = None
    iso_choices: tuple | None = None
    # ((num, den), ...) exposure times
    exposure_choices: tuple | None = None
    # ((num, den), ...) f-numbers x100
    fnumber_choices: tuple | None = None
    metering_choices: tuple | None = None
    exposure_program_choices: tuple | None = None
    serial_prefixes: tuple = ("92A", "94A", "93A", "95A")
    # subprofile name -> (width, height); e.g. {"native": (...), ...}.
    subprofiles: dict = field(default_factory=lambda: {
        "native": (GFX_NATIVE_W, GFX_NATIVE_H),
        "pixelshift": (PIXELSHIFT_W, PIXELSHIFT_H),
    })
    # Where the calibration block came from: "reference-gfx-combiner",
    # "harvested-dng" or "exif-plus-fallback" (see per-profile README).
    calibration_source: str = "reference-gfx-combiner"

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

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CameraProfile":
        """Build a profile from a registry ``profile.json`` dict.

        Missing calibration keys fall back to the GFX reference values
        (documented per profile via ``calibration_source``).
        """
        ref = cls()

        def _or(key: str, default: Any) -> Any:
            value = data.get(key, default)
            return default if value is None else value
        matrix1 = data.get("color_matrix1")
        matrix2 = data.get("color_matrix2")
        opcode_hex = data.get("opcode_list3_hex")
        subprofiles = data.get("subprofiles") or {}
        if not isinstance(subprofiles, dict):
            raise ValueError("subprofiles must be a dict")
        subs: dict[str, tuple[int, int]] = {}
        for name, geom in subprofiles.items():
            if not isinstance(geom, dict):
                raise ValueError(
                    f"subprofile {name!r} must be a dict")
            try:
                w, h = int(geom["width"]), int(geom["height"])
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(
                    f"subprofile {name!r} needs int width/height") from exc
            if w <= 0 or h <= 0:
                raise ValueError(
                    f"subprofile {name!r} needs positive width/height")
            subs[name] = (w, h)
        return cls(
            make=data.get("make", ref.make),
            model=data.get("model", ref.model),
            unique_camera_model=data.get(
                "unique_camera_model", data.get("model", ref.model)),
            software=data.get("software", ref.software),
            dng_version=bytes(data["dng_version"])
            if data.get("dng_version") else ref.dng_version,
            dng_backward=bytes(data["dng_backward"])
            if data.get("dng_backward") else ref.dng_backward,
            color_matrix1=[tuple(p) for p in matrix1]
            if matrix1 else list(ref.color_matrix1),
            color_matrix2=[tuple(p) for p in matrix2]
            if matrix2 else list(ref.color_matrix2),
            calib_illuminant1=_or("calib_illuminant1",
                                   ref.calib_illuminant1),
            calib_illuminant2=_or("calib_illuminant2",
                                   ref.calib_illuminant2),
            baseline_noise=tuple(data["baseline_noise"])
            if data.get("baseline_noise") else ref.baseline_noise,
            baseline_sharpness=tuple(data["baseline_sharpness"])
            if data.get("baseline_sharpness") else ref.baseline_sharpness,
            linear_response_limit=tuple(data["linear_response_limit"])
            if data.get("linear_response_limit")
            else ref.linear_response_limit,
            shadow_scale=tuple(data["shadow_scale"])
            if data.get("shadow_scale") else ref.shadow_scale,
            black_level_ref=_or("black_level_ref", ref.black_level_ref),
            opcode_list3=bytes.fromhex(opcode_hex)
            if opcode_hex else ref.opcode_list3,
            slug=data.get("slug", ""),
            display_name=data.get("display_name", ""),
            native_width=data.get("native_width"),
            native_height=data.get("native_height"),
            suggested_bit_depth=_or("suggested_bit_depth", 16),
            cfa_pattern=data.get("cfa_pattern"),
            crop_factor=_or("crop_factor", ref.crop_factor),
            lenses=tuple(tuple(l) for l in data["lenses"])
            if data.get("lenses") else None,
            iso_choices=tuple(data["iso_choices"])
            if data.get("iso_choices") else None,
            exposure_choices=tuple(tuple(e) for e in data["exposure_choices"])
            if data.get("exposure_choices") else None,
            fnumber_choices=tuple(tuple(f) for f in data["fnumber_choices"])
            if data.get("fnumber_choices") else None,
            metering_choices=tuple(data["metering_choices"])
            if data.get("metering_choices") else None,
            exposure_program_choices=tuple(data["exposure_program_choices"])
            if data.get("exposure_program_choices") else None,
            serial_prefixes=tuple(data["serial_prefixes"])
            if data.get("serial_prefixes") else ref.serial_prefixes,
            subprofiles=subs,
            calibration_source=data.get("calibration_source", ""),
        )


DEFAULT_PROFILE = CameraProfile()
