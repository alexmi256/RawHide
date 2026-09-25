"""Extra coverage tests for areas missed by the main suite.

Hermetic: no network, thumbnail="synthetic" on every encode.
Covers codec/container/cover/framing/profile/sizing/split/stego/
thumbnails/shim edges plus in-process CLI (main) paths.
"""

import io
import os
import struct
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stego_dng
from stegodng import container as C
from stegodng.codec import LsbCodec, format_kb, format_kb_hi, format_kb_lo
from stegodng.framing import PayloadFrame


# ---------------------------------------------------------------- codec

def test_format_kb_variants():
    assert format_kb(1024) == "1.0 KB"
    assert "KB" in format_kb_hi(1500)
    assert "KB" in format_kb_lo(1500)
    # hi rounds up, lo rounds down: 1025 bytes = 1.0009 KB
    assert format_kb_hi(1025) == "1.1 KB"
    assert format_kb_lo(1025) == "1.0 KB"
    assert stego_dng._kb(2048) == format_kb(2048)
    assert stego_dng._kb_hi(2048) == format_kb_hi(2048)
    assert stego_dng._kb_lo(2048) == format_kb_lo(2048)


def test_codec_init_and_capacity():
    c = LsbCodec(lsb_planes=3)
    assert c.lsb_planes == 3
    assert c.capacity(800) == LsbCodec.capacity_bytes(800, 3)


def test_bits_for_range_empty():
    farr = np.frombuffer(b"\x00\xff", dtype=np.uint8)
    out = LsbCodec._bits_for_range(farr, 0, 0)
    assert out.size == 0


def test_embed_window_skips_empty_planes():
    cover = np.zeros(16, dtype=np.uint16)
    bits = np.array([1], dtype=np.uint8)  # planes 1,2 empty for lsb=3
    w = cover.astype(np.uint32)
    LsbCodec._embed_bits_into_window(w, bits, 3)
    assert int(w[0] & 1) == 1


def test_embed_bitarray_oversize():
    cover = np.zeros((4, 4, 3), dtype=np.uint16)
    with pytest.raises(ValueError, match="payload too large"):
        LsbCodec.embed_bitarray(cover, np.ones(cover.size + 1, dtype=np.uint8), 1)


def test_extract_bitarray_skips_empty_views():
    raw = np.ones((4, 4, 3), dtype=np.uint16) * 7
    bits = LsbCodec.extract_bitarray(raw, 3, 1)
    assert bits.shape == (1,)


def test_extract_bitarray_oversize_direct():
    raw = np.zeros((2, 2, 3), dtype=np.uint16)
    with pytest.raises(ValueError):
        LsbCodec.extract_bitarray(raw, 1, raw.size + 1)


def test_embed_bits_ok_and_oversize():
    from stegodng.codec import embed_bits as wb, extract_bits as rb
    cover = np.zeros((8, 8, 3), dtype=np.uint16)
    frame = b"\x01\x02\x03\x04"
    stego = LsbCodec.embed_bits(cover, frame, 1)
    assert rb(stego, 1, len(frame)) == frame
    assert wb(cover, frame, 1).shape == cover.shape
    with pytest.raises(ValueError, match="payload too large"):
        LsbCodec.embed_bits(cover, b"\xff" * 100000, 1)


def test_extract_stream_bad_total_bits():
    raw = np.zeros((4, 4, 3), dtype=np.uint16)
    with pytest.raises(ValueError, match="whole number of bytes"):
        LsbCodec.extract_stream([raw], 1, 7)


def test_extract_stream_pending_paths():
    # Tiny sample chunks force byte splits across iterations (pending).
    orig = LsbCodec._chunk_samples
    LsbCodec._chunk_samples = staticmethod(lambda p: 5)
    try:
        rng = np.random.default_rng(7)
        c1 = rng.integers(0, 65535, size=(8, 8, 3)).astype(np.uint16)
        payload = os.urandom(37)
        frame = PayloadFrame.pack(payload, None)
        stegos = LsbCodec.stripe_frames([c1.copy()], frame, 3)
        out = LsbCodec.extract_stream(stegos, 3, len(frame) * 8)
        assert PayloadFrame.unpack(out, None)[0] == payload
    finally:
        LsbCodec._chunk_samples = orig


