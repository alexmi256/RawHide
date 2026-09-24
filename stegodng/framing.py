"""Payload framing: magic + version + length + CRC32 header.

The framed stream is what actually gets embedded in (and recovered from)
the LSB planes. With a key, header and body are XOR-masked with a
SHA-256 counter keystream (confidentiality against casual inspection,
not authenticated encryption; a wrong key fails closed on magic/CRC).
"""
from __future__ import annotations

import hashlib
import struct
import zlib


class PayloadFrame:
    MAGIC = b"DNGS"
    VERSION = 1
    HEADER_LEN = 4 + 1 + 1 + 8 + 4  # magic, version, flags, len-u64be, crc32-be
    FLAG_KEYED = 0x01

    @staticmethod
    def _keystream(key: bytes, length: int) -> bytes:
        """SHA-256 counter keystream (simple stream cipher, no extra deps)."""
        out = bytearray()
        ctr = 0
        while len(out) < length:
            out += hashlib.sha256(key + struct.pack(">Q", ctr)).digest()
            ctr += 1
        return bytes(out[:length])

    @classmethod
    def pack(cls, payload: bytes, key: bytes | None) -> bytes:
        """Frame ``payload`` for embedding (header + body)."""
        flags = 0
        if key:
            flags |= cls.FLAG_KEYED
        body = payload
        if key:
            body = bytes(b ^ k for b, k in zip(payload, cls._keystream(key, len(payload))))
        header = cls.MAGIC + bytes((cls.VERSION, flags)) + struct.pack(
            ">Q", len(payload)
        ) + struct.pack(">I", zlib.crc32(payload) & 0xFFFFFFFF)
        if key:
            header = bytes(b ^ k for b, k in zip(header, cls._keystream(key, len(header))))
        return header + body

    @classmethod
    def unpack(cls, stream: bytes, key: bytes | None) -> tuple[bytes, int]:
        """Return (payload, total_frame_len). Raises ValueError on failure."""
        if len(stream) < cls.HEADER_LEN:
            raise ValueError("bitstream too short for header")
        header = stream[:cls.HEADER_LEN]
        if key:
            header = bytes(b ^ k for b, k in zip(header, cls._keystream(key, len(header))))
        if header[:4] != cls.MAGIC:
            raise ValueError(
                "magic not found - wrong key, wrong LSB depth or no payload"
            )
        ver, flags = header[4], header[5]
        if ver != cls.VERSION:
            raise ValueError(f"unsupported frame version {ver}")
        (pay_len,) = struct.unpack(">Q", header[6:14])
        (crc,) = struct.unpack(">I", header[14:18])
        total = cls.HEADER_LEN + pay_len
        if len(stream) < total:
            raise ValueError("truncated payload")
        body = stream[cls.HEADER_LEN:total]
        if key:
            body = bytes(b ^ k for b, k in zip(body, cls._keystream(key, len(body))))
        if zlib.crc32(body) & 0xFFFFFFFF != crc:
            raise ValueError("CRC32 mismatch - corrupt payload or wrong key")
        return body, total
