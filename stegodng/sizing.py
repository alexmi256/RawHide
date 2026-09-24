"""Automatic configuration: pick the smallest fitting geometry.

:func:`recommend_config` (and :meth:`AutoSizer.recommend`) walk preset
geometries -- or compute an exact-fit frame with ``auto_size`` -- choosing
the fewest LSB planes (and user-fixed ``frames``) that hold the payload.
Sizes in errors are reported in kilobytes.
"""
from __future__ import annotations

import math

from .codec import (
    capacity_bytes,
    capacity_bytes_total,
    format_kb as _kb,
    format_kb_hi as _kb_hi,
    format_kb_lo as _kb_lo,
)
from .framing import PayloadFrame
from .profile import (
    AUTO_MIN_H,
    AUTO_MIN_W,
    GFX_NATIVE_H,
    GFX_NATIVE_W,
    MAX_FRAMES,
    MAX_LSB_PLANES,
    PIXELSHIFT_H,
    PIXELSHIFT_W,
    PRESET_GEOMETRIES,
    SUPPORTED_BIT_DEPTHS,
)

HEADER_LEN = PayloadFrame.HEADER_LEN


def _top_planes(bit_depth: int) -> int:
    """Highest writable plane count: full-range uint16 takes 16, packed
    depths are capped by their declared WhiteLevel (payload values must
    stay below 2**bit_depth)."""
    return min(MAX_LSB_PLANES, bit_depth)


def _max_config_str(mode: str, bit_depth: int, frames: int = 1) -> str:
    s = (f"{PIXELSHIFT_W}x{PIXELSHIFT_H} {mode} {bit_depth}-bit, "
         f"{_top_planes(bit_depth)} LSB planes")
    return s + (f" x {frames} frames" if frames > 1 else "")


# Floor for --auto-size dimensions: JPEG-MCU-friendly, even (Bayer-safe),
# and far above the smallest sizes verified with the writer.