def test_extract_bits_zero_and_wrappers():
    from stegodng.codec import (
        _embed_bitarray,
        _extract_bitarray,
        capacity_bytes_total,
    )
    assert LsbCodec.extract_bits(np.zeros(8, dtype=np.uint16), 1, 0) == b""
    assert stego_dng.extract_bits(np.zeros(8, dtype=np.uint16), 1, 0) == b""
    cover = np.zeros((8, 8, 3), dtype=np.uint16)
    bits = np.unpackbits(np.frombuffer(b"hi", dtype=np.uint8))
    stego = _embed_bitarray(cover, bits, 2)
    assert _extract_bitarray(stego, 2, 16).shape == (16,)
    assert capacity_bytes_total(100, 1, 2) == LsbCodec.capacity_bytes_total(100, 1, 2)
    assert stego_dng.capacity_bytes_total(100, 1, 2) == LsbCodec.capacity_bytes_total(100, 1, 2)
    assert stego_dng.embed_bits(cover, b"AB", 1).shape == cover.shape
    assert stego_dng.extract_bits(stego_dng.embed_bits(cover, b"AB", 1), 1, 2) == b"AB"


# ------------------------------------------------------------- container

def test_split_markers_unknown_fields(tmp_path):
    out = str(tmp_path / "m.dng")
    stego_dng.encode(b"x", out, width=64, height=48, seed=1, thumbnail="synthetic")
    cont = C.DngContainer(out)
    with pytest.raises(ValueError, match="unknown split id field"):
        cont.split_markers(id_field="Nope")
    with pytest.raises(ValueError, match="unknown split seq field"):
        cont.split_markers(seq_field="Nope")


def test_split_markers_bad_seq_wrapped(tmp_path, monkeypatch):
    out = str(tmp_path / "m2.dng")
    stego_dng.encode(b"x", out, width=64, height=48, seed=1, thumbnail="synthetic")
    import stegodng.split as sp
    def boom(field, raw):
        raise ValueError("bad seq")
    monkeypatch.setattr(sp, "parse_seq_value", boom)
    # Need a file that actually carries a seq marker so the parse path runs.
    from stegodng import DngStego
    infos = DngStego().encode_split(
        b"z" * 5000, str(tmp_path / "s.dng"), 2000, width=256, height=192,
        seed=1, thumbnail="synthetic")
    with pytest.raises(ValueError, match="bad seq"):
        C.DngContainer(infos[0]["path"]).split_markers()


def test_is_bigtiff_property(tmp_path):
    out = str(tmp_path / "s.dng")
    stego_dng.encode(b"x", out, width=64, height=48, seed=1, thumbnail="synthetic")
    assert C.DngContainer(out).is_bigtiff is False


def test_build_exif_block_wrapper(tmp_path):
    meta = stego_dng.randomize_metadata(1)
    blob = C.build_exif_block(meta, 64, 48, 1024)
    assert len(blob) > 0
    # Same as internal classic builder.
    assert blob == C._build_exif_block(meta, 64, 48, 1024, False)


def test_seek_helpers_bad_magic(tmp_path):
    p = str(tmp_path / "bad.bin")
    with open(p, "wb") as f:
        f.write(b"NOTIFF" + b"\x00" * 100)
    with open(p, "rb") as f:
        with pytest.raises(ValueError, match="little-endian TIFF"):
            C._seek_ifd_entry(f, 8, 271)
    with open(p, "rb") as f:
        with pytest.raises(ValueError, match="little-endian TIFF"):
            C._seek_ifd0_offset(f)


