"""Payload framing: magic + version + length + CRC32 header.

The framed stream is what actually gets embedded in (and recovered from)
the LSB planes. With a key, header and body are XOR-masked with a
SHA-256 counter keystream (confidentiality against casual inspection,
not authenticated encryption; a wrong key fails closed on magic/CRC).
"""
from __future__ import annotations

import hashlib
import os
import stat
import struct
import zlib
from typing import Any, BinaryIO, cast

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
    def _build_header(cls, payload_len: int, crc: int,
                      key: bytes | None) -> bytes:
        """Framed header for ``payload_len`` bytes with plaintext ``crc``."""
        flags = 0
        if key:
            flags |= cls.FLAG_KEYED
        header = cls.MAGIC + bytes((cls.VERSION, flags)) + struct.pack(
            ">Q", payload_len
        ) + struct.pack(">I", crc & 0xFFFFFFFF)
        return cls._xor_data(header, key) if key else header

    @classmethod
    def pack(cls, payload: bytes, key: bytes | None) -> bytes:
        """Frame ``payload`` for embedding (header + body)."""
        crc = zlib.crc32(payload) & 0xFFFFFFFF
        body = cls._xor_data(payload, key) if key else payload
        return cls._build_header(len(payload), crc, key) + body

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
        ver, _flags = header[4], header[5]
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


class PayloadReader:
    """Seekable byte source for a payload file, bytes blob or file object.

    ``read()`` never materializes the whole payload: file-backed readers
    seek + read only the requested byte range, and byte blobs are viewed
    through a :class:`memoryview` (no copy).  This is what lets
    :class:`FramedPayload` serve arbitrary bit ranges to the codec while
    the payload itself stays on disk.
    """

    _CHUNK = 4 << 20

    def __init__(self, source: bytes | bytearray | memoryview
                 | str | os.PathLike | BinaryIO) -> None:
        self._file: BinaryIO | None = None
        self._owns = False
        self._view: memoryview | None = None
        self._source: Any = None
        self._spooled = False
        self._base = 0
        if isinstance(source, (bytes, bytearray, memoryview)):
            self._view = memoryview(source)
            self.length = len(self._view)
        elif isinstance(source, (str, os.PathLike)):
            self._file = open(source, "rb")
            self._owns = True
            info = os.fstat(self._file.fileno())
            if stat.S_ISREG(info.st_mode):
                self.length = info.st_size
            else:
                # FIFO/device: st_size is 0 (or meaningless), so spool.
                self._spool(self._file.read())
        elif hasattr(source, "__len__") and hasattr(source, "__getitem__"):
            # Generic sequence of bytes (e.g. test doubles); slicing stays
            # lazy, so chunked encode still reads one range at a time.
            seq = cast(Any, source)
            self._source = seq
            self.length = len(seq)
        elif hasattr(source, "read"):
            self._file = source
            try:
                pos = source.tell()
                source.seek(0, os.SEEK_END)
                self.length = source.tell() - pos
                source.seek(pos)
                self._base = pos
            except (AttributeError, OSError, ValueError):
                # Non-seekable stream (pipe/stdin): the length is unknown,
                # so spool it once.  Callers on that path keep the old
                # whole-payload behavior.
                self._spool(source.read())
        else:
            raise TypeError(
                "payload must be bytes, a path, a binary file object or a "
                f"bytes-like sequence (got {type(source).__name__})")

    def _spool(self, data: bytes) -> None:
        """Buffer a non-seekable source (the only whole-payload path)."""
        self._view = memoryview(data)
        self._spooled = True
        self.length = len(self._view)
        if self._owns and self._file is not None:
            self._file.close()
        self._file = None
        self._owns = False

    def buffered(self) -> memoryview | None:
        """Spooled bytes for a non-seekable source, else ``None``.

        ``encode_split`` uses this for the single-chunk shortcut so a
        stream that was already consumed to measure its length is not
        re-read as empty.
        """
        return self._view if self._spooled else None

    # -- lifetime -----------------------------------------------------
    def close(self) -> None:
        if self._owns and self._file is not None:
            self._file.close()
        self._file = None
        self._view = None
        self._source = None

    def __del__(self) -> None:
        # Best-effort cleanup when an exception unwinds past the caller's
        # explicit close() (e.g. a capacity error mid-split).
        try:
            self.close()
        except Exception:
            pass

    def __enter__(self) -> "PayloadReader":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    # -- reading ------------------------------------------------------
    def read(self, offset: int, length: int) -> bytes | memoryview:
        """Bytes ``[offset, offset+length)`` relative to the payload start."""
        if length <= 0:
            return b""
        start = self._base + offset
        if self._view is not None:
            return self._view[start:start + length]
        if self._source is not None:
            data = self._source[start:start + length]
            if len(data) != length:
                raise ValueError("truncated payload")
            return data
        assert self._file is not None
        self._file.seek(start)
        data = self._file.read(length)
        if len(data) != length:
            raise ValueError("truncated payload")
        return data

    def crc32(self, offset: int = 0, length: int | None = None) -> int:
        """CRC32 of the byte range, streamed in `_CHUNK` pieces."""
        if length is None:
            length = self.length - offset
        crc = 0
        for pos in range(0, length, self._CHUNK):
            piece = self.read(offset + pos, min(self._CHUNK, length - pos))
            crc = zlib.crc32(piece, crc)
        return crc & 0xFFFFFFFF

    def framed(self, key: bytes | None, offset: int = 0,
               length: int | None = None) -> "FramedPayload":
        """A framed view over ``[offset, offset+length)`` of this source."""
        if length is None:
            length = self.length - offset
        if offset < 0 or length < 0 or offset + length > self.length:
            raise ValueError("payload range exceeds source length")
        return FramedPayload(self, offset, length, key,
                             self.crc32(offset, length))