class AutoSizer:
    """Sizing engine: smallest fitting geometry for a payload.

    Backed by the GFX reference profile (reserved for future
    per-camera presets)."""

    def __init__(self) -> None:
        pass

    def recommend(
        self,
            payload_len: int,
            width: int | None = None,
            height: int | None = None,
            mode: str | None = None,
            bit_depth: int | None = None,
            lsb_planes: int | None = None,
            auto_size: bool = False,
            frames: int = 1,
        ) -> dict:
        """Choose the smallest configuration that fits ``payload_len`` bytes.

        Any argument left as ``None`` is auto-selected; explicitly passed
        values are always respected (and validated). With ``auto_size=True``
        (no preset geometries) the smallest 4:3 width/height holding the
        payload is computed instead, which also minimizes the output file.
        ``frames`` scales capacity (payload is striped over that many raw
        SubIFDs); it is never auto-bumped, only validated. Returns a dict
        with ``width``, ``height``, ``mode``, ``bit_depth``, ``lsb_planes``,
        ``frames``, ``capacity`` and ``auto`` (names of the auto-chosen
        fields).

        Raises ValueError (stating the payload size, the relevant maximum
        capacity and how to proceed) when nothing fits. Sizes in errors are
        reported in kilobytes.
        """
        if mode is None:
            mode_eff = "linear"
        else:
            if mode not in ("linear", "cfa"):
                raise ValueError("mode must be 'linear' or 'cfa'")
            mode_eff = mode
        if bit_depth is None:
            depth_eff = 16
        else:
            if bit_depth not in SUPPORTED_BIT_DEPTHS:
                raise ValueError(
                    f"bit_depth must be one of {SUPPORTED_BIT_DEPTHS}")
            depth_eff = bit_depth
        if lsb_planes is not None and not (1 <= lsb_planes <= MAX_LSB_PLANES):
            raise ValueError(
                f"lsb_planes must be 1-{MAX_LSB_PLANES} (got {lsb_planes})")
        if not (1 <= frames <= MAX_FRAMES):
            raise ValueError(f"frames must be 1-{MAX_FRAMES} (got {frames})")
        if lsb_planes is not None and lsb_planes > depth_eff:
            raise ValueError(
                f"lsb_planes ({lsb_planes}) exceeds bit_depth ({depth_eff}); "
                f"payload values would overflow the declared WhiteLevel. "
                f"Use --bit-depth 16 (full-range uint16, up to 16 planes) or "
                f"fewer planes.")

        factor = 3 if mode_eff == "linear" else 1

        def cap(w: int, h: int, p: int) -> int:
            return capacity_bytes_total(w * h * factor, p, frames)

        if auto_size and (width is not None or height is not None):
            raise ValueError(
                "--auto-size cannot be combined with explicit "
                "--width/--height (it computes dimensions itself)")
        auto: list[str] = []
        if mode is None:
            auto.append("mode")
        if bit_depth is None:
            auto.append("bit_depth")

        if width is not None or height is not None:
            # One-sided geometry: complete via the 4:3 GFX aspect.
            if width is None:
                assert height is not None
                width = round(height * 4 / 3)
                auto.append("width")
            if height is None:
                height = round(width * 3 / 4)
                auto.append("height")
            if width <= 0 or height <= 0:
                raise ValueError(
                    f"width and height must be positive (got {width}x{height})")
            if lsb_planes is not None:
                c = cap(width, height, lsb_planes)
                if payload_len <= c:
                    return {"width": width, "height": height, "mode": mode_eff,
                            "bit_depth": depth_eff, "lsb_planes": lsb_planes,
                            "frames": frames,
                            "capacity": c, "auto": auto, "preset": None}
                c_max = cap(width, height, _top_planes(depth_eff))
                gbl = cap(PIXELSHIFT_W, PIXELSHIFT_H, _top_planes(depth_eff))
                raise ValueError(
                    f"payload {_kb_hi(payload_len)} exceeds capacity {_kb_lo(c)} "
                    f"for {width}x{height} {mode_eff} {depth_eff}-bit with "
                    f"{lsb_planes} LSB plane(s) "
                    f"(max at this geometry with {_top_planes(depth_eff)} planes: "
                    f"{_kb(c_max)}; largest supported configuration "
                    f"({_max_config_str(mode_eff, depth_eff, frames)}): {_kb(gbl)}). "
                    "Use a larger --width/--height, more --lsb-planes, more "
                    "--raw-frames, leave dimensions unset for auto-sizing, or "
                    "split the input across multiple DNGs.")
            for p in range(1, min(MAX_LSB_PLANES, depth_eff) + 1):
                c = cap(width, height, p)
                if payload_len <= c:
                    return {"width": width, "height": height, "mode": mode_eff,
                            "bit_depth": depth_eff, "lsb_planes": p,
                            "frames": frames,
                            "capacity": c, "auto": auto + ["lsb_planes"],
                            "preset": None}
            top = _top_planes(depth_eff)
            c_max = cap(width, height, top)
            gbl = cap(PIXELSHIFT_W, PIXELSHIFT_H, top)
            raise ValueError(
                f"payload {_kb_hi(payload_len)} exceeds capacity {_kb_lo(c_max)} "
                f"for {width}x{height} {mode_eff} {depth_eff}-bit even with "
                f"{top} LSB planes (largest supported configuration "
                f"({_max_config_str(mode_eff, depth_eff, frames)}): {_kb(gbl)}). "
                "Use a larger --width/--height, leave dimensions unset for "
                "auto-sizing, more --raw-frames, or split the input across "
                "multiple DNGs.")

        top = _top_planes(depth_eff)
        planes_list = ([lsb_planes] if lsb_planes is not None
                       else list(range(1, top + 1)))
        if auto_size:
            need_bits = (payload_len + HEADER_LEN) * 8
            for p in planes_list:
                # Per-frame slot need: the bitstream is striped over frames.
                need_px = math.ceil(
                    math.ceil(need_bits / p / frames) / factor)
                w = math.ceil(math.sqrt(need_px * 4 / 3))
                # Closed-form height: smallest h with cap(w,h,p) >= payload
                # while keeping the 4:3 frame when it already fits.
                h = max(math.ceil(w * 3 / 4),
                        math.ceil(need_bits / (frames * w * factor * p)))
                # Even dimensions keep Bayer cells whole.
                w += w % 2
                h += h % 2
                w = max(w, AUTO_MIN_W)
                h = max(h, AUTO_MIN_H)
                for _ in range(8):  # integer-rounding backstop
                    if cap(w, h, p) >= payload_len:
                        break
                    h += 2
                else:
                    continue  # unreachable in practice; try more planes
                if w <= PIXELSHIFT_W and h <= PIXELSHIFT_H:
                    auto_fields = auto + ["width", "height"]
                    if lsb_planes is None:
                        auto_fields = auto_fields + ["lsb_planes"]
                    return {"width": w, "height": h, "mode": mode_eff,
                            "bit_depth": depth_eff, "lsb_planes": p,
                            "frames": frames,
                            "capacity": cap(w, h, p), "auto": auto_fields,
                            "preset": "auto-size"}
        else:
            # Smallest preset geometry (then fewest planes) that fits.
            for (w, h, label) in PRESET_GEOMETRIES:
                for p in planes_list:
                    c = cap(w, h, p)
                    if payload_len <= c:
                        auto_fields = auto + ["width", "height"]
                        if lsb_planes is None:
                            auto_fields = auto_fields + ["lsb_planes"]
                        return {"width": w, "height": h, "mode": mode_eff,
                                "bit_depth": depth_eff, "lsb_planes": p,
                                "frames": frames,
                                "capacity": c, "auto": auto_fields,
                                "preset": label}
        p_max = planes_list[-1]
        gbl = cap(PIXELSHIFT_W, PIXELSHIFT_H, p_max)
        abs_max = cap(PIXELSHIFT_W, PIXELSHIFT_H, top)
        hint = ""
        if lsb_planes is not None and lsb_planes < top:
            hint = (f" (with {top} LSB planes the max would be "
                    f"{_kb_lo(abs_max)})")
        if mode_eff == "cfa":
            abs_lin = capacity_bytes(
                PIXELSHIFT_W * PIXELSHIFT_H * 3, MAX_LSB_PLANES)
            hint += (f" (linear mode max would be {_kb_lo(abs_lin)})")
        if auto_size:
            hint += (" (--auto-size already uses minimal dimensions; only "
                     "more planes, linear mode, or splitting the input help)")
        raise ValueError(
            f"payload {_kb_hi(payload_len)} exceeds maximum capacity {_kb_lo(gbl)} "
            f"under the given constraints "
            f"(largest supported configuration "
            f"({_max_config_str(mode_eff, depth_eff, frames)}): {_kb_lo(abs_max)})"
            f"{hint}. Split the input across multiple DNGs.")

    @staticmethod
    def max_config(mode: str, bit_depth: int, frames: int = 1) -> str:
        return _max_config_str(mode, bit_depth, frames)

    @staticmethod
    def risk_warnings(cfg: dict, key: bool) -> list[str]:
        return risk_warnings(cfg, key)




