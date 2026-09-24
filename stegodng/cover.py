"""Synthetic photographic-like covers (gradient + noise + Bayer gains).

The cover is what the raw samples look like before payload bits replace
the low planes; it keeps bit-plane statistics plausible. Covers are
rescaled per bit depth so exposure stays constant instead of saturating.
"""
from __future__ import annotations

import numpy as np

from .profile import SUPPORTED_BIT_DEPTHS


class CoverGenerator:
    def __init__(self, seed: int | None = None) -> None:
        self._seed = 0 if seed is None else seed

    def cover(self, height: int, width: int, mode: str,
              bit_depth: int) -> np.ndarray:
        """Photographic-like raw cover: uint8 for 8-bit, else uint16.

        10/12/14-bit values are quantized to ``2**(16 - bit_depth)`` steps
        so packed BitsPerSample files round-trip exactly.

        Banded implementation: rows are generated in strips so peak
        temporaries stay at ``BAND_ROWS * width`` instead of
        ``height * width`` (the previous ``np.mgrid`` held two full-frame
        float32 grids plus a float64 noise frame — gigabytes at
        16382x12286). Element-wise math and the RNG draw order are
        unchanged, so covers are bit-identical to the old code.
        """
        if bit_depth not in SUPPORTED_BIT_DEPTHS:
            raise ValueError(f"bit_depth must be one of {SUPPORTED_BIT_DEPTHS}")
        rng = np.random.default_rng(self._seed)
        peak = (1 << bit_depth) - 1
        scale = peak / 65535.0
        sigma = 420 * scale
        if bit_depth <= 8:
            dtype = np.uint8
            step = 1 << (8 - bit_depth) if bit_depth < 8 else 1
        else:
            dtype = np.uint16
            step = 1 << (16 - bit_depth) if bit_depth < 16 else 1
        h_denom = max(height - 1, 1)
        w_denom = max(width - 1, 1)
        cols = np.arange(width, dtype=np.float32)
        # Column terms are width-1D; rows broadcast per band. Values match
        # ``np.mgrid[0:H,0:W].astype(np.float32)`` element-wise (exact for
        # these sizes) while never materializing full-frame yy/xx grids.
        col_frac = cols / w_denom
        sin_col = np.sin(2 * np.pi * cols / max(width, 1) * 3)
        band = 512
        if mode == "linear":
            gains = np.array([1.0, 0.94, 0.82], dtype=np.float32)  # R,G,B-ish
            cover = np.empty((height, width, 3), dtype=dtype)
            # Channels outer, bands inner: preserves the historic RNG draw
            # order (full channel 0, then 1, then 2) so covers stay
            # bit-identical while peak stays at band size.
            for c in range(3):
                for y0 in range(0, height, band):
                    y1 = min(y0 + band, height)
                    rows = np.arange(y0, y1, dtype=np.float32)[:, None]
                    base16 = (
                        7000
                        + 2600 * (rows / h_denom)
                        + 1400 * col_frac[None, :]
                        + 500 * sin_col[None, :]
                    )
                    base = base16 * scale
                    noise = rng.normal(
                        0, sigma, size=(y1 - y0, width)).astype(np.float32)
                    plane = np.clip(base * gains[c] + noise, 0, peak)
                    if step > 1:
                        plane = np.floor(plane / step) * step
                    cover[y0:y1, :, c] = plane.astype(dtype)
        elif mode == "cfa":
            cover = np.empty((height, width), dtype=dtype)
            for y0 in range(0, height, band):
                y1 = min(y0 + band, height)
                rows = np.arange(y0, y1, dtype=np.float32)[:, None]
                base16 = (
                    7000
                    + 2600 * (rows / h_denom)
                    + 1400 * col_frac[None, :]
                    + 500 * sin_col[None, :]
                )
                base = base16 * scale
                noise = rng.normal(
                    0, sigma, size=(y1 - y0, width)).astype(np.float32)
                plane = np.clip(base + noise, 0, peak)
                # RGGB Bayer gains per 2x2 cell, keyed to absolute frame
                # coordinates (band-relative slicing would shift parity
                # for odd y0, so offset the starts by y0 % 2).
                r_even = 0 if y0 % 2 == 0 else 1
                r_odd = 1 if y0 % 2 == 0 else 0
                plane[r_even::2, 0::2] *= 1.00
                plane[r_even::2, 1::2] *= 0.94
                plane[r_odd::2, 0::2] *= 0.94
                plane[r_odd::2, 1::2] *= 0.82
                plane = np.clip(plane, 0, peak)
                if step > 1:
                    plane = np.floor(plane / step) * step
                cover[y0:y1, :] = plane.astype(dtype)
        else:  # pragma: no cover
            raise ValueError("mode must be 'linear' or 'cfa'")
        return np.ascontiguousarray(cover)

    def thumbnail(self, height: int, width: int) -> np.ndarray:
        rng = np.random.default_rng(self._seed + 999)
        yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
        r = 90 + 90 * (xx / max(width - 1, 1)) + rng.normal(0, 9, (height, width))
        g = 100 + 70 * (yy / max(height - 1, 1)) + rng.normal(0, 9, (height, width))
        b = 110 - 40 * (xx / max(width - 1, 1)) + rng.normal(0, 9, (height, width))
        thumb = np.stack(
            [np.clip(r, 0, 255), np.clip(g, 0, 255), np.clip(b, 0, 255)], axis=-1
        ).astype(np.uint8)
        return np.ascontiguousarray(thumb)


def make_cover(height: int, width: int, seed: int | None, mode: str,
               bit_depth: int) -> np.ndarray:
    """Backwards-compatible wrapper (see :meth:`CoverGenerator.cover`)."""
    return CoverGenerator(seed).cover(height, width, mode, bit_depth)


def make_thumbnail(height: int, width: int, seed: int | None) -> np.ndarray:
    """Backwards-compatible wrapper (see :meth:`CoverGenerator.thumbnail`)."""
    return CoverGenerator(seed).thumbnail(height, width)
