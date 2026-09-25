"""P0 memory fixes: in-place striping + lazy split chunking.

Hermetic: no network, thumbnail="synthetic" on every encode.
"""

import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stego_dng
from stegodng import DngStego
from stegodng.codec import LsbCodec
from stegodng.cover import CoverGenerator
from stegodng.framing import PayloadFrame
from stegodng.split import iter_chunk_bounds


def _covers():
    rng = np.random.default_rng(1234)
    c1 = rng.integers(0, 65535, size=(64, 64, 3)).astype(np.uint16)
    c2 = rng.integers(0, 65535, size=(48, 48, 3)).astype(np.uint16)
    return c1, c2


def test_stripe_frames_embeds_in_place():
    # Returned arrays are the same objects (same buffers): no second
    # full-frame copy beside the covers.
    c1, c2 = _covers()
    before = c1.copy()
    payload = os.urandom(1000)
    frame = PayloadFrame.pack(payload, None)
    stegos = LsbCodec.stripe_frames([c1, c2], frame, 2)
    assert stegos[0] is c1 and stegos[1] is c2
    assert not np.array_equal(c1, before)  # cover was mutated
    out = LsbCodec.extract_stream(stegos, 2, len(frame) * 8)
    assert PayloadFrame.unpack(out, None)[0] == payload


def test_stripe_frames_in_place_spills_across_frames_keyed():
    # Multi-frame striping + keyed framing keep identical bit mapping.
    c1, c2 = _covers()
    cap = (LsbCodec.capacity_bytes_total(c1.size, 1, 1)
           + LsbCodec.capacity_bytes_total(c2.size, 1, 1)
           + PayloadFrame.HEADER_LEN)
    payload = os.urandom(min(2000, cap))
    frame = PayloadFrame.pack(payload, b"chunk-key")
    stegos = LsbCodec.stripe_frames([c1, c2], frame, 1)
    assert stegos[0] is c1 and stegos[1] is c2
    out = LsbCodec.extract_stream(stegos, 1, len(frame) * 8)
    assert PayloadFrame.unpack(out, b"chunk-key")[0] == payload


def test_stripe_frames_noncontiguous_falls_back_to_copy():
    rng = np.random.default_rng(9)
    base = rng.integers(0, 65535, size=(64, 64, 3)).astype(np.uint16)
    snap = base.copy()
    nc = base.transpose(1, 0, 2)  # view, not C-contiguous
    assert not nc.flags["C_CONTIGUOUS"]
    payload = os.urandom(500)
    frame = PayloadFrame.pack(payload, None)
    stegos = LsbCodec.stripe_frames([nc], frame, 1)
    # Roundtrip works and the result is a fresh contiguous array;
    # the caller's buffer is untouched (copy fallback).
    assert stegos[0].flags["C_CONTIGUOUS"]
    assert np.array_equal(base, snap)
    out = LsbCodec.extract_stream(stegos, 1, len(frame) * 8)
    assert PayloadFrame.unpack(out, None)[0] == payload


def test_embed_bits_shares_cover_buffer():
    cover = CoverGenerator(3).cover(32, 48, "linear", 16)
    stego = LsbCodec.embed_bits(cover, b"\x01\x02\x03\x04", 1)
    assert np.shares_memory(stego, cover)


def test_iter_chunk_bounds():
    assert list(iter_chunk_bounds(60000, 20000)) == [
        (1, 3, 0, 20000), (2, 3, 20000, 40000), (3, 3, 40000, 60000)]
    # Exact multiple: no empty tail chunk.
    assert list(iter_chunk_bounds(40000, 20000)) == [
        (1, 2, 0, 20000), (2, 2, 20000, 40000)]
    # Remainder.
    assert list(iter_chunk_bounds(45000, 20000)) == [
        (1, 3, 0, 20000), (2, 3, 20000, 40000), (3, 3, 40000, 45000)]
    # Empty payload still yields one (empty) chunk; tiny payload one chunk.
    assert list(iter_chunk_bounds(0, 20000)) == [(1, 1, 0, 0)]
    assert list(iter_chunk_bounds(100, 100000)) == [(1, 1, 0, 100)]
    # Bounds reconstruct the payload.
    data = os.urandom(5000)
    assert b"".join(data[s:e] for _, _, s, e in
                    iter_chunk_bounds(len(data), 2000)) == data


