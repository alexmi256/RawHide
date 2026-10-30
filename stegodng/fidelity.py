"""Optional per-profile metadata fidelity settings.

Everything here is opt-in through a ``fidelity`` block in
``profile.json``.  Absent fields keep the historical writer behaviour, so
the GFX reference output stays byte-identical and harvested profiles are
unchanged until they add the block.
"""
from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .makernote import MakernoteConfig

# Tag-set conventions seen in files re-wrapped by Adobe software.  They
# are opt-in because they change the tag inventory of the written file.
TAG_CONVENTIONS = ("adobe",)


def _pair(value: Any, name: str, *, positive: bool = False) -> tuple[int, int]:
    if (not isinstance(value, (list, tuple)) or len(value) != 2):
        raise ValueError(f"{name} must be a two-item list")
    a, b = int(value[0]), int(value[1])
    if positive and (a <= 0 or b <= 0):
        raise ValueError(f"{name} values must be positive")
    return (a, b)


def _ranges(value: Any, name: str, *, count: int = 2) -> tuple[int, ...]:
    if not isinstance(value, (list, tuple)) or len(value) != count:
        raise ValueError(f"{name} must have {count} values")
    return tuple(int(v) for v in value)


def _int_pair(value: Any, name: str) -> tuple[int, int]:
    """Two-item integer list/tuple (typed as a pair for the dataclass)."""
    low, high = _ranges(value, name)
    return (low, high)


def _floats(value: Any, name: str, *, count: int = 2) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)) or len(value) != count:
        raise ValueError(f"{name} must have {count} values")
    return tuple(float(v) for v in value)


def _float_pair(value: Any, name: str) -> tuple[float, float]:
    """Two-item float list/tuple (typed as a pair for the dataclass)."""
    low, high = _floats(value, name)
    return (low, high)