def test_append_exif_odd_offset_branch(tmp_path):
    import tifffile
    rng = np.random.default_rng(0)
    thumb = np.ascontiguousarray(rng.integers(0, 255, size=(48, 64, 3)).astype(np.uint8))
    raw = np.ascontiguousarray(rng.integers(0, 65535, size=(64, 80, 3)).astype(np.uint16))
    p = str(tmp_path / "odd.dng")
    with tifffile.TiffWriter(p, bigtiff=False) as tif:
        tif.write(thumb, photometric="ycbcr", compression="jpeg",
                  metadata=None, software="X", datetime="2020:11:26 12:17:12",
                  subfiletype=1, subifds=1,
                  extratags=[(271, "s", 0, "FUJIFILM", True),
                             (65000, 3, 1, (0,), True)])
        tif.write(raw, photometric="rgb", metadata=None, software=False,
                  bitspersample=16, subfiletype=0,
                  extratags=[(50714, 4, 3, (256, 256, 256), True),
                             (50717, 4, 3, (65535, 65535, 65535), True)])
    # Force odd EOF so the word-align pad branch runs.
    with open(p, "r+b") as f:
        f.seek(0, 2)
        if f.tell() % 2 == 0:
            f.write(b"\x00")
    C._append_exif(p, stego_dng.randomize_metadata(1), 64, 48)
    with tifffile.TiffFile(p) as tif:
        assert 34665 in tif.pages[0].tags


def test_raw_series_fallback_and_errors(tmp_path):
    import tifffile
    # Two plain RGB series, no LinearRaw/CFA photometric -> fallback series[1:].
    p = str(tmp_path / "plain2.tif")
    a = np.zeros((16, 16, 3), dtype=np.uint8)
    b = np.zeros((16, 16, 3), dtype=np.uint8) + 5
    with tifffile.TiffWriter(p) as tif:
        tif.write(a, photometric="rgb")
        tif.write(b, photometric="rgb")
    with tifffile.TiffFile(p) as tif:
        assert len(C._raw_series_all(tif)) >= 1
        assert C._raw_series(tif) is not None
    # Single series -> hard error.
    p1 = str(tmp_path / "plain1.tif")
    with tifffile.TiffWriter(p1) as tif:
        tif.write(a, photometric="rgb")
    with tifffile.TiffFile(p1) as tif:
        with pytest.raises(ValueError, match="no SubIFD"):
            C._raw_series_all(tif)


def test_exif_lookup_variants():
    assert C._exif_lookup({"ImageUniqueID": "u"}, 42016, "ImageUniqueID") == "u"
    assert C._exif_lookup({42016: "v"}, 42016, "ImageUniqueID") == "v"
    assert C._exif_lookup({}, 42016, "ImageUniqueID") is None


# ------------------------------------------------------------ cover/profile

def test_cover_bad_depth():
    from stegodng.cover import CoverGenerator
    with pytest.raises(ValueError, match="bit_depth"):
        CoverGenerator(1).cover(16, 16, "linear", 11)


def test_cover_wrappers():
    from stegodng.cover import make_cover, make_thumbnail
    assert make_cover(16, 24, 3, "linear", 16).shape == (16, 24, 3)
    assert make_thumbnail(16, 24, 3).shape == (16, 24, 3)


def test_profile_helpers():
    from stegodng.profile import CameraProfile
    assert CameraProfile.container_bits(8) == 8
    assert CameraProfile.container_bits(12) == 16
    assert CameraProfile().white_level(8) == 255
    assert CameraProfile().black_level(8) >= 1
    assert CameraProfile().top_planes(8) == 8


# ---------------------------------------------------------------- framing

def test_xor_empty():
    assert PayloadFrame._xor_data(b"", b"key") == b""


