"""Streaming payload pipeline: file-backed framing, sink decode, CLI paths.

Hermetic: no network, ``thumbnail="synthetic"`` on every encode.
"""

import io
import os
import sys
import threading
import zlib

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stego_dng
from stegodng import DngStego, FrameSink, FramedPayload, PayloadFrame, PayloadReader
from stegodng.codec import LsbCodec


def _payload(n=5000, seed=1):
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=n, dtype=np.uint8).tobytes()


def _bytes_source(data):
    """File-like object that records every read size (no extra copies)."""
    class Spy(io.BytesIO):
        def __init__(self, blob):
            super().__init__(blob)
            self.read_sizes = []

        def read(self, n=-1):
            data = super().read(n)
            self.read_sizes.append(len(data))
            return data

    return Spy(data)


class _Pipe:
    """Non-seekable, non-sized binary stream (like stdin/a pipe)."""

    def __init__(self, data):
        self._buf = io.BytesIO(data)

    def read(self, n=-1):
        return self._buf.read(n)

    def tell(self):
        raise OSError("not seekable")

    def seek(self, *args):
        raise OSError("not seekable")


def test_payload_reader_crc_and_length(tmp_path):
    data = _payload(9000)
    path = tmp_path / "p.bin"
    path.write_bytes(data)
    with PayloadReader(str(path)) as reader:
        assert reader.length == len(data)
        assert reader.crc32() == zlib.crc32(data) & 0xFFFFFFFF
        assert reader.crc32(1000, 500) == (
            zlib.crc32(data[1000:1500]) & 0xFFFFFFFF)


@pytest.mark.parametrize("key", [None, b"stream-key"])
def test_framed_payload_matches_pack(tmp_path, key):
    data = _payload(7000)
    frame = PayloadFrame.pack(data, key)
    path = tmp_path / "frame.bin"
    path.write_bytes(data)
    with PayloadReader(str(path)) as reader:
        framed = reader.framed(key)
        assert len(framed) == len(frame)
        # Bit ranges crossing header/body and byte boundaries agree.
        for start, length in [(0, 144), (1, 7), (100, 1000),
                              (len(frame) * 8 - 500, 500)]:
            want = LsbCodec._bits_for_range(
                np.frombuffer(frame, dtype=np.uint8), start, length)
            got = framed.read_bits(start, length)
            assert np.array_equal(got, want)
        assert framed.frame_crc32_hex() == f"{zlib.crc32(frame) & 0xFFFFFFFF:08x}"


def test_framed_payload_reads_bounded_chunks():
    data = _payload(5 << 20)
    spy = _bytes_source(data)
    reader = PayloadReader(spy)
    framed = reader.framed(None)
    # Walk the whole frame; no single payload read may approach the
    # payload size (chunking keeps it at a few MB).
    step = LsbCodec._CHUNK_BITS
    for bit in range(0, len(framed) * 8, step):
        framed.read_bits(bit, min(step, len(framed) * 8 - bit))
    assert spy.read_sizes
    assert max(spy.read_sizes) <= (4 << 20)
    assert max(spy.read_sizes) < len(data)


def test_payload_reader_rejects_unknown_type():
    with pytest.raises(TypeError, match="payload must be"):
        PayloadReader(1234)


def test_frame_sink_verifies_crc_and_length():
    data = _payload(2000)
    key = b"k"
    frame = PayloadFrame.pack(data, key)
    out = io.BytesIO()
    sink = FrameSink(key, out)
    # Arbitrary chunk boundaries, including inside the header.
    for i in range(0, len(frame), 7):
        sink.write(frame[i:i + 7])
    assert sink.finish() == len(data)
    assert out.getvalue() == data

    bad = bytearray(frame)
    bad[-1] ^= 0xFF
    sink = FrameSink(key, io.BytesIO())
    sink.write(bytes(bad))
    with pytest.raises(ValueError, match="CRC32 mismatch"):
        sink.finish()

    sink = FrameSink(key, io.BytesIO())
    sink.write(frame[:-1])
    with pytest.raises(ValueError, match="truncated payload"):
        sink.finish()


