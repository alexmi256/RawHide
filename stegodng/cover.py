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
        """
        if bit_depth not in SUPPORTED_BIT_DEPTHS:
            raise ValueError(f"bit_depth must be one of {SUPPORTED_BIT_DEPTHS}")
        rng = np.random.default_rng(self._seed)
        yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
        peak = (1 << bit_depth) - 1
        scale = peak / 65535.0
        base16 = (
            7000
            + 2600 * (yy / max(height - 1, 1))
            + 1400 * (xx / max(width - 1, 1))
            + 500 * np.sin(2 * np.pi * xx / max(width, 1) * 3)
        )
        base = base16 * scale
        sigma = 420 * scale
        if bit_depth <= 8:
            dtype = np.uint8
            step = 1 << (8 - bit_depth) if bit_depth < 8 else 1
        else:
            dtype = np.uint16
            step = 1 << (16 - bit_depth) if bit_depth < 16 else 1
        if mode == "linear":
            gains = np.array([1.0, 0.94, 0.82], dtype=np.float32)  # R,G,B-ish
            cover = np.empty((height, width, 3), dtype=dtype)
            for c in range(3):
                noise = rng.normal(0, sigma, size=(height, width)).astype(np.float32)
                plane = np.clip(base * gains[c] + noise, 0, peak)
                if step > 1:
                    plane = np.floor(plane / step) * step
                cover[:, :, c] = plane.astype(dtype)
        elif mode == "cfa":
            noise = rng.normal(0, sigma, size=(height, width)).astype(np.float32)
            plane = np.clip(base + noise, 0, peak)
            # RGGB Bayer gains per 2x2 cell
            plane[0::2, 0::2] *= 1.00
            plane[0::2, 1::2] *= 0.94
            plane[1::2, 0::2] *= 0.94
            plane[1::2, 1::2] *= 0.82
            plane = np.clip(plane, 0, peak)
            if step > 1:
                plane = np.floor(plane / step) * step
            cover = plane.astype(dtype)
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