def test_unpack_errors():
    with pytest.raises(ValueError, match="too short"):
        PayloadFrame.unpack(b"short", None)
    # Bad version: craft header with version 99, unkeyed.
    import struct
    import zlib
    payload = b"abc"
    bad_ver = PayloadFrame.MAGIC + bytes((99, 0)) + struct.pack(">Q", 3) + struct.pack(">I", zlib.crc32(payload) & 0xFFFFFFFF) + payload
    with pytest.raises(ValueError, match="unsupported frame version"):
        PayloadFrame.unpack(bad_ver, None)
    # Truncated: header declares 3 bytes, stream shorter.
    good = PayloadFrame.pack(b"abc", None)
    with pytest.raises(ValueError, match="truncated"):
        PayloadFrame.unpack(good[:-1], None)
    # CRC mismatch: flip a body byte.
    tampered = bytearray(good)
    tampered[-1] ^= 0xFF
    with pytest.raises(ValueError, match="CRC32"):
        PayloadFrame.unpack(bytes(tampered), None)


# ------------------------------------------------------------------- split

def test_split_seq_format_parse():
    from stegodng.split import format_seq_value, parse_seq_value
    assert format_seq_value("PageNumber", 2, 5) == (2, 5)
    assert format_seq_value("ImageDescription", 2, 5) == "0002/0005"
    assert format_seq_value("ImageNumber", 2, 5) == 2
    assert parse_seq_value("PageNumber", (2, 5)) == (2, 5)
    assert parse_seq_value("ImageDescription", "0002/0005") == (2, 5)
    assert parse_seq_value("ImageNumber", 7) == (7, None)
    assert parse_seq_value("ImageNumber", (7,)) == (7, None)
    with pytest.raises(ValueError, match="PageNumber needs"):
        parse_seq_value("PageNumber", (1, 2, 3))
    with pytest.raises(ValueError, match="NNNN/MMMM"):
        parse_seq_value("ImageDescription", "bogus")


# ------------------------------------------------------------------ sizing

def test_sizing_validation():
    from stegodng.sizing import recommend
    with pytest.raises(ValueError, match="mode must be"):
        recommend(100, mode="bogus")
    with pytest.raises(ValueError, match="bit_depth"):
        recommend(100, bit_depth=11)
    with pytest.raises(ValueError, match="lsb_planes must be"):
        recommend(100, lsb_planes=0)
    with pytest.raises(ValueError, match="lsb_planes must be"):
        recommend(100, lsb_planes=17)
    with pytest.raises(ValueError, match="frames must be"):
        recommend(100, frames=0)
    with pytest.raises(ValueError, match="exceeds bit_depth"):
        recommend(100, bit_depth=8, lsb_planes=9)
    # One-sided geometry completes via 4:3.
    a = recommend(1000, width=800)
    assert a["height"] == round(800 * 3 / 4)
    assert "height" in a["auto"]
    b = recommend(1000, height=600)
    assert b["width"] == round(600 * 4 / 3)
    assert "width" in b["auto"]
    with pytest.raises(ValueError, match="positive"):
        recommend(100, width=-10, height=10)
    # Fixed dims + fixed planes that fit.
    c = recommend(100, width=512, height=384, lsb_planes=1)
    assert c["lsb_planes"] == 1 and c["preset"] is None
    # Fixed dims + fixed planes that overflow.
    with pytest.raises(ValueError, match="exceeds capacity"):
        recommend(10_000_000, width=64, height=48, lsb_planes=1)
    # Fixed dims, auto planes, still too big.
    with pytest.raises(ValueError, match="even with"):
        recommend(10_000_000, width=64, height=48)


