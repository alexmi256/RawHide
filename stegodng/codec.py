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

    # Target ~8 Mbits of payload bitstream per processing chunk. This
    # bounds all temporaries (unpacked bits, per-plane views) to tens of
    # MB regardless of total payload size.
    _CHUNK_BITS = 8 << 20

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
    def _chunk_samples(lsb_planes: int) -> int:
        """Samples per streaming chunk (~_CHUNK_BITS payload bits)."""
        return max(256 * 1024, LsbCodec._CHUNK_BITS // max(1, lsb_planes))

    @staticmethod
    def _bits_for_range(farr: np.ndarray, start: int,
                        length: int) -> np.ndarray:
        """Unpacked bits (uint8 0/1) for frame-bit interval [start, end).

        ``farr`` is the framed payload as a uint8 array (no copy). Only
        the covering bytes are unpacked, so peak cost is ~8x the chunk
        size, never ~8x the whole payload.
        """
        if length <= 0:
            return np.empty(0, dtype=np.uint8)
        byte_lo = start // 8
        bit_off = start % 8
        byte_hi = (start + length + 7) // 8
        unpacked = np.unpackbits(farr[byte_lo:byte_hi])
        return unpacked[bit_off:bit_off + length]

    @staticmethod
    def _embed_bits_into_window(window32: np.ndarray, bits: np.ndarray,
                                lsb_planes: int) -> None:
        """Write ``bits`` into ``window32`` (uint32 sample chunk) in place.

        Bit ``i`` goes to plane ``i % lsb_planes`` of sample
        ``i // lsb_planes`` — identical mapping to the historic
        ``arange`` implementation, but via strided slices (no int64
        index array).
        """
        for p in range(lsb_planes):
            sub = bits[p::lsb_planes]
            if sub.size == 0:
                continue
            window32[:sub.size] = (
                (window32[:sub.size] & ~(np.uint32(1 << p)))
                | (sub.astype(np.uint32, copy=False) << np.uint32(p))
            )

    @staticmethod
    def embed_bitarray(cover: np.ndarray, bits: np.ndarray,
                       lsb_planes: int) -> np.ndarray:
        """Write ``bits`` (uint8 0/1, any length <= slots) into cover LSBs."""
        n_slots = cover.size * lsb_planes
        if bits.size > n_slots:
            raise ValueError(
                f"payload too large: need {bits.size} bits, "
                f"capacity is {n_slots} bits")
        bits = np.ascontiguousarray(bits, dtype=np.uint8)
        stego = cover.reshape(-1).astype(np.uint32)
        LsbCodec._embed_bits_into_window(stego, bits, lsb_planes)
        return stego.reshape(cover.shape).astype(cover.dtype)

    @staticmethod
    def extract_bitarray(raw: np.ndarray, lsb_planes: int,
                         n_bits: int) -> np.ndarray:
        """Read ``n_bits`` LSBs (uint8 0/1) from raw samples in embed order."""
        if n_bits > raw.size * lsb_planes:
            raise ValueError(
                f"request too large: need {n_bits} bits, "
                f"capacity is {raw.size * lsb_planes} bits")
        flat = raw.reshape(-1)
        bits = np.empty(n_bits, dtype=np.uint8)
        for p in range(lsb_planes):
            view = bits[p::lsb_planes]
            if view.size == 0:
                continue
            view[:] = ((flat[:view.size] >> np.uint32(p)) & np.uint32(1)
                       ).astype(np.uint8)
        return bits

    @classmethod
    def embed_bits(cls, cover: np.ndarray, frame: bytes,
                   lsb_planes: int) -> np.ndarray:
        """Embed ``frame`` into ``cover`` LSBs (in place, see
        :meth:`stripe_frames`)."""
        n_slots = cover.size * lsb_planes
        if len(frame) * 8 > n_slots:
            raise ValueError(
                f"payload too large: need {len(frame) * 8} bits, "
                f"capacity is {n_slots} bits "
                f"({format_kb(cls.capacity_bytes(cover.size, lsb_planes))} payload capacity)"
            )
        return cls.stripe_frames([cover], frame, lsb_planes)[0]

    @staticmethod
    def stripe_frames(covers: list[np.ndarray], frame: bytes,
                      lsb_planes: int) -> list[np.ndarray]:
        """Unpack a framed payload and stripe its bits over frame covers
        in write order (one shared helper so single- and split-file
        encodes cannot drift apart).

        Streaming implementation: the frame is never fully unpacked
        (``np.unpackbits`` on a 1 GB payload would need ~8 GB of bit
        array) and no ``np.arange`` index array is built (the previous
        ``int64`` index needed ~8 bytes per payload *bit*, i.e. ~72 GiB
        for the 16382x12286/16-plane case in the bug report). Each cover
        is processed in ~8-Mbit sample chunks with identical bit mapping.

        Raises ValueError when the framed bitstream exceeds the combined
        cover slots (previous implementation silently truncated the
        excess; failing closed avoids silent data loss).

        Memory: covers are embedded **in place** — the returned list
        holds the same array objects (same buffers), so callers must
        treat ``covers`` as consumed. This avoids a second full-frame
        copy beside the covers (gigabytes at PixelShift scale).
        Non-contiguous inputs fall back to a contiguous copy for that
        cover.
        """
        farr = np.frombuffer(frame, dtype=np.uint8)
        total_bits = len(frame) * 8
        total_slots = sum(c.size * lsb_planes for c in covers)
        if total_bits > total_slots:
            raise ValueError(
                f"payload too large: need {total_bits} bits, "
                f"capacity is {total_slots} bits")
        chunk_samples = LsbCodec._chunk_samples(lsb_planes)
        stegos: list[np.ndarray] = []
        pos = 0
        for cover in covers:
            n_slots = cover.size * lsb_planes
            take = min(n_slots, total_bits - pos)
            flat = cover.reshape(-1)
            if np.shares_memory(flat, cover):
                inplace = True
            else:
                # Non-contiguous input: reshape copied, so embed into a
                # contiguous copy and return it (previous behavior).
                flat = np.ascontiguousarray(cover).reshape(-1)
                inplace = False
            if take > 0:
                n_used = (take + lsb_planes - 1) // lsb_planes
                for s0 in range(0, n_used, chunk_samples):
                    s1 = min(s0 + chunk_samples, n_used)
                    b0 = pos + s0 * lsb_planes
                    b1 = min(pos + s1 * lsb_planes, pos + take)
                    bits = LsbCodec._bits_for_range(farr, b0, b1 - b0)
                    ns = (bits.size + lsb_planes - 1) // lsb_planes
                    window = flat[s0:s0 + ns].astype(np.uint32)
                    LsbCodec._embed_bits_into_window(window, bits,
                                                     lsb_planes)
                    flat[s0:s0 + ns] = window.astype(flat.dtype)
            stegos.append(cover if inplace else flat.reshape(cover.shape))
            pos += take
        return stegos

    @staticmethod
    def extract_stream(raws: list[np.ndarray], lsb_planes: int,
                       total_bits: int) -> bytes:
        """Gather ``total_bits`` LSBs across ordered raw frames -> bytes.

        Streaming counterpart of :meth:`stripe_frames`: extracts in
        ~8-Mbit sample chunks and packs incrementally, so a 1 GB payload
        never materializes its ~8 GB unpacked bit array.
        """
        if total_bits % 8:
            raise ValueError("total_bits must be a whole number of bytes")
        out = bytearray(total_bits // 8)
        out_pos = 0
        pending = np.empty(0, dtype=np.uint8)
        remaining = total_bits
        chunk_samples = LsbCodec._chunk_samples(lsb_planes)
        done = False
        for raw in raws:
            if done:
                break
            flat = raw.reshape(-1)
            take = min(raw.size * lsb_planes, remaining)
            n_used = (take + lsb_planes - 1) // lsb_planes
            for s0 in range(0, n_used, chunk_samples):
                s1 = min(s0 + chunk_samples, n_used)
                length = min(s1 * lsb_planes, take) - s0 * lsb_planes
                ns = (length + lsb_planes - 1) // lsb_planes
                seg = flat[s0:s0 + ns]
                bits = np.empty(length, dtype=np.uint8)
                for p in range(lsb_planes):
                    view = bits[p::lsb_planes]
                    if view.size == 0:
                        continue
                    view[:] = ((seg[:view.size] >> np.uint32(p))
                               & np.uint32(1)).astype(np.uint8)
                if pending.size:
                    bits = np.concatenate((pending, bits))
                    pending = np.empty(0, dtype=np.uint8)
                n_full = (bits.size // 8) * 8
                if n_full:
                    out[out_pos:out_pos + n_full // 8] = np.packbits(
                        bits[:n_full]).tobytes()
                    out_pos += n_full // 8
                if n_full < bits.size:
                    pending = bits[n_full:].copy()
            remaining -= take
            if remaining <= 0:
                done = True
        if pending.size:  # pragma: no cover - total_bits is byte-multiple
            raise ValueError("bitstream ended mid-byte")
        return bytes(out)

    @classmethod
    def extract_bits(cls, raw: np.ndarray, lsb_planes: int,
                     n_bytes: int) -> bytes:
        if n_bytes == 0:
            return b""
        return cls.extract_stream([raw], lsb_planes, n_bytes * 8)


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