def test_extract_stream_to_sink_matches_bytes():
    rng = np.random.default_rng(3)
    cover = rng.integers(0, 65535, size=(64, 64, 3)).astype(np.uint16)
    payload = _payload(1000)
    frame = PayloadFrame.pack(payload, None)
    stego = LsbCodec.stripe_frames([cover], frame, 2)[0]
    want = LsbCodec.extract_stream([stego], 2, len(frame) * 8)
    out = io.BytesIO()
    written = LsbCodec.extract_stream([stego], 2, len(frame) * 8, sink=out)
    assert written == len(want)
    assert out.getvalue() == want


def test_encode_from_path_and_file_matches_bytes(tmp_path):
    data = _payload(4000)
    src = tmp_path / "payload.bin"
    src.write_bytes(data)
    kwargs = dict(width=256, height=192, seed=5, thumbnail="synthetic")
    by_bytes = DngStego().encode(data, str(tmp_path / "a.dng"), **kwargs)
    by_path = DngStego().encode(str(src), str(tmp_path / "b.dng"), **kwargs)
    with open(src, "rb") as fh:
        by_file = DngStego().encode(fh, str(tmp_path / "c.dng"), **kwargs)
    assert by_bytes["payload_len"] == by_path["payload_len"] == 4000
    a = (tmp_path / "a.dng").read_bytes()
    assert a == (tmp_path / "b.dng").read_bytes()
    assert a == (tmp_path / "c.dng").read_bytes()
    assert by_file["payload_len"] == 4000
    assert DngStego().decode(str(tmp_path / "b.dng")) == data


def test_encode_keyed_from_path_roundtrip(tmp_path):
    data = _payload(3000)
    src = tmp_path / "payload.bin"
    src.write_bytes(data)
    out = tmp_path / "k.dng"
    DngStego().encode(str(src), str(out), width=256, height=192, seed=5,
                      key=b"pass", thumbnail="synthetic")
    assert DngStego().decode(str(out), key=b"pass") == data


def test_encode_split_from_path_matches_bytes(tmp_path):
    data = _payload(12000)
    src = tmp_path / "payload.bin"
    src.write_bytes(data)
    files_a = DngStego().encode_split(
        data, str(tmp_path / "a.dng"), 5000, width=256, height=192,
        seed=5, thumbnail="synthetic", split_id="setA")
    files_b = DngStego().encode_split(
        str(src), str(tmp_path / "b.dng"), 5000, width=256, height=192,
        seed=5, thumbnail="synthetic", split_id="setA")
    assert [i["payload_len"] for i in files_a] == [5000, 5000, 2000]
    assert [i["payload_len"] for i in files_b] == [5000, 5000, 2000]
    for ia, ib in zip(files_a, files_b):
        assert open(ia["path"], "rb").read() == open(ib["path"], "rb").read()
    assert DngStego().decode([i["path"] for i in files_b]) == data


def test_decode_to_matches_decode_and_is_atomic(tmp_path):
    data = _payload(6000)
    enc = tmp_path / "in.dng"
    DngStego().encode(data, str(enc), width=256, height=192, seed=5,
                      key=b"k", thumbnail="synthetic")
    out = tmp_path / "out.bin"
    n = DngStego().decode_to(str(enc), str(out), key=b"k")
    assert n == len(data)
    assert out.read_bytes() == data
    assert DngStego().decode(str(enc), key=b"k") == data
    # Wrong key: no output and no leftover .part file.
    bad = tmp_path / "bad.bin"
    with pytest.raises(ValueError):
        DngStego().decode_to(str(enc), str(bad), key=b"wrong")
    assert not bad.exists()
    assert not (tmp_path / "bad.bin.part").exists()


def test_decode_to_split_set(tmp_path):
    data = _payload(11000)
    infos = DngStego().encode_split(
        data, str(tmp_path / "s.dng"), 5000, width=256, height=192,
        seed=5, thumbnail="synthetic", split_id="setS")
    files = [i["path"] for i in infos]
    out = tmp_path / "whole.bin"
    n = DngStego().decode_to(files, str(out))
    assert n == len(data)
    assert out.read_bytes() == data