def test_sizing_delegates_and_hints():
    from stegodng import AutoSizer
    from stegodng.sizing import _max_config_str, recommend
    assert AutoSizer.max_config("linear", 16) == _max_config_str("linear", 16, 1)
    cfg = {"lsb_planes": 2, "bit_depth": 16, "frames": 1}
    assert AutoSizer.risk_warnings(cfg, key=False) == []
    # Hint when fewer planes than max were requested.
    try:
        recommend(10**12, lsb_planes=2)
    except ValueError as exc:
        assert "with 16 LSB planes" in str(exc)
    # CFA hint mentions linear max.
    try:
        recommend(10**12, mode="cfa")
    except ValueError as exc:
        assert "linear mode max" in str(exc)
    # auto_size hint.
    try:
        recommend(10**12, auto_size=True)
    except ValueError as exc:
        assert "--auto-size already uses minimal dimensions" in str(exc)


def test_risk_warning_planes_branches():
    from stegodng.sizing import risk_warnings
    mid = risk_warnings({"lsb_planes": 6, "bit_depth": 16, "frames": 1}, key=True)
    assert any("heavily degrade" in w for w in mid)
    hi = risk_warnings({"lsb_planes": 10, "bit_depth": 16, "frames": 1}, key=True)
    assert any("destroy most" in w for w in hi)
    full = risk_warnings({"lsb_planes": 16, "bit_depth": 16, "frames": 1}, key=True)
    assert any("no cover" in w for w in full)


# ------------------------------------------------------------------- stego

def test_encode_default_seed(tmp_path):
    out = str(tmp_path / "noseed.dng")
    info = stego_dng.encode(b"hi-default-seed", out, thumbnail="synthetic")
    assert info["payload_len"] == len(b"hi-default-seed")
    assert stego_dng.decode(out) == b"hi-default-seed"


def test_validate_options_branches(tmp_path):
    with pytest.raises(ValueError, match="bit_depth"):
        stego_dng.encode(b"x", str(tmp_path / "a.dng"), bit_depth=11, thumbnail="synthetic")
    with pytest.raises(ValueError, match="mode must be"):
        stego_dng.encode(b"x", str(tmp_path / "b.dng"), mode="bogus", thumbnail="synthetic")
    with pytest.raises(ValueError, match="compression must be"):
        stego_dng.encode(b"x", str(tmp_path / "c.dng"), compression="lzw", thumbnail="synthetic")


def test_encode_split_id_validation(tmp_path):
    from stegodng import DngStego
    with pytest.raises(ValueError, match="non-empty string"):
        DngStego().encode_split(b"x", str(tmp_path / "a.dng"), 10, split_id="", thumbnail="synthetic")
    with pytest.raises(ValueError, match="ASCII"):
        DngStego().encode_split(b"x", str(tmp_path / "b.dng"), 10, split_id="caf\xc3\xa9", thumbnail="synthetic")


def test_encode_split_chunk_too_big(tmp_path):
    from stegodng import DngStego
    with pytest.raises(ValueError, match="exceeds per-file capacity"):
        DngStego().encode_split(
            b"z" * 50000, str(tmp_path / "big.dng"), 25000,
            width=64, height=48, seed=1, thumbnail="synthetic")


def test_encode_split_ifd0_fields(tmp_path):
    import tifffile
    from stegodng import DngStego
    infos = DngStego().encode_split(
        b"z" * 20000, str(tmp_path / "ifd0.dng"), 8000,
        width=256, height=192, seed=3, thumbnail="synthetic",
        split_id_field="ImageDescription", split_seq_field="PageNumber",
        split_id="ifd0set")
    assert len(infos) == 3
    with tifffile.TiffFile(infos[0]["path"]) as tif:
        assert tif.pages[0].tags[270].value == "ifd0set"
        assert tuple(tif.pages[0].tags[297].value) == (1, 3)
    assert DngStego().decode(
        [i["path"] for i in infos],
        split_id_field="ImageDescription",
        split_seq_field="PageNumber") == b"z" * 20000