def test_iter_chunk_bounds_rejects_bad_split_size():
    import pytest
    for bad in (0, -1, -20000, True, False, 2.5, "20k"):
        with pytest.raises(ValueError, match="positive byte count"):
            list(iter_chunk_bounds(60000, bad))


class _SliceLogger:
    """bytes-like payload recording every slice request."""

    def __init__(self, data: bytes):
        self._data = data
        self.events: list[tuple] = []

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return True

    def __getitem__(self, s):
        assert isinstance(s, slice)
        self.events.append(("slice", s.start, s.stop))
        return self._data[s]


def test_encode_split_slices_one_chunk_at_a_time(tmp_path, monkeypatch):
    # Laziness is behavioral: slice/write events must interleave
    # (slice1, write1, slice2, ...) instead of slicing everything
    # up front (slice1, slice2, ..., write1, ...).
    data = os.urandom(60000)
    logged: list[tuple] = []

    def fake_write(self, path, **kw):
        logged.append(("write", path))
        with open(path, "wb") as f:
            f.write(b"x")
        return False

    monkeypatch.setattr(DngStego, "_write_container", fake_write)
    monkeypatch.setattr(DngStego, "_write_split_tags",
                        staticmethod(lambda *a, **k: logged.append(("tags",)) or None))

    payload = _SliceLogger(data)
    out = str(tmp_path / "lz.dng")
    infos = DngStego().encode_split(
        payload, out, 20000, width=512, height=384, seed=5,
        thumbnail="synthetic", split_id="lazytest")
    assert [i["chunk_seq"] for i in infos] == [1, 2, 3]
    assert [i["payload_len"] for i in infos] == [20000, 20000, 20000]
    # Chunk bytes seen by pack() reassemble the payload in order.
    assert payload.events == [("slice", 0, 20000), ("slice", 20000, 40000),
                              ("slice", 40000, 60000)]
    order = [e[0] for e in logged]
    assert order == ["write", "tags"] * 3


def test_encode_split_slice_write_interleaving(tmp_path, monkeypatch):
    # Companion to the above: a single shared event log proves each
    # chunk is sliced just before its file is written.
    data = os.urandom(45000)
    events: list[str] = []

    class LoggingPayload(_SliceLogger):
        def __getitem__(self, s):
            events.append("slice")
            return super().__getitem__(s)

    def fake_write(self, path, **kw):
        events.append("write")
        with open(path, "wb") as f:
            f.write(b"x")
        return False

    monkeypatch.setattr(DngStego, "_write_container", fake_write)
    monkeypatch.setattr(DngStego, "_write_split_tags",
                        staticmethod(lambda *a, **k: None))

    infos = DngStego().encode_split(
        LoggingPayload(data), str(tmp_path / "lz2.dng"), 20000,
        width=512, height=384, seed=5, thumbnail="synthetic",
        split_id="lazytest2")
    assert [i["payload_len"] for i in infos] == [20000, 20000, 5000]
    assert events == ["slice", "write"] * 3


def test_encode_split_empty_and_exact_multiple(tmp_path):
    # Empty payload: single plain file, no split markers.
    infos = DngStego().encode_split(
        b"", str(tmp_path / "empty.dng"), 20000, width=256, height=192,
        seed=5, thumbnail="synthetic")
    assert len(infos) == 1 and "chunk_seq" not in infos[0]
    assert DngStego().decode(infos[0]["path"]) == b""
    # Exact multiple: two full chunks, no empty tail.
    payload = os.urandom(40000)
    infos = DngStego().encode_split(
        payload, str(tmp_path / "exact.dng"), 20000, width=512, height=384,
        seed=5, thumbnail="synthetic", split_id="exactset")
    assert len(infos) == 2
    assert [i["payload_len"] for i in infos] == [20000, 20000]
    files = [i["path"] for i in infos]
    assert DngStego().decode(files) == payload