class FramedPayload:
    """Random-access view of ``header ‖ body`` without a full-frame copy.

    Provides the same bytes :meth:`PayloadFrame.pack` would produce, but
    computes them on demand from a :class:`PayloadReader`.  The codec
    asks for bit ranges only, so peak memory stays at the chunk size
    regardless of payload size.
    """

    def __init__(self, reader: PayloadReader, offset: int, payload_len: int,
                 key: bytes | None, crc: int) -> None:
        self._reader = reader
        self._offset = offset
        self.payload_len = payload_len
        self._key = key
        self._header = PayloadFrame._build_header(payload_len, crc, key)

    def __len__(self) -> int:
        return PayloadFrame.HEADER_LEN + self.payload_len

    def _read_frame_bytes(self, offset: int, length: int) -> bytes:
        """Bytes ``[offset, offset+length)`` of the framed stream."""
        if length <= 0:
            return b""
        out = bytearray(length)
        start = 0
        if offset < PayloadFrame.HEADER_LEN:
            take = min(length, PayloadFrame.HEADER_LEN - offset)
            out[:take] = self._header[offset:offset + take]
            offset += take
            start = take
        if start < length:
            body_off = offset - PayloadFrame.HEADER_LEN
            n = length - start
            data = self._reader.read(self._offset + body_off, n)
            if self._key:
                keystream = PayloadFrame._keystream_range(
                    self._key, body_off, n)
                data = np.bitwise_xor(
                    np.frombuffer(data, dtype=np.uint8),
                    np.frombuffer(keystream, dtype=np.uint8)).tobytes()
            out[start:] = data
        return bytes(out)

    def read_bits(self, start_bit: int, n_bits: int) -> np.ndarray:
        """Unpacked bits (uint8 0/1) for frame-bit interval [start, end)."""
        if n_bits <= 0:
            return np.empty(0, dtype=np.uint8)
        byte_lo = start_bit // 8
        bit_off = start_bit % 8
        byte_hi = (start_bit + n_bits + 7) // 8
        buf = self._read_frame_bytes(byte_lo, byte_hi - byte_lo)
        unpacked = np.unpackbits(np.frombuffer(buf, dtype=np.uint8))
        return unpacked[bit_off:bit_off + n_bits]

    def frame_crc32_hex(self) -> str:
        """CRC32 of the complete framed stream as 8 lowercase hex digits."""
        crc = 0
        for pos in range(0, len(self), PayloadReader._CHUNK):
            chunk = self._read_frame_bytes(
                pos, min(PayloadReader._CHUNK, len(self) - pos))
            crc = zlib.crc32(chunk, crc)
        return f"{crc & 0xFFFFFFFF:08x}"


class FrameSink:
    """Streaming counterpart of :meth:`PayloadFrame.unpack`.

    Consumes the framed bitstream in pieces, decrypts the body and
    verifies length + CRC32 incrementally, writing the plaintext payload
    to ``sink``.  ``finish()`` raises ValueError when the stream is
    truncated or corrupt; callers that need atomic output should write
    to a temporary file and rename only after ``finish()`` succeeds.
    """

    def __init__(self, key: bytes | None, sink) -> None:
        self._key = key
        self._sink = sink
        self._head = bytearray()
        self._pos = 0
        self._crc = 0
        self._written = 0
        self._pay_len: int | None = None
        self._crc_expected: int | None = None

    def _parse_header(self) -> None:
        header = bytes(self._head)
        if self._key:
            header = PayloadFrame._xor_data(header, self._key)
        if header[:4] != PayloadFrame.MAGIC:
            raise ValueError(
                "magic not found - wrong key, wrong LSB depth or no payload"
            )
        if header[4] != PayloadFrame.VERSION:
            raise ValueError(f"unsupported frame version {header[4]}")
        (self._pay_len,) = struct.unpack(">Q", header[6:14])
        (self._crc_expected,) = struct.unpack(">I", header[14:18])

    def write(self, data: bytes) -> None:
        view = memoryview(data)
        if len(self._head) < PayloadFrame.HEADER_LEN:
            take = min(PayloadFrame.HEADER_LEN - len(self._head), len(view))
            self._head += view[:take]
            view = view[take:]
            self._pos += take
            if len(self._head) == PayloadFrame.HEADER_LEN:
                self._parse_header()
        if not view:
            return
        if self._pay_len is None:
            raise ValueError("bitstream too short for header")
        body_off = self._pos - PayloadFrame.HEADER_LEN
        if self._written + len(view) > self._pay_len:
            raise ValueError("framed stream longer than its declared payload")
        if self._key:
            keystream = PayloadFrame._keystream_range(
                self._key, body_off, len(view))
            view = np.bitwise_xor(
                np.frombuffer(view, dtype=np.uint8),
                np.frombuffer(keystream, dtype=np.uint8))
        self._crc = zlib.crc32(view, self._crc)
        self._sink.write(bytes(view))
        self._written += len(view)
        self._pos += len(view)

    def finish(self) -> int:
        """Verify the stream; return the recovered payload length."""
        if self._pay_len is None:
            raise ValueError("bitstream too short for header")
        if self._written != self._pay_len:
            raise ValueError("truncated payload")
        if (self._crc & 0xFFFFFFFF) != self._crc_expected:
            raise ValueError("CRC32 mismatch - corrupt payload or wrong key")
        return self._pay_len