def _rationals(value: Any, name: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(value, (list, tuple)) or not value:
        raise ValueError(f"{name} must be a non-empty list")
    out = []
    for item in value:
        n, d = _pair(item, name)
        if d <= 0:
            raise ValueError(f"{name} denominators must be positive")
        out.append((n, d))
    return tuple(out)


def _matrix(value: Any, name: str) -> tuple[tuple[int, int], ...]:
    rats = _rationals(value, name)
    if len(rats) != 9:
        raise ValueError(f"{name} needs nine rationals")
    return rats


def _asset(value: Any, base_dir: str | Path | None, name: str) -> bytes:
    if base_dir is None:
        raise ValueError(f"{name} needs a profile directory to load")
    path = Path(base_dir) / str(value)
    try:
        return path.read_bytes()
    except OSError as exc:
        raise ValueError(f"cannot read {name} asset {path}") from exc


@dataclass(frozen=True)
class AdobeProfile:
    """Small Adobe camera-profile tags (the large lookup blobs are later)."""

    forward_matrix1: tuple[tuple[int, int], ...] | None = None
    forward_matrix2: tuple[tuple[int, int], ...] | None = None
    name: str | None = None
    calibration_signature: str | None = None
    copyright: str | None = None
    embed_policy: int | None = None
    hue_sat_map_dims: tuple[int, int, int] | None = None
    hue_sat_map_data1: bytes | None = None
    hue_sat_map_data2: bytes | None = None
    look_table_dims: tuple[int, int, int] | None = None
    look_table_data: bytes | None = None


@dataclass(frozen=True)
class FidelityConfig:
    """Optional fidelity knobs shared by every camera profile."""

    # Presentation / per-file metadata
    preview_size: tuple[int, int] | None = None
    orientations: tuple[int, ...] = ()
    software_variants: tuple[str, ...] = ()
    date_range: tuple[str, str] | None = None
    date_window_days: int | None = None
    suggested_mode: str | None = None
    asn_r: tuple[int, int] | None = None
    asn_b: tuple[int, int] | None = None
    baseline_exposure: tuple[int, int] | None = None  # EV * 10000
    subject_distance: tuple[tuple[int, int], ...] = ()
    subject_distance_range: tuple[int, ...] = ()
    exposure_bias: tuple[int, ...] = ()
    flash: int | None = None

    # Tag presence
    emit_xmp: bool = True
    emit_lens: bool = True
    emit_serials: bool = True
    emit_gps: bool = False
    exif_allow: tuple[int, ...] | None = None
    tag_conventions: str | None = None   # "adobe" -> Adobe writer tag set
    raw_digests: bool = False            # NewRawImageDigest + RawDataUniqueID
    makernote: MakernoteConfig | None = None
    subsec_digits: int = 2               # EXIF SubSecTime fractional digits

    # Raw IFD
    tile: tuple[int, int] | None = None
    black_levels: tuple[tuple[int, int], ...] | None = None
    white_level: int | None = None
    max_planes: int | None = None
    level_policy: str = "capacity"  # "strict" | "capacity"
    crop_margin: tuple[int, int] | None = None
    bayer_green_split: int | None = None
    sensor_sizes: tuple[tuple[int, int], ...] = ()
    prefer_native: bool = False
    noise_s: tuple[float, float] | None = None
    noise_o: tuple[float, float] | None = None

    adobe: AdobeProfile | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any],
                  base_dir: str | Path | None = None) -> "FidelityConfig":
        if not isinstance(data, dict):
            raise ValueError("fidelity must be a dict")
        preview = data.get("preview")
        preview_size = None
        if preview is not None:
            if not isinstance(preview, dict):
                raise ValueError("fidelity.preview must be a dict")
            preview_size = _pair(preview.get("size"), "preview.size",
                                 positive=True)
        orientations = tuple(int(v) for v in data.get("orientation", ()))
        if any(v < 1 or v > 8 for v in orientations):
            raise ValueError("orientation values must be 1..8")
        variants = tuple(str(v) for v in data.get("software_variants", ()))
        date_range = data.get("date_range")
        if date_range is not None:
            if (not isinstance(date_range, (list, tuple))
                    or len(date_range) != 2):
                raise ValueError("date_range must be [start, end]")
            for item in date_range:
                try:
                    _dt.date.fromisoformat(str(item))
                except ValueError as exc:
                    raise ValueError(
                        f"date_range values must be YYYY-MM-DD: {item!r}") from exc
        window = (int(data["date_window_days"])
                  if data.get("date_window_days") is not None else None)
        if window is not None and not (1 <= window <= 3650):
            raise ValueError("date_window_days must be 1..3650")
        suggested_mode = data.get("suggested_mode")
        if suggested_mode is not None and suggested_mode not in ("linear", "cfa"):
            raise ValueError("suggested_mode must be linear or cfa")
        asn = data.get("as_shot_neutral") or {}
        asn_r = (_int_pair(asn["r"], "as_shot_neutral.r")
                 if asn.get("r") else None)
        asn_b = (_int_pair(asn["b"], "as_shot_neutral.b")
                 if asn.get("b") else None)
        for name, pair in (("as_shot_neutral.r", asn_r),
                           ("as_shot_neutral.b", asn_b)):
            if pair and not (0 < pair[0] <= pair[1] <= 10000):
                raise ValueError(f"{name} must be 0 < low <= high <= 10000")
        baseline = data.get("baseline_exposure")
        baseline_pair = (_int_pair(baseline, "baseline_exposure")
                         if baseline is not None else None)
        if baseline_pair and not (-10000 <= baseline_pair[0]
                                  <= baseline_pair[1] <= 10000):
            raise ValueError("baseline_exposure must be within -1..+1 EV")

        subject = data.get("subject_distance") or {}
        subject_dist = (_rationals(subject.get("choices"),
                                   "subject_distance.choices")
                        if subject.get("choices") else ())
        subject_range = (tuple(int(v) for v in subject.get("range", ()))
                         if subject.get("range") else ())

        tags = data.get("tags") or {}
        emit = {
            "emit_xmp": bool(tags.get("xmp", True)),
            "emit_lens": bool(tags.get("lens", True)),
            "emit_serials": bool(tags.get("serials", True)),
            "emit_gps": bool(tags.get("gps", False)),
        }
        allow = tags.get("exif_allow")
        exif_allow = (tuple(int(v) for v in allow)
                      if allow is not None else None)
        exposure_bias = tuple(int(v) for v in tags.get("exposure_bias", ()))
        flash = int(tags["flash"]) if tags.get("flash") is not None else None

        conventions = data.get("tag_conventions")
        if conventions is not None and conventions not in TAG_CONVENTIONS:
            raise ValueError(
                f"tag_conventions must be one of {TAG_CONVENTIONS}")
        raw_digests = bool(data.get("raw_digests", False))
        makernote_data = data.get("makernote")
        makernote = (MakernoteConfig.from_dict(makernote_data)
                     if makernote_data else None)
        subsec_digits = data.get("subsec_digits")
        if subsec_digits is None:
            # Adobe/re-wrapped files keep the full EXIF sub-second
            # fraction (6 digits); the legacy writer used 2.
            subsec_digits = 6 if conventions == "adobe" else 2
        subsec_digits = int(subsec_digits)
        if not (1 <= subsec_digits <= 9):
            raise ValueError("subsec_digits must be 1..9")

        raw = data.get("raw") or {}
        tile = _pair(raw.get("tile"), "raw.tile", positive=True) \
            if raw.get("tile") else None
        black = (_rationals(raw.get("black_levels"), "raw.black_levels")
                 if raw.get("black_levels") else None)
        if black is not None and len(black) not in (1, 3, 4):
            raise ValueError("raw.black_levels needs 1, 3 or 4 values")
        white = (int(raw["white_level"])
                 if raw.get("white_level") is not None else None)
        if white is not None and not (1 <= white <= 65535):
            raise ValueError("raw.white_level must be 1..65535")
        max_planes = (int(raw["max_planes"])
                      if raw.get("max_planes") is not None else None)
        if max_planes is not None and not (1 <= max_planes <= 16):
            raise ValueError("raw.max_planes must be 1..16")
        policy = str(raw.get("level_policy", "capacity")).lower()
        if policy not in ("strict", "capacity"):
            raise ValueError("raw.level_policy must be strict or capacity")
        margin = (_pair(raw.get("crop_margin"), "raw.crop_margin")
                  if raw.get("crop_margin") else None)
        if margin is not None and (margin[0] < 0 or margin[1] < 0):
            raise ValueError("raw.crop_margin must be non-negative")
        green = (int(raw["bayer_green_split"])
                 if raw.get("bayer_green_split") is not None else None)
        geom = data.get("geometry") or {}
        sensor_sizes = tuple(
            _pair(v, "geometry.sensor_sizes", positive=True)
            for v in geom.get("sensor_sizes", ()))
        prefer = bool(geom.get("prefer_native", False))

        noise = data.get("noise") or {}
        noise_s = (_float_pair(noise["s"], "noise.s")
                   if noise.get("s") else None)
        noise_o = (_float_pair(noise["o"], "noise.o")
                   if noise.get("o") else None)
        for name, pair in (("noise.s", noise_s), ("noise.o", noise_o)):
            if pair and not (0 < pair[0] <= pair[1]):
                raise ValueError(f"{name} must be 0 < low <= high")

        adobe_data = data.get("adobe")
        adobe = None
        if adobe_data:
            if not isinstance(adobe_data, dict):
                raise ValueError("fidelity.adobe must be a dict")
            hue_dims = (tuple(int(v) for v in adobe_data["hue_sat_map_dims"])
                        if adobe_data.get("hue_sat_map_dims") else None)
            look_dims = (tuple(int(v) for v in adobe_data["look_table_dims"])
                         if adobe_data.get("look_table_dims") else None)
            if hue_dims is not None and len(hue_dims) != 3:
                raise ValueError("adobe.hue_sat_map_dims needs three values")
            if look_dims is not None and len(look_dims) != 3:
                raise ValueError("adobe.look_table_dims needs three values")
            adobe = AdobeProfile(
                forward_matrix1=_matrix(adobe_data["forward_matrix1"],
                                        "adobe.forward_matrix1")
                if adobe_data.get("forward_matrix1") else None,
                forward_matrix2=_matrix(adobe_data["forward_matrix2"],
                                        "adobe.forward_matrix2")
                if adobe_data.get("forward_matrix2") else None,
                name=adobe_data.get("name"),
                calibration_signature=adobe_data.get("calibration_signature"),
                copyright=adobe_data.get("copyright"),
                embed_policy=adobe_data.get("embed_policy"),
                hue_sat_map_dims=hue_dims,
                hue_sat_map_data1=_asset(adobe_data["hue_sat_map_data1"],
                                         base_dir, "adobe.hue_sat_map_data1")
                if adobe_data.get("hue_sat_map_data1") else None,
                hue_sat_map_data2=_asset(adobe_data["hue_sat_map_data2"],
                                         base_dir, "adobe.hue_sat_map_data2")
                if adobe_data.get("hue_sat_map_data2") else None,
                look_table_dims=look_dims,
                look_table_data=_asset(adobe_data["look_table_data"],
                                       base_dir, "adobe.look_table_data")
                if adobe_data.get("look_table_data") else None,
            )
            for label, dims, blob in (
                    ("hue_sat_map_data1", adobe.hue_sat_map_dims,
                     adobe.hue_sat_map_data1),
                    ("hue_sat_map_data2", adobe.hue_sat_map_dims,
                     adobe.hue_sat_map_data2),
                    ("look_table_data", adobe.look_table_dims,
                     adobe.look_table_data)):
                if dims is None or blob is None:
                    continue
                expected = dims[0] * dims[1] * dims[2] * 3 * 4
                if len(blob) != expected:
                    raise ValueError(
                        f"adobe.{label} is {len(blob)} bytes, expected "
                        f"{expected} for dims {dims}")

        return cls(
            preview_size=preview_size,
            orientations=orientations,
            software_variants=variants,
            date_range=((str(date_range[0]), str(date_range[1]))
                        if date_range else None),
            date_window_days=window,
            suggested_mode=suggested_mode,
            asn_r=asn_r, asn_b=asn_b,
            baseline_exposure=baseline_pair,
            subject_distance=subject_dist,
            subject_distance_range=subject_range,
            exposure_bias=exposure_bias,
            flash=flash,
            exif_allow=exif_allow,
            tag_conventions=conventions,
            raw_digests=raw_digests,
            makernote=makernote,
            subsec_digits=subsec_digits,
            tile=tile, black_levels=black, white_level=white,
            max_planes=max_planes, level_policy=policy,
            crop_margin=margin, bayer_green_split=green,
            sensor_sizes=sensor_sizes, prefer_native=prefer,
            noise_s=noise_s, noise_o=noise_o,
            adobe=adobe,
            **emit,
        )

    # -- convenience ----------------------------------------------------
    def date_bounds(self) -> tuple[_dt.datetime, _dt.datetime] | None:
        if self.date_window_days:
            end = _dt.datetime.now()
            return end - _dt.timedelta(days=self.date_window_days), end
        if not self.date_range:
            return None
        start = _dt.datetime.fromisoformat(self.date_range[0])
        end = (_dt.datetime.fromisoformat(self.date_range[1])
               + _dt.timedelta(days=1, seconds=-1))
        return start, end