def test_write_split_tags_int_wrap(tmp_path):
    # Line 437 (val,) wrap runs only for IFD0-bound single-int fields.
    # No shipped registry hits it, so drive it directly: reserve one
    # dummy via _write_container, then call with a faked int seq value.
    from stegodng import DngStego
    from stegodng.codec import LsbCodec
    from stegodng.cover import CoverGenerator
    from stegodng.framing import PayloadFrame
    from stegodng.metadata import MetadataRandomizer
    from stegodng.thumbnails import ThumbnailProvider
    import tifffile
    stego = DngStego()
    out = str(tmp_path / "wrap.dng")
    width, height = 256, 192
    covers = [CoverGenerator(1).cover(height, width, "linear", 16)]
    stegos = LsbCodec.stripe_frames(covers, PayloadFrame.pack(b"x", None), 1)
    meta = MetadataRandomizer(1).randomize()
    thumb, _ = ThumbnailProvider(seed=1).get(256, 192, source="synthetic")
    stego._write_container(out, stegos=stegos, thumb_rgb=thumb, meta=meta,
                           width=width, height=height, mode="linear",
                           bit_depth=16, compression="none", frames=1,
                           tw=256, th=192, ifd0_dummies=1)
    import stegodng.stego as stego_mod
    orig = stego_mod.format_seq_value
    stego_mod.format_seq_value = lambda f, s, t: 7
    try:
        DngStego._write_split_tags(out, None,
                                    {"tag": 297, "dtype": "SHORT", "ifd": "ifd0"},
                                    "none", "PageNumber", "uid", 1, 1)
    finally:
        stego_mod.format_seq_value = orig
    with tifffile.TiffFile(out) as tif:
        assert 297 in tif.pages[0].tags


def test_decode_with_planes_capacity_error():
    from stegodng import DngStego
    # Header declaring a 1 GB payload on a tiny cover -> capacity error.
    import struct
    import zlib
    pay_len = 1024 ** 3
    hdr = (PayloadFrame.MAGIC + bytes((1, 0)) + struct.pack(">Q", pay_len)
           + struct.pack(">I", zlib.crc32(b"") & 0xFFFFFFFF))
    # Build a raw that at least holds the header.
    big = np.zeros((64, 64, 3), dtype=np.uint16)
    bits = np.unpackbits(np.frombuffer(hdr, dtype=np.uint8))
    stego = LsbCodec.embed_bitarray(big, bits, 1)
    with pytest.raises(ValueError, match="exceeds image capacity"):
        DngStego._decode_with_planes([stego], None, 1)


def test_decode_validation(tmp_path):
    from stegodng import DngStego
    out = str(tmp_path / "v.dng")
    stego_dng.encode(b"x", out, width=64, height=48, seed=1, thumbnail="synthetic")
    with pytest.raises(ValueError, match="lsb_planes"):
        DngStego().decode(out, lsb_planes=99)
    with pytest.raises(ValueError, match="no input files"):
        DngStego().decode([])
    with pytest.raises(ValueError, match="lsb_planes"):
        DngStego()._decode_one(out, lsb_planes=0)


def test_decode_both_none_orders_by_name(tmp_path):
    # Both split fields "none": _decode_many skips markers entirely.
    from stegodng import DngStego
    payload = os.urandom(9000)
    infos = DngStego().encode_split(
        payload, str(tmp_path / "bothnone.dng"), 3000, width=256, height=192,
        seed=1, thumbnail="synthetic", split_id_field="none",
        split_seq_field="none", split_id="x")
    files = [i["path"] for i in infos]
    assert DngStego().decode(files, split_id_field="none",
                              split_seq_field="none") == payload


def test_extract_stream_empty_view_branch():
    # planes=16, tiny chunks: a remainder of 8 bits leaves planes 8-15
    # with empty views in the final iteration.
    orig = LsbCodec._chunk_samples
    LsbCodec._chunk_samples = staticmethod(lambda p: 5)
    try:
        rng = np.random.default_rng(9)
        c1 = rng.integers(0, 65535, size=(32, 32, 3)).astype(np.uint16)
        payload = os.urandom(33)  # (18+33)*8 % 80 == 8
        frame = PayloadFrame.pack(payload, None)
        assert (len(frame) * 8) % 80 == 8
        stegos = LsbCodec.stripe_frames([c1.copy()], frame, 16)
        out = LsbCodec.extract_stream(stegos, 16, len(frame) * 8)
        assert PayloadFrame.unpack(out, None)[0] == payload
    finally:
        LsbCodec._chunk_samples = orig