def recommend(
    payload_len: int,
    width: int | None = None,
    height: int | None = None,
    mode: str | None = None,
    bit_depth: int | None = None,
    lsb_planes: int | None = None,
    auto_size: bool = False,
    frames: int = 1,
) -> dict:
    """Backwards-compatible wrapper (see :meth:`AutoSizer.recommend`)."""
    return AutoSizer().recommend(
        payload_len, width=width, height=height, mode=mode,
        bit_depth=bit_depth, lsb_planes=lsb_planes,
        auto_size=auto_size, frames=frames,
    )




def risk_warnings(cfg: dict, key: bool) -> list[str]:
    """High-density option warnings (also see README detection risks).

    Planes > 4, extra raw frames, sub-14-bit depths and exact-fit
    dimensions all deviate from plausible GFX 100 II combiner output.
    """
    out: list[str] = []
    p, depth, frames = cfg["lsb_planes"], cfg["bit_depth"], cfg["frames"]
    if p > 4:
        if p >= MAX_LSB_PLANES:
            out.append(
                f"warning: {p} LSB planes leave no cover: every sample bit "
                f"is payload, so the raw image renders as noise. "
                f"Bit-plane statistics trivially expose this.")
        elif p >= 9:
            out.append(
                f"warning: {p} LSB planes destroy most of the "
                f"{depth}-bit cover signal; the raw image will look "
                f"severely degraded/noise-like.")
        else:
            out.append(
                f"warning: {p} LSB planes heavily degrade the cover image "
                f"(only {depth - p} of {depth} bits per sample remain "
                f"photographic).")
    if frames > 1:
        out.append(
            f"warning: {frames} full-resolution raw frames in one still "
            f"DNG is non-standard (burst/stack-style multi-image TIFFs "
            f"exist, but no GFX combiner output looks like this) and "
            f"multiplies the file size ~{frames}x.")
    if depth < 14:
        out.append(
            f"warning: {depth}-bit is below every GFX 100 II option "
            f"(14/16-bit); the BitsPerSample tag alone marks the file "
            f"as unusual for this camera story.")
    if out and not key:
        out.append(
            "warning: high-risk options without --key leave the payload "
            "readable to anyone extracting LSBs; consider encrypting.")
    return out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------



def _risk_warnings(cfg: dict, key: bool) -> list[str]:
    """Backwards-compatible alias for :func:`risk_warnings`."""
    return risk_warnings(cfg, key)


#: Backwards-compatible alias for :func:`recommend` (the original name).
recommend_config = recommend
