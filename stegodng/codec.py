"""LSB steganography codec for raw samples.

Bit ``i`` of the framed payload goes to plane ``i % lsb_planes`` of sample
``i // lsb_planes``, spreading the payload over all tiles/channels. All
arithmetic runs in uint32 so uint8 and uint16 covers behave identically.
"""
from __future__ import annotations

import math

import numpy as np

from .framing import PayloadFrame


def format_kb(n: int) -> str:
    """Format a byte count as kilobytes for user-facing messages."""
    return f"{n / 1024:,.1f} KB"


def format_kb_hi(n: int) -> str:
    """Like :func:`format_kb` but rounded up (payload sizes in errors)."""
    return f"{math.ceil(n / 1024 * 10) / 10:,.1f} KB"


def format_kb_lo(n: int) -> str:
    """Like :func:`format_kb` but rounded down (capacities in errors)."""
    return f"{math.floor(n / 1024 * 10) / 10:,.1f} KB"


# Legacy aliases (stego_dng shim re-exports these names).
_kb = format_kb
_kb_hi = format_kb_hi
_kb_lo = format_kb_lo


class LsbCodec:
    """LSB embed/extract over raw sample arrays."""

    def __init__(self, lsb_planes: int = 1) -> None:
        self.lsb_planes = lsb_planes

    @staticmethod
    def capacity_bytes(n_samples: int, lsb_planes: int) -> int:
        return LsbCodec.capacity_bytes_total(n_samples, lsb_planes, 1)

    @staticmethod
    def capacity_bytes_total(n_samples_per_frame: int, lsb_planes: int,
                             frames: int = 1) -> int:
        """Total payload bytes across ``frames`` equal frames sharing one
        header (a single floor over all slots, not one per frame)."""
        return ((n_samples_per_frame * lsb_planes * frames) // 8
                - PayloadFrame.HEADER_LEN)

    def capacity(self, n_samples: int) -> int:
        return self.capacity_bytes(n_samples, self.lsb_planes)

    @staticmethod
    def embed_bitarray(cover: np.ndarray, bits: np.ndarray,
                       lsb_planes: int) -> np.ndarray:
        """Write ``bits`` (uint8 0/1, any length <= slots) into cover LSBs."""
        n_slots = cover.size * lsb_planes
        if bits.size > n_slots:
            raise ValueError(
                f"payload too large: need {bits.size} bits, "
                f"capacity is {n_slots} bits")
        stego = cover.reshape(-1).astype(np.uint32).copy()
        idx = np.arange(bits.size)
        samples = idx // lsb_planes
        planes = idx % lsb_planes
        for p in range(lsb_planes):
            m = planes == p
            s = samples[m]
            stego[s] = (stego[s] & ~(np.uint32(1 << p))) | (
                bits[m].astype(np.uint32) << np.uint32(p))
        return stego.reshape(cover.shape).astype(cover.dtype)

    @staticmethod
    def extract_bitarray(raw: np.ndarray, lsb_planes: int,
                         n_bits: int) -> np.ndarray:
        """Read ``n_bits`` LSBs (uint8 0/1) from raw samples in embed order."""
        flat = raw.reshape(-1).astype(np.uint32)
        idx = np.arange(n_bits)
        samples = idx // lsb_planes
        planes = idx % lsb_planes
        bits = np.empty(n_bits, dtype=np.uint8)
        for p in range(lsb_planes):
            m = planes == p
            bits[m] = ((flat[samples[m]] >> np.uint32(p)) & np.uint32(1)).astype(np.uint8)
        return bits

    @classmethod
    def embed_bits(cls, cover: np.ndarray, frame: bytes,
                   lsb_planes: int) -> np.ndarray:
        bits = np.unpackbits(np.frombuffer(frame, dtype=np.uint8))
        n_slots = cover.size * lsb_planes
        if bits.size > n_slots:
            raise ValueError(
                f"payload too large: need {bits.size} bits, "
                f"capacity is {n_slots} bits "
                f"({format_kb(cls.capacity_bytes(cover.size, lsb_planes))} payload capacity)"
            )
        return cls.embed_bitarray(cover, bits, lsb_planes)

    @staticmethod
    def stripe_frames(covers: list[np.ndarray], frame: bytes,
                      lsb_planes: int) -> list[np.ndarray]:
        """Unpack a framed payload and stripe its bits over frame covers
        in write order (one shared helper so single- and split-file
        encodes cannot drift apart)."""
        bits = np.unpackbits(np.frombuffer(frame, dtype=np.uint8))
        stegos, pos = [], 0
        for cover in covers:
            seg = bits[pos:pos + cover.size * lsb_planes]
            stegos.append(LsbCodec.embed_bitarray(cover, seg, lsb_planes))
            pos += cover.size * lsb_planes
        return stegos

    @classmethod
    def extract_bits(cls, raw: np.ndarray, lsb_planes: int,
                     n_bytes: int) -> bytes:
        return np.packbits(
            cls.extract_bitarray(raw, lsb_planes, n_bytes * 8)).tobytes()


def capacity_bytes(n_samples: int, lsb_planes: int) -> int:
    """Backwards-compatible wrapper (see :meth:`LsbCodec.capacity_bytes`)."""
    return LsbCodec.capacity_bytes(n_samples, lsb_planes)


def embed_bits(cover: np.ndarray, frame: bytes, lsb_planes: int) -> np.ndarray:
    """Backwards-compatible wrapper (see :meth:`LsbCodec.embed_bits`)."""
    return LsbCodec.embed_bits(cover, frame, lsb_planes)


def extract_bits(raw: np.ndarray, lsb_planes: int, n_bytes: int) -> bytes:
    """Backwards-compatible wrapper (see :meth:`LsbCodec.extract_bits`)."""
    return LsbCodec.extract_bits(raw, lsb_planes, n_bytes)


def _embed_bitarray(cover: np.ndarray, bits: np.ndarray,
                    lsb_planes: int) -> np.ndarray:
    return LsbCodec.embed_bitarray(cover, bits, lsb_planes)


def _extract_bitarray(raw: np.ndarray, lsb_planes: int,
                      n_bits: int) -> np.ndarray:
    return LsbCodec.extract_bitarray(raw, lsb_planes, n_bits)


def capacity_bytes_total(n_samples_per_frame: int, lsb_planes: int,
                         frames: int = 1) -> int:
    """Backwards-compatible wrapper (see :meth:`LsbCodec.capacity_bytes_total`)."""
    return LsbCodec.capacity_bytes_total(n_samples_per_frame, lsb_planes,
                                         frames)
