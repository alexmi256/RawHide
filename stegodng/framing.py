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

import numpy as np


class PayloadFrame:
    MAGIC = b"DNGS"
    VERSION = 1
    HEADER_LEN = 4 + 1 + 1 + 8 + 4  # magic, version, flags, len-u64be, crc32-be
    FLAG_KEYED = 0x01

    # Chunk size for streaming XOR so a 1 GB payload never holds a 1 GB
    # keystream beside a 1 GB output (plus avoids the previous per-byte
    # Python ``bytes(b ^ k ...)`` loop, which was hours at GB scale).
    _XOR_CHUNK = 4 << 20

    @staticmethod
    def _keystream(key: bytes, length: int) -> bytes:
        """SHA-256 counter keystream (simple stream cipher, no extra deps)."""
        out = bytearray()
        ctr = 0
        while len(out) < length:
            out += hashlib.sha256(key + struct.pack(">Q", ctr)).digest()
            ctr += 1
        return bytes(out[:length])

    @staticmethod
    def _keystream_range(key: bytes, offset: int, length: int) -> bytes:
        """Keystream slice ``[offset, offset+length)`` without building
        the full prefix (identical bytes to :meth:`_keystream`)."""
        if length <= 0:
            return b""
        ctr0 = offset // 32
        skip = offset % 32
        need = skip + length
        n_hash = (need + 31) // 32
        out = bytearray(n_hash * 32)
        pos = 0
        for ctr in range(ctr0, ctr0 + n_hash):
            out[pos:pos + 32] = hashlib.sha256(
                key + struct.pack(">Q", ctr)).digest()
            pos += 32
        return bytes(out[skip:skip + length])

    @classmethod
    def _xor_data(cls, data: bytes, key: bytes) -> bytes:
        """XOR ``data`` with the counter keystream (streaming, numpy)."""
        if not data:
            return b""
        out = bytearray(len(data))
        for off in range(0, len(data), cls._XOR_CHUNK):
            chunk = data[off:off + cls._XOR_CHUNK]
            ks = cls._keystream_range(key, off, len(chunk))
            a = np.frombuffer(chunk, dtype=np.uint8)
            b = np.frombuffer(ks, dtype=np.uint8)
            out[off:off + len(chunk)] = np.bitwise_xor(a, b).tobytes()
        return bytes(out)

    @classmethod
    def pack(cls, payload: bytes, key: bytes | None) -> bytes:
        """Frame ``payload`` for embedding (header + body)."""
        flags = 0
        if key:
            flags |= cls.FLAG_KEYED
        body = cls._xor_data(payload, key) if key else payload
        header = cls.MAGIC + bytes((cls.VERSION, flags)) + struct.pack(
            ">Q", len(payload)
        ) + struct.pack(">I", zlib.crc32(payload) & 0xFFFFFFFF)
        if key:
            header = cls._xor_data(header, key)
        return header + body

    @classmethod
    def unpack(cls, stream: bytes, key: bytes | None) -> tuple[bytes, int]:
        """Return (payload, total_frame_len). Raises ValueError on failure."""
        if len(stream) < cls.HEADER_LEN:
            raise ValueError("bitstream too short for header")
        header = stream[:cls.HEADER_LEN]
        if key:
            header = cls._xor_data(header, key)
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
            body = cls._xor_data(body, key)
        if zlib.crc32(body) & 0xFFFFFFFF != crc:
            raise ValueError("CRC32 mismatch - corrupt payload or wrong key")
        return body, total