def test_encode_split_non_seekable_single_chunk(tmp_path):
    # Regression: the single-chunk shortcut must not re-read a spooled,
    # already-exhausted stream (that encoded an empty payload).
    data = _payload(3000)
    infos = DngStego().encode_split(
        _Pipe(data), str(tmp_path / "p.dng"), 5000, width=256, height=192,
        seed=5, thumbnail="synthetic")
    assert len(infos) == 1
    assert infos[0]["payload_len"] == 3000
    assert DngStego().decode(infos[0]["path"]) == data


def test_encode_split_non_seekable_multi_chunk(tmp_path):
    data = _payload(9000)
    infos = DngStego().encode_split(
        _Pipe(data), str(tmp_path / "m.dng"), 4000, width=256, height=192,
        seed=5, thumbnail="synthetic", split_id="pipe")
    assert [i["payload_len"] for i in infos] == [4000, 4000, 1000]
    assert DngStego().decode([i["path"] for i in infos]) == data


@pytest.mark.skipif(not hasattr(os, "mkfifo"), reason="POSIX FIFO only")
def test_cli_encode_from_fifo_path(tmp_path, capsys):
    # FIFO: st_size is 0, so the CLI/reader must spool instead of
    # trusting the size (previously the payload was silently dropped).
    import stegodng.cli as cli_mod
    data = _payload(2000)
    fifo = tmp_path / "payload.fifo"
    os.mkfifo(fifo)
    out = tmp_path / "fifo.dng"

    def writer():
        with open(fifo, "wb") as f:
            f.write(data)

    thread = threading.Thread(target=writer, daemon=True)
    thread.start()
    try:
        rc = cli_mod.main([
            "encode", "-i", str(fifo), "-o", str(out),
            "--width", "256", "--height", "192", "--seed", "5",
            "--thumbnail", "synthetic",
        ])
    finally:
        thread.join(timeout=10)
    assert not thread.is_alive()
    assert rc == 0
    assert DngStego().decode(str(out)) == data


def test_decode_to_split_late_failure_leaves_no_output(tmp_path, monkeypatch):
    # Chunk 1 decodes into the .part file; chunk 2 fails.  The temp file
    # and the final output must both be gone.
    data = _payload(9000)
    infos = DngStego().encode_split(
        data, str(tmp_path / "late.dng"), 4000, width=256, height=192,
        seed=5, thumbnail="synthetic", split_id="late")
    files = [i["path"] for i in infos]
    out = tmp_path / "late.bin"
    original = DngStego._decode_one
    calls = []

    def fail_second(self, path, *args, **kwargs):
        calls.append(path)
        if len(calls) == 2:
            raise ValueError("late failure")
        return original(self, path, *args, **kwargs)

    monkeypatch.setattr(DngStego, "_decode_one", fail_second)
    with pytest.raises(ValueError, match="late failure"):
        DngStego().decode_to(files, str(out))
    assert calls and len(calls) == 2
    assert not out.exists()
    assert not (tmp_path / "late.bin.part").exists()


def test_cli_encode_reads_path_not_bytes(tmp_path, monkeypatch):
    """The CLI must hand the path to the API, not a fully-read bytes blob."""
    import stegodng.cli as cli_mod
    src = tmp_path / "input.bin"
    src.write_bytes(_payload(2000))
    seen = {}

    def fake_encode(payload, output_path, **kwargs):
        seen["payload"] = payload
        # Emulate the real file_info contract just enough for the CLI.
        return {"path": output_path, "size": 1, "payload_len": 2000,
                "capacity": 4000, "bigtiff": False,
                "thumbnail": "synthetic",
                "metadata": {"datetime": "x", "iso": 100, "lens": "x",
                             "camera_serial": "x"},
                "debug_metadata_path": None}

    monkeypatch.setattr(cli_mod, "encode", fake_encode)
    assert cli_mod.main(["encode", "-i", str(src), "-o",
                         str(tmp_path / "o.dng"), "--seed", "5"]) == 0
    assert seen["payload"] == str(src)


def test_shim_exports_decode_to():
    assert stego_dng.decode_to is not None
    assert stego_dng.PayloadReader is PayloadReader
    assert stego_dng.FramedPayload is FramedPayload
    assert stego_dng.FrameSink is FrameSink