def test_decode_many_markers_error_wrapped(tmp_path, monkeypatch):
    from stegodng import DngStego
    payload = os.urandom(8000)
    infos = DngStego().encode_split(
        payload, str(tmp_path / "m.dng"), 3000, width=256, height=192,
        seed=1, thumbnail="synthetic")
    files = [i["path"] for i in infos]
    orig = C.DngContainer.split_markers
    def boom(self, id_field="ImageUniqueID", seq_field="ImageNumber"):
        raise ValueError("marker boom")
    monkeypatch.setattr(C.DngContainer, "split_markers", boom)
    with pytest.raises(ValueError, match="marker boom"):
        DngStego().decode(files)


def test_decode_many_id_only_orders_by_name(tmp_path):
    from stegodng import DngStego
    payload = os.urandom(12000)
    infos = DngStego().encode_split(
        payload, str(tmp_path / "idonly.dng"), 5000, width=256, height=192,
        seed=4, thumbnail="synthetic", split_seq_field="none",
        split_id="idonlyset")
    files = [i["path"] for i in infos]
    assert DngStego().decode(files, split_seq_field="none") == payload


def test_decode_many_single_file_error_wrapped(tmp_path):
    from stegodng import DngStego
    out = str(tmp_path / "k.dng")
    stego_dng.encode(b"secret", out, width=256, height=192, seed=1,
                     key=b"k1", thumbnail="synthetic")
    infos = DngStego().encode_split(
        b"z" * 8000, str(tmp_path / "kk.dng"), 3000, width=256, height=192,
        seed=1, thumbnail="synthetic", key=b"k1")
    files = [i["path"] for i in infos]
    # Wrong key on a chunk set wraps the per-file error with the path.
    with pytest.raises(ValueError, match=r"kk0001.*magic|magic.*kk0001"):
        DngStego().decode(files, key=b"wrong")


def test_order_by_markers_errors():
    from stegodng import DngStego
    paths = ["a0001.dng", "a0002.dng"]
    # Different UUIDs.
    m = [{"id": "u1", "seq": 1, "total": None},
         {"id": "u2", "seq": 2, "total": None}]
    with pytest.raises(ValueError, match="different sets"):
        DngStego._order_by_markers(paths, m, True, True)
    # Duplicate seqs.
    m2 = [{"id": "u", "seq": 1, "total": None},
          {"id": "u", "seq": 1, "total": None}]
    with pytest.raises(ValueError, match="duplicate chunk numbers"):
        DngStego._order_by_markers(paths, m2, True, True)
    # Conflicting totals.
    m3 = [{"id": "u", "seq": 1, "total": 2},
          {"id": "u", "seq": 2, "total": 3}]
    with pytest.raises(ValueError, match="conflicting chunk totals"):
        DngStego._order_by_markers(paths, m3, True, True)