def test_encode_byte_stable(tmp_path):
    # P0 changed buffering, not bits: fixed inputs give byte-identical
    # raw rasters and identical non-offset tags.
    # raw rasters and identical non-offset tags.
    import tifffile
    payload = os.urandom(3000)
    a = str(tmp_path / "a.dng")
    b = str(tmp_path / "b.dng")
    kw = dict(width=256, height=192, seed=7, lsb_planes=2,
              thumbnail="synthetic")
    stego_dng.encode(payload, a, **kw)
    stego_dng.encode(payload, b, **kw)
    assert DngStego().decode(a) == DngStego().decode(b) == payload
    SKIP = {273, 279, 324, 325, 330, 34665}  # offsets legitimately shift
    with tifffile.TiffFile(a) as ta, tifffile.TiffFile(b) as tb:
        ra, rb = ta.series[-1].asarray(), tb.series[-1].asarray()
        assert np.array_equal(ra, rb)
        tags_a = {t.code: t.value for t in ta.pages[0].tags.values()
                  if t.code not in SKIP}
        tags_b = {t.code: t.value for t in tb.pages[0].tags.values()
                  if t.code not in SKIP}
        assert tags_a.keys() == tags_b.keys()
        for code in tags_a:
            va, vb = tags_a[code], tags_b[code]
            assert str(va) == str(vb), code


def test_stripe_bit_mapping_golden_vector(tmp_path):
    # Pins the exact bit mapping against pre-P0 output: the hash below
    # was verified byte-identical to code before the in-place change,
    # so any plane/sample ordering change fails here (a same-version
    # self-comparison would not catch it).
    import hashlib
    from stegodng.container import DngContainer
    payload = bytes(range(256)) * 16
    out = str(tmp_path / "golden.dng")
    stego_dng.encode(payload, out, width=256, height=192, seed=7,
                     lsb_planes=2, thumbnail="synthetic")
    raw = DngContainer(out).raw_frames()[0]
    assert raw.shape == (192, 256, 3) and str(raw.dtype) == "uint16"
    assert (hashlib.sha256(raw.tobytes()).hexdigest()
            == "6df71f26ef5ec5a80762fc668ab1249e284282cecd4e8ee95eeaeb4dc6c7d627")
    assert (int(raw.flat[0]), int(raw.flat[1]), int(raw.flat[1000]),
            int(raw.flat[100000]), int(raw.flat[-1])) == (
                7002, 7024, 6891, 9064, 8818)
    assert DngStego().decode(out) == payload


def test_encode_split_chunk_seeds_match_manual_encode(tmp_path):
    # Each chunk must embed exactly as encode(chunk, seed=base+seq-1).
    from stegodng.container import DngContainer
    payload = os.urandom(45000)
    seed = 5
    kw = dict(width=512, height=384, thumbnail="synthetic")
    infos = DngStego().encode_split(
        payload, str(tmp_path / "sd.dng"), 20000, seed=seed,
        split_id="seedset", **kw)
    assert [i["payload_len"] for i in infos] == [20000, 20000, 5000]
    for seq, info in enumerate(infos, start=1):
        chunk = payload[(seq - 1) * 20000:seq * 20000]
        manual = str(tmp_path / f"m{seq}.dng")
        DngStego().encode(chunk, manual, seed=seed + seq - 1, **kw)
        a = DngContainer(info["path"]).raw_frames()[0]
        b = DngContainer(manual).raw_frames()[0]
        assert np.array_equal(a, b), f"chunk {seq} raster differs"
        assert DngStego().decode(info["path"]) == chunk


def test_encode_split_no_randomize_chunk1_matches_manual(tmp_path):
    # seed=None + no_randomize pins chunk 1 to base seed 0.
    from stegodng.container import DngContainer
    payload = os.urandom(25000)
    kw = dict(width=512, height=384, thumbnail="synthetic")
    infos = DngStego().encode_split(
        payload, str(tmp_path / "nr.dng"), 20000, seed=None,
        no_randomize=True, split_id="nrset", **kw)
    assert [i["payload_len"] for i in infos] == [20000, 5000]
    manual = str(tmp_path / "nr_manual.dng")
    DngStego().encode(payload[:20000], manual, seed=0,
                      no_randomize=True, **kw)
    a = DngContainer(infos[0]["path"]).raw_frames()[0]
    b = DngContainer(manual).raw_frames()[0]
    assert np.array_equal(a, b)