def test_order_by_names_errors(tmp_path):
    import glob
    from stegodng import DngStego
    from stegodng.stego import DngStego as DS
    # Mixed stems via none/none split then rename to different stems.
    payload = os.urandom(9000)
    infos = DngStego().encode_split(
        payload, str(tmp_path / "mix.dng"), 3000, width=256, height=192,
        seed=1, thumbnail="synthetic", split_id_field="none",
        split_seq_field="none", split_id="x")
    files = [i["path"] for i in infos]
    other = str(tmp_path / "other0001.dng")
    import shutil
    shutil.copy(files[0], other)
    with pytest.raises(ValueError, match="mix stems"):
        DS._order_by_names([files[0], other])
    # Duplicate numbers.
    with pytest.raises(ValueError, match="duplicate chunk numbers"):
        DS._order_by_names([files[0], files[0]])
    # Starts late.
    with pytest.raises(ValueError, match="not 0001"):
        DS._order_by_names(files[1:])
    # Gap.
    payload2 = os.urandom(12000)
    infos2 = DngStego().encode_split(
        payload2, str(tmp_path / "gap.dng"), 3000, width=256, height=192,
        seed=2, thumbnail="synthetic", split_id_field="none",
        split_seq_field="none", split_id="y")
    gfiles = [i["path"] for i in infos2]
    assert len(gfiles) >= 3
    with pytest.raises(ValueError, match="not consecutive"):
        DS._order_by_names([gfiles[0], gfiles[2]])


def test_module_wrappers(tmp_path):
    import stegodng.stego as sm
    out = str(tmp_path / "w.dng")
    info = sm.encode(b"wrap", out, width=64, height=48, seed=1, thumbnail="synthetic")
    assert sm.decode(out) == b"wrap"
    infos = sm.encode_split(b"z" * 4000, str(tmp_path / "ws.dng"), 1500,
                            width=256, height=192, seed=1, thumbnail="synthetic")
    assert len(infos) == 3
    assert sm.decode([i["path"] for i in infos]) == b"z" * 4000
    t = sm.generate_tiff(str(tmp_path / "w.tif"), width=32, height=24, seed=1)
    assert t.endswith(".tif")


# --------------------------------------------------------------- thumbnails

def test_thumbnail_unexpected_redirect():
    from stegodng.thumbnails import ThumbnailProvider
    def opener(url, timeout):
        if url == ThumbnailProvider.RANDOM_URL:
            return ("https://commons.wikimedia.org/wiki/Main_Page", b"x")
        raise AssertionError(url)
    arr, label = ThumbnailProvider(seed=1, max_attempts=1, opener=opener).get(64, 48, source="random")
    assert label == "synthetic-noise-fallback"
    assert arr.shape == (48, 64, 3)


def test_thumbnail_empty_download():
    from stegodng.thumbnails import ThumbnailProvider
    photo = b"tiny"
    def opener(url, timeout):
        if url == ThumbnailProvider.RANDOM_URL:
            return ("https://commons.wikimedia.org/wiki/File:Meadow.png", b"page")
        if url.startswith(ThumbnailProvider.FILEPATH_URL.format("")):
            return ("https://upload.wikimedia.org/x", b"short")
        raise AssertionError(url)
    arr, label = ThumbnailProvider(seed=1, max_attempts=1, opener=opener).get(64, 48, source="random")
    assert label == "synthetic-noise-fallback"


def test_prepare_reraises_thumbnail_error(monkeypatch):
    from stegodng.thumbnails import ThumbnailError, prepare
    from PIL import Image
    def boom(*a, **k):
        raise ThumbnailError("inner")
    monkeypatch.setattr(Image, "open", boom)
    with pytest.raises(ThumbnailError, match="inner"):
        prepare(b"whatever", 64, 48)


# --------------------------------------------------------------------- shim

def test_shim_wrappers():
    import random
    rng = random.Random(0)
    assert stego_dng.pack_frame(b"ab", 1, None) == PayloadFrame.pack(b"ab", None)
    assert stego_dng.unpack_frame(stego_dng.pack_frame(b"ab", 1, None), 1, None)[0] == b"ab"
    assert stego_dng._keystream(b"k", 10) == PayloadFrame._keystream(b"k", 10)
    s1 = stego_dng._rand_serial(rng, "AB")
    assert s1.startswith("AB") and len(s1) == 8
    raw = np.zeros((16, 16, 3), dtype=np.uint16)
    frame = PayloadFrame.pack(b"hi", None)
    stego = LsbCodec.embed_bits(raw, frame, 1)
    assert stego_dng._decode_with_planes(stego, None, 1) == b"hi"
