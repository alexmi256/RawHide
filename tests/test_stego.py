"""Roundtrip tests for stego_dng (no sample images required)."""

import io
import os
import sys
import tempfile
from urllib.error import URLError

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stego_dng
from stegodng.thumbnails import ThumbnailError, ThumbnailProvider


def _tmp(name):
    return os.path.join(tempfile.mkdtemp(), name)


def test_linear_roundtrip():
    payload = os.urandom(4096)
    out = _tmp("linear.dng")
    info = stego_dng.encode(payload, out, width=512, height=384, seed=11,
                            thumbnail="synthetic")
    assert info["payload_len"] == len(payload)
    assert stego_dng.decode(out) == payload


def test_cfa_keyed_roundtrip():
    payload = b"hello raw world" * 10
    out = _tmp("cfa.dng")
    stego_dng.encode(
        payload, out, width=320, height=240, seed=12, mode="cfa",
        key=b"passphrase",
    thumbnail="synthetic",
    )
    assert stego_dng.decode(out, key=b"passphrase") == payload


def test_wrong_key_fails():
    out = _tmp("keyed.dng")
    stego_dng.encode(b"secret", out, width=320, height=240, seed=13,
                     key=b"right", thumbnail="synthetic")
    try:
        stego_dng.decode(out, key=b"wrong")
    except ValueError:
        pass
    else:
        raise AssertionError("decode with wrong key should fail")


def test_two_planes_14bit():
    payload = os.urandom(20000)
    out = _tmp("p14.dng")
    stego_dng.encode(payload, out, width=512, height=384, seed=14,
                     lsb_planes=2, bit_depth=14, thumbnail="synthetic")
    assert stego_dng.decode(out, lsb_planes=2) == payload


def test_all_bit_depths_roundtrip():
    payload = os.urandom(2048)
    for bit_depth in stego_dng.SUPPORTED_BIT_DEPTHS:
        for mode in ("linear", "cfa"):
            out = _tmp(f"bd{bit_depth}_{mode}.dng")
            info = stego_dng.encode(
                payload, out, width=512, height=384, seed=21,
                bit_depth=bit_depth, mode=mode,
            thumbnail="synthetic",
            )
            assert info["bit_depth"] == bit_depth, (bit_depth, mode)
            assert stego_dng.decode(out) == payload, (bit_depth, mode)


def test_packed_bps_and_levels():
    import tifffile
    out = _tmp("bps12.dng")
    stego_dng.encode(b"z" * 100, out, width=256, height=192, seed=22,
                     bit_depth=12, thumbnail="synthetic")
    with tifffile.TiffFile(out) as tif:
        raw_pg = [s for s in tif.series
                  if int(s.keyframe.photometric) in (34892, 32803)][0].keyframe
        bps = raw_pg.bitspersample
        bps = tuple(bps) if isinstance(bps, tuple) else (bps,) * 3
        assert bps == (12, 12, 12), raw_pg.bitspersample
        assert tuple(raw_pg.tags[50717].value) == (4095, 4095, 4095)
        assert tuple(raw_pg.tags[50714].value) == (16, 16, 16)


def test_four_planes_roundtrip():
    payload = os.urandom(30000)
    out = _tmp("p4.dng")
    stego_dng.encode(payload, out, width=512, height=384, seed=23,
                     lsb_planes=4, thumbnail="synthetic")
    assert stego_dng.decode(out, lsb_planes=4) == payload


def test_packed_depth_rejects_deflate():
    try:
        stego_dng.encode(b"z" * 100, _tmp("bad.dng"), width=256,
                         height=192, seed=24, bit_depth=12,
                         compression="adobe_deflate", thumbnail="synthetic")
    except ValueError:
        pass
    else:
        raise AssertionError("packed depth + deflate should be rejected")


def test_metadata_differs_per_seed():
    p = b"x"
    a = _tmp("a.dng")
    b = _tmp("b.dng")
    ia = stego_dng.encode(p, a, width=256, height=192, seed=1, thumbnail="synthetic")
    ib = stego_dng.encode(p, b, width=256, height=192, seed=2, thumbnail="synthetic")
    assert ia["metadata"]["datetime"] != ib["metadata"]["datetime"]
    assert ia["metadata"]["camera_serial"] != ib["metadata"]["camera_serial"]


def test_capacity():
    n = 1024 * 768 * 3
    assert stego_dng.capacity_bytes(n, 1) == n // 8 - stego_dng.HEADER_LEN


def test_oversize_rejected():
    try:
        stego_dng.encode(b"y" * 100000, _tmp("big.dng"),
                         width=64, height=64, seed=1, thumbnail="synthetic")
    except ValueError:
        pass
    else:
        raise AssertionError("oversize payload should be rejected")


def test_auto_config_defaults():
    cfg = stego_dng.recommend_config(1000)
    assert (cfg["width"], cfg["height"]) == (2048, 1536)
    assert cfg["lsb_planes"] == 1 and cfg["mode"] == "linear"
    assert cfg["bit_depth"] == 16
    assert set(cfg["auto"]) == {"mode", "bit_depth", "width", "height",
                                "lsb_planes"}


def test_auto_config_grows_geometry():
    # 5 MB fits the smallest preset once planes may exceed 4
    cfg = stego_dng.recommend_config(5_000_000)
    assert (cfg["width"], cfg["height"], cfg["lsb_planes"]) == (2048, 1536, 5)
    # beyond demo @16 planes (18.9 MB) the geometry must grow
    cfg = stego_dng.recommend_config(20_000_000)
    assert (cfg["width"], cfg["height"], cfg["lsb_planes"]) == (4000, 3000, 5)


def test_auto_config_fixed_dims_bumps_planes():
    cfg = stego_dng.recommend_config(2_000_000, width=2048, height=1536)
    assert cfg["lsb_planes"] == 2
    assert "width" not in cfg["auto"] and "lsb_planes" in cfg["auto"]


def test_auto_config_too_big_reports_max():
    mx = stego_dng.capacity_bytes(23296 * 17472 * 3,
                                    stego_dng.MAX_LSB_PLANES)
    try:
        stego_dng.recommend_config(mx + 1)
    except ValueError as exc:
        assert stego_dng._kb_lo(mx) in str(exc) and "KB" in str(exc)
        assert "bytes" not in str(exc) and "Split the input" in str(exc)
    else:
        raise AssertionError("oversize auto-config should fail")


def test_decode_autodetects_planes():
    payload = os.urandom(20000)
    out = _tmp("autodet.dng")
    stego_dng.encode(payload, out, width=512, height=384, seed=31,
                     lsb_planes=3, thumbnail="synthetic")
    assert stego_dng.decode(out) == payload  # no planes given
    assert stego_dng.decode(out, lsb_planes=3) == payload  # strict
    try:
        stego_dng.decode(out, lsb_planes=1)
    except ValueError:
        pass
    else:
        raise AssertionError("strict wrong-plane decode should fail")


def test_cli_auto_encode_roundtrip():
    import subprocess
    d = tempfile.mkdtemp()
    src_p = os.path.join(d, "in.bin")
    enc = os.path.join(d, "auto.dng")
    rec = os.path.join(d, "out.bin")
    with open(src_p, "wb") as f:
        f.write(os.urandom(3000))
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "encode", "-i", src_p, "-o", enc,
         "--seed", "5", "--thumbnail", "synthetic"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "auto-config" in r.stdout
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "decode", "-i", enc, "-o", rec],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    with open(src_p, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()


def test_auto_size_exact_fit():
    cfg = stego_dng.recommend_config(60000, auto_size=True)
    assert cfg["preset"] == "auto-size" and cfg["lsb_planes"] == 1
    assert cfg["width"] % 2 == 0 and cfg["height"] % 2 == 0
    assert abs(cfg["width"] / cfg["height"] - 4 / 3) < 0.05
    n = cfg["width"] * cfg["height"] * 3
    assert stego_dng.capacity_bytes(n, 1) >= 60000
    # minimal: shrinking either side (keeping even) must not fit
    w, h = cfg["width"], cfg["height"]
    assert (stego_dng.capacity_bytes((w - 2) * h * 3, 1) < 60000
            or stego_dng.capacity_bytes(w * (h - 2) * 3, 1) < 60000)


def test_auto_size_floor_and_conflict():
    cfg = stego_dng.recommend_config(100, auto_size=True)
    assert (cfg["width"], cfg["height"]) == (64, 48)
    try:
        stego_dng.recommend_config(100, width=100, auto_size=True)
    except ValueError:
        pass
    else:
        raise AssertionError("--auto-size + --width should fail")


def test_auto_size_roundtrip_is_smaller():
    import subprocess
    d = tempfile.mkdtemp()
    src_p = os.path.join(d, "in.bin")
    auto_p = os.path.join(d, "auto.dng")
    pre_p = os.path.join(d, "pre.dng")
    rec = os.path.join(d, "out.bin")
    with open(src_p, "wb") as f:
        f.write(os.urandom(60000))
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "encode", "-i", src_p,
         "-o", auto_p, "--seed", "5", "--auto-size",
         "--thumbnail", "synthetic"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "warning: --auto-size chose non-standard dimensions" in r.stdout
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "encode", "-i", src_p,
         "-o", pre_p, "--seed", "5", "--thumbnail", "synthetic"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert os.path.getsize(auto_p) < os.path.getsize(pre_p) // 4
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "decode", "-i", auto_p, "-o", rec],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    with open(src_p, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()


def test_messages_use_kilobytes():
    import subprocess
    d = tempfile.mkdtemp()
    src_p = os.path.join(d, "in.bin")
    enc = os.path.join(d, "o.dng")
    with open(src_p, "wb") as f:
        f.write(os.urandom(3000))
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "encode", "-i", src_p, "-o", enc,
         "--seed", "5", "--width", "512", "--height", "384",
         "--thumbnail", "synthetic"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "KB" in r.stdout and "bytes" not in r.stdout
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "capacity"],
        capture_output=True, text=True)
    assert "KB" in r.stdout and "bytes" not in r.stdout


def test_sixteen_planes_full_replace():
    payload = os.urandom(5000)
    out = _tmp("p16.dng")
    info = stego_dng.encode(payload, out, width=256, height=192, seed=41,
                            lsb_planes=16, thumbnail="synthetic")
    assert info["lsb_planes"] == 16
    assert stego_dng.decode(out) == payload  # autodetects 16
    # ceilings enforced: >16, or above the declared depth, is rejected
    for kw in ({"lsb_planes": 17},
               {"lsb_planes": 16, "bit_depth": 14},
               {"lsb_planes": 9, "bit_depth": 8}):
        try:
            stego_dng.encode(b"z", _tmp("bad.dng"), width=64, height=64,
                             seed=41, **kw, thumbnail="synthetic")
        except ValueError:
            pass
        else:
            raise AssertionError(f"should reject {kw}")


def test_frames_striped_roundtrip():
    import tifffile
    c1 = stego_dng.capacity_bytes(256 * 192 * 3, 1)
    payload = os.urandom(int(c1 + 3000))  # forces striping over frame 2
    out = _tmp("f3.dng")
    info = stego_dng.encode(payload, out, width=256, height=192, seed=42,
                            frames=3, thumbnail="synthetic")
    assert info["frames"] == 3
    # single shared header: total slots floored once, not per frame
    assert info["capacity"] == stego_dng.capacity_bytes_total(
        256 * 192 * 3, 1, 3) == c1 * 3 + 2 * stego_dng.HEADER_LEN
    with tifffile.TiffFile(out) as tif:
        subifds = tif.pages[0].tags[330].value
        assert len(subifds) == 3, subifds
    assert stego_dng.decode(out) == payload
    try:
        stego_dng.encode(b"z", _tmp("bad.dng"), width=64, height=64,
                         seed=42, frames=9, thumbnail="synthetic")
    except ValueError:
        pass
    else:
        raise AssertionError("frames=9 should be rejected")


def test_frames_multiplier_in_recommend():
    a = stego_dng.recommend_config(1000)
    b = stego_dng.recommend_config(1000, frames=3)
    assert b["capacity"] == stego_dng.capacity_bytes_total(
        2048 * 1536 * 3, 1, 3) and b["frames"] == 3


def test_bigtiff_patch_and_append():
    import numpy as np
    import tifffile
    rng = np.random.default_rng(0)
    thumb = np.ascontiguousarray(rng.integers(0, 255, size=(48, 64, 3))
                                 .astype(np.uint8))
    raw = np.ascontiguousarray(rng.integers(0, 65535, size=(64, 80, 3))
                               .astype(np.uint16))
    p = _tmp("bt.dng")
    with tifffile.TiffFile(p, mode="w") if False else tifffile.TiffWriter(
            p, bigtiff=True) as tif:
        tif.write(thumb, photometric="ycbcr", compression="jpeg",
                  metadata=None, software="X",
                  datetime="2020:11:26 12:17:12",
                  subfiletype=1, subifds=2,
                  extratags=[(271, "s", 0, "FUJIFILM", True),
                             (65000, 3, 1, (0,), True)])
        for _ in range(2):
            tif.write(raw, photometric="rgb", metadata=None, software=False,
                      bitspersample=16, subfiletype=0,
                      extratags=[(50714, 4, 3, (256, 256, 256), True),
                                 (50717, 4, 3, (65535, 65535, 65535), True)])
    stego_dng._patch_linear_raw(p)
    stego_dng._append_exif(p, stego_dng.randomize_metadata(1), 64, 48)
    with tifffile.TiffFile(p) as tif:
        assert tif.is_bigtiff
        ifd0 = stego_dng._ifd0_offset(bytearray(tif.filehandle.read()))
    data = bytearray(open(p, "rb").read())
    subs = stego_dng._subifd_offsets(data, stego_dng._ifd0_offset(data))
    assert len(subs) == 2
    import struct
    for s in subs:
        e2 = stego_dng._find_ifd_entry(data, s, 262)
        _, _, vptr = stego_dng._entry_value_ptr(data, e2)
        assert struct.unpack_from("<H", data, vptr)[0] == 34892
    with tifffile.TiffFile(p) as tif:
        assert 34665 in tif.pages[0].tags
        assert len(tif.pages[0].tags[34665].value) == 43


def test_risk_warnings():
    w = stego_dng._risk_warnings(
        {"lsb_planes": 1, "bit_depth": 16, "frames": 1}, key=False)
    assert w == [], w
    w = stego_dng._risk_warnings(
        {"lsb_planes": 16, "bit_depth": 16, "frames": 8}, key=False)
    text = "\n".join(w)
    assert "no cover" in text and "8 full-resolution" in text
    assert "--key" in text
    w = stego_dng._risk_warnings(
        {"lsb_planes": 16, "bit_depth": 16, "frames": 8}, key=True)
    assert not any("--key" in line for line in w)
    w = stego_dng._risk_warnings(
        {"lsb_planes": 2, "bit_depth": 12, "frames": 1}, key=True)
    assert any("12-bit" in line for line in w)


def test_cli_frames_warnings_and_roundtrip():
    import subprocess
    d = tempfile.mkdtemp()
    src_p = os.path.join(d, "in.bin")
    enc = os.path.join(d, "f.dng")
    rec = os.path.join(d, "out.bin")
    with open(src_p, "wb") as f:
        f.write(os.urandom(20000))
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "encode", "-i", src_p, "-o", enc,
         "--seed", "5", "--width", "512", "--height", "384",
         "--thumbnail", "synthetic",
         "--lsb-planes", "6", "--raw-frames", "2"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "warning: 6 LSB planes" in r.stdout
    assert "warning: 2 full-resolution raw frames" in r.stdout
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "decode", "-i", enc, "-o", rec],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    with open(src_p, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()


def test_package_class_apis():
    import numpy as np
    from stegodng import (
        AutoSizer,
        CameraProfile,
        CoverGenerator,
        DngContainer,
        DngStego,
        LsbCodec,
        MetadataRandomizer,
        PayloadFrame,
    )
    # profile derives per-depth levels
    assert CameraProfile().white_level(16) == 65535
    assert CameraProfile().black_level(16) == 256
    assert CameraProfile().top_planes(12) == 12
    # framing roundtrip incl. keyed + tamper detection
    f = PayloadFrame.pack(b"abc", key=b"k")
    assert PayloadFrame.unpack(f, key=b"k")[0] == b"abc"
    try:
        PayloadFrame.unpack(f, key=b"wrong")
    except ValueError:
        pass
    else:
        raise AssertionError("wrong key should fail")
    # metadata + cover + codec units
    m1 = MetadataRandomizer(7).randomize()
    assert MetadataRandomizer(7).randomize() == m1  # deterministic
    cover = CoverGenerator(7).cover(32, 48, "linear", 16)
    assert cover.shape == (32, 48, 3)
    assert CoverGenerator(7).thumbnail(16, 24).shape == (16, 24, 3)
    assert LsbCodec.capacity_bytes(800, 1) == 100 - PayloadFrame.HEADER_LEN
    stego = LsbCodec.embed_bitarray(
        cover, np.unpackbits(np.frombuffer(b"hi", dtype=np.uint8)), 2)
    assert np.packbits(LsbCodec.extract_bitarray(stego, 2, 16)).tobytes() == b"hi"
    # sizer class delegates to the same engine
    assert AutoSizer().recommend(1000)["preset"] == "demo"


def test_package_end_to_end_and_container():
    import tifffile
    from stegodng import DngContainer, DngStego
    payload = os.urandom(3000)
    out = _tmp("pkg.dng")
    stego = DngStego()
    info = stego.encode(payload, out, width=512, height=384, seed=8,
                        lsb_planes=2, frames=2, thumbnail="synthetic")
    assert info["frames"] == 2
    assert stego.decode(out) == payload
    cont = DngContainer(out)
    assert sum(f.size for f in cont.raw_frames()) == 2 * 512 * 384 * 3
    assert len(cont.exif()) == 43
    with tifffile.TiffFile(out) as tif:
        assert len(tif.pages[0].tags[330].value) == 2
    assert DngStego().generate_tiff(_tmp("c.tif"), width=64, height=48,
                                    seed=8).endswith(".tif")


def test_shim_delegates_to_package():
    import stego_dng
    import stegodng.stego
    import stegodng.sizing
    assert stego_dng.encode is stegodng.stego.encode
    assert stego_dng.decode is stegodng.stego.decode
    assert stego_dng.recommend_config is stegodng.sizing.recommend_config
    assert stego_dng.DngStego is stegodng.stego.DngStego
    assert stego_dng.STATIC["model"] == "GFX 100"
    # legacy namespace stays complete (functions, classes, constants)
    for name in (
        "MAGIC", "VERSION", "HEADER_LEN", "FLAG_KEYED", "MAX_LSB_PLANES",
        "MAX_FRAMES", "SUPPORTED_BIT_DEPTHS", "STATIC", "LENSES",
        "ISO_CHOICES", "GFX_NATIVE_W", "PIXELSHIFT_W", "PRESET_GEOMETRIES",
        "XMP_LEN", "pack_frame", "unpack_frame", "randomize_metadata",
        "make_cover", "make_thumbnail", "capacity_bytes", "embed_bits",
        "extract_bits", "build_xmp", "build_exif_block", "encode",
        "encode_split", "decode", "generate_tiff", "recommend_config",
        "CameraProfile", "PayloadFrame", "MetadataRandomizer",
        "CoverGenerator", "LsbCodec", "DngContainer", "AutoSizer",
        "ThumbnailProvider", "main",
    ):
        assert hasattr(stego_dng, name), name


def _thumb_bytes(width=800, height=600, color=(10, 120, 200),
                   fmt="JPEG", mode="RGB"):
    from PIL import Image
    buf = io.BytesIO()
    Image.new(mode, (width, height), color).save(buf, format=fmt)
    return buf.getvalue()


def _fake_opener_factory(files, fail_urls=()):
    def opener(url, timeout):
        if url in fail_urls:
            raise URLError("boom")
        if url == ThumbnailProvider.RANDOM_URL:
            return ("https://commons.wikimedia.org/wiki/File:Meadow.png",
                    b"page")
        if url.startswith(ThumbnailProvider.FILEPATH_URL.format("")):
            return ("https://upload.wikimedia.org/thumb/x/Meadow.png", files)
        raise AssertionError(f"unexpected url {url}")
    return opener


def test_thumbnail_prepare_aspect_and_size():
    from stegodng.thumbnails import prepare
    wide = _thumb_bytes(1600, 400)   # panorama -> 4:3 frame
    a = prepare(wide, 800, 600)
    assert a.shape == (600, 800, 3) and a.dtype == np.uint8
    tall = _thumb_bytes(100, 900)
    b = prepare(tall, 400, 300)
    assert b.shape == (300, 400, 3)
    # alpha composites instead of erroring
    rgba = _thumb_bytes(200, 200, color=(10, 20, 30, 128), fmt="PNG",
                        mode="RGBA")
    c = prepare(rgba, 100, 100)
    assert c.shape == (100, 100, 3)
    try:
        prepare(b"not-an-image", 64, 48)
    except ThumbnailError:
        pass
    else:
        raise AssertionError("corrupt bytes should fail")


def test_thumbnail_random_with_fake_opener():
    from stegodng.thumbnails import ThumbnailError, ThumbnailProvider
    from urllib.error import URLError
    photo = _thumb_bytes(900, 700, fmt="PNG")
    p = ThumbnailProvider(seed=2,
                          opener=_fake_opener_factory(photo))
    arr, label = p.get(320, 240, source="random")
    assert arr.shape == (240, 320, 3) and label == "commons:Meadow.png"
    # network down -> noise fallback, never raises
    p2 = ThumbnailProvider(seed=2, max_attempts=2,
                           opener=_fake_opener_factory(b"", fail_urls=(
                               ThumbnailProvider.RANDOM_URL,)))
    arr2, label2 = p2.get(64, 48, source="random")
    assert label2 == "synthetic-noise-fallback"
    assert arr2.shape == (48, 64, 3)
    n2 = ThumbnailProvider(seed=2).noise(64, 48)
    assert (arr2 == n2).all()  # deterministic fallback
    # unsupported media type (.svg) is skipped, then falls back
    def svg_opener(url, timeout):
        if url == ThumbnailProvider.RANDOM_URL:
            return ("https://commons.wikimedia.org/wiki/File:Pic.svg", b"x")
        raise AssertionError(url)
    arr3, label3 = ThumbnailProvider(
        seed=2, max_attempts=1, opener=svg_opener).get(64, 48)
    assert label3 == "synthetic-noise-fallback"
    # unknown source names are errors, not silent network fetches
    try:
        ThumbnailProvider(seed=2).get(64, 48, source="typo")
    except ThumbnailError:
        pass
    else:
        raise AssertionError("unknown source should fail")


def test_thumbnail_file_source():
    from stegodng.thumbnails import ThumbnailError, ThumbnailProvider
    png = _tmp("pic.png")
    with open(png, "wb") as f:
        f.write(_thumb_bytes(500, 500, fmt="PNG"))
    arr, label = ThumbnailProvider(seed=2).get(100, 100, source=png)
    assert arr.shape == (100, 100, 3) and label == f"file:{png}"
    try:
        ThumbnailProvider(seed=2).get(100, 100, source=png + ".missing")
    except ThumbnailError:
        pass
    else:
        raise AssertionError("missing file source should fail")


def test_cli_thumbnail_variants():
    import subprocess
    d = tempfile.mkdtemp()
    src_p = os.path.join(d, "in.bin")
    png = os.path.join(d, "thumb.png")
    enc = os.path.join(d, "o.dng")
    rec = os.path.join(d, "out.bin")
    with open(src_p, "wb") as f:
        f.write(os.urandom(2000))
    with open(png, "wb") as f:
        f.write(_thumb_bytes(300, 200, fmt="PNG"))
    for extra in (["--thumbnail", "synthetic"],
                  ["--thumbnail", png]):
        r = subprocess.run(
            [sys.executable, "stego_dng.py", "encode", "-i", src_p,
             "-o", enc, "--seed", "5", "--width", "256", "--height", "192"]
            + extra, capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        assert "thumbnail: " in r.stdout
        r = subprocess.run(
            [sys.executable, "stego_dng.py", "decode", "-i", enc, "-o", rec],
            capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        with open(src_p, "rb") as f1, open(rec, "rb") as f2:
            assert f1.read() == f2.read()
    # IFD0 is a decodable JPEG with the right frame size
    import tifffile
    from PIL import Image
    with tifffile.TiffFile(enc) as tif:
        offsets = tif.pages[0].tags[273].value
        counts = tif.pages[0].tags[279].value
        with open(enc, "rb") as f:
            f.seek(offsets[0] if isinstance(offsets, tuple) else offsets)
            n = counts[0] if isinstance(counts, tuple) else counts
            jpeg = f.read(n)
    im = Image.open(io.BytesIO(jpeg))
    assert im.size == (256, 192), im.size


def test_thumbnail_ycbcr_colors_correct():
    # Regression: YCbCr-tagged IFD0 must decode with faithful colors
    # (tifffile stores the planes verbatim, so RGB input came out swapped).
    import tifffile
    from PIL import Image
    red = _tmp("red.png")
    Image.new("RGB", (300, 200), (255, 0, 0)).save(red)
    out = _tmp("redthumb.dng")
    stego_dng.encode(b"payload-123", out, width=256, height=192, seed=1,
                     thumbnail=red)
    with tifffile.TiffFile(out) as tif:
        pg = tif.pages[0]
        assert int(pg.photometric) == 6  # still YCbCr like combiner files
        offs = pg.tags[273].value
        counts = pg.tags[279].value
        off = offs[0] if isinstance(offs, tuple) else offs
        n = counts[0] if isinstance(counts, tuple) else counts
        with open(out, "rb") as f:
            f.seek(off)
            jpeg = f.read(n)
    mean = Image.open(io.BytesIO(jpeg)).convert("RGB")
    import numpy as _np
    r, g, b = _np.asarray(mean).reshape(-1, 3).mean(axis=0)
    assert r > 200 and g < 80 and b < 80, (r, g, b)


def test_split_size_parsing():
    from stegodng.split import parse_size
    assert parse_size("1g") == 1024 ** 3
    assert parse_size("100m") == 100 * 1024 ** 2
    assert parse_size("500k") == 500 * 1024
    assert parse_size("2G") == 2 * 1024 ** 3
    assert parse_size("64KB") == 64 * 1024
    assert parse_size("1.5m") == int(1.5 * 1024 ** 2)
    assert parse_size("1024") == 1024
    for bad in ("", "abc", "10x", "0", "-5m"):
        try:
            parse_size(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"should reject {bad!r}")


def test_split_naming_and_parsing():
    from stegodng.split import chunk_path, parse_chunk_name
    assert chunk_path("out.dng", 1) == "out0001.dng"
    assert chunk_path("a/b", 12) == "a/b0012"
    assert parse_chunk_name("test0001.dng") == ("test", 1, ".dng")
    assert parse_chunk_name("test0003.dng") == ("test", 3, ".dng")
    assert parse_chunk_name("plain.dng") is None


def _split_three(tmpname="sp.dng", **kw):
    import glob
    from stegodng import DngStego
    payload = os.urandom(60000)
    d = tempfile.mkdtemp()
    out = os.path.join(d, tmpname)
    infos = DngStego().encode_split(
        payload, out, 20000, width=512, height=384, seed=5,
        thumbnail="synthetic", split_id="unitestuid", **kw)
    assert len(infos) == 3
    assert [i["chunk_seq"] for i in infos] == [1, 2, 3]
    assert all(i["chunk_total"] == 3 for i in infos)
    files = sorted(glob.glob(os.path.join(
        d, os.path.splitext(tmpname)[0] + "0*.dng")))
    assert len(files) == 3
    return payload, files


def test_split_roundtrip_defaults():
    import tifffile
    payload, files = _split_three()
    from stegodng import DngStego
    with tifffile.TiffFile(files[1]) as tif:
        ex = tif.pages[0].tags[34665].value
        assert ex.get("ImageUniqueID") == "unitestuid"
        # ImageNumber is TIFF/EP tag 0x9211 = 37393 decimal, in EXIF
        assert ex.get("ImageNumber") in (2, (2,))
        assert 9211 not in tif.pages[0].tags  # no bogus decimal tag
    assert DngStego().decode(files) == payload
    assert DngStego().decode(list(reversed(files))) == payload  # order-free


def test_split_rename_uuid_ordering():
    import shutil
    from stegodng import DngStego
    payload, files = _split_three()
    d = tempfile.mkdtemp()
    renamed = []
    for src, name in zip(files, ["zeta.dng", "alpha.dng", "mid.dng"]):
        dst = os.path.join(d, name)
        shutil.copy(src, dst)
        renamed.append(dst)
    assert DngStego().decode(renamed) == payload


def test_split_gap_start_mixed_errors():
    from stegodng import DngStego
    payload, files = _split_three()
    try:
        DngStego().decode([files[0], files[2]])
    except ValueError as exc:
        assert "0002" in str(exc) and "consecutive" in str(exc)
    else:
        raise AssertionError("gap should fail")
    try:
        DngStego().decode(files[1:])
    except ValueError as exc:
        assert "0001" in str(exc)
    else:
        raise AssertionError("start-at-0002 should fail")
    # mixed with a plain non-split file
    plain = os.path.join(tempfile.mkdtemp(), "plain.dng")
    DngStego().encode(b"x", plain, width=256, height=192, seed=5,
                      thumbnail="synthetic")
    try:
        DngStego().decode([files[0], plain])
    except ValueError as exc:
        assert "inconsistent" in str(exc)
    else:
        raise AssertionError("mixed set should fail")
    # not chunks at all
    try:
        DngStego().decode([plain, plain])
    except ValueError as exc:
        assert "4-digit" in str(exc)
    else:
        raise AssertionError("non-chunks should fail")


def test_split_none_none_filename_path():
    import glob
    import shutil
    from stegodng import DngStego
    payload = os.urandom(60000)
    d = tempfile.mkdtemp()
    infos = DngStego().encode_split(
        payload, os.path.join(d, "nn.dng"), 20000, width=512, height=384,
        seed=5, thumbnail="synthetic", split_id_field="none",
        split_seq_field="none", split_id="x")
    assert len(infos) == 3
    files = sorted(glob.glob(os.path.join(d, "nn0*.dng")))
    assert DngStego().decode(files) == payload
    renamed = [os.path.join(d, n) for n in ("a.dng", "b.dng", "c.dng")]
    for src, dst in zip(files, renamed):
        shutil.copy(src, dst)
    try:
        DngStego().decode(renamed)
    except ValueError as exc:
        assert "4-digit" in str(exc)
    else:
        raise AssertionError("renamed marker-less files should fail")


def test_split_pagenumber_total_enforced():
    import glob
    from stegodng import DngStego
    payload = os.urandom(50000)
    d = tempfile.mkdtemp()
    DngStego().encode_split(
        payload, os.path.join(d, "pn.dng"), 20000, width=512, height=384,
        seed=5, thumbnail="synthetic", split_id="uid7",
        split_seq_field="PageNumber")
    files = sorted(glob.glob(os.path.join(d, "pn0*.dng")))
    assert DngStego().decode(files, split_seq_field="PageNumber") == payload
    try:
        DngStego().decode(files[:2], split_seq_field="PageNumber")
    except ValueError as exc:
        assert "0003" in str(exc) and "total" in str(exc)
    else:
        raise AssertionError("subset should fail on total")


def test_split_single_chunk_plain_and_warning():
    import warnings
    from stegodng import DngStego
    d = tempfile.mkdtemp()
    infos = DngStego().encode_split(
        b"tiny", os.path.join(d, "one.dng"), 100000, width=256, height=192,
        seed=5, thumbnail="synthetic")
    assert len(infos) == 1 and infos[0]["path"].endswith("one.dng")
    assert "chunk_seq" not in infos[0]
    assert DngStego().decode(infos[0]["path"]) == b"tiny"
    # lone chunk file warns about partial data
    _, files = _split_three()
    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        part = DngStego().decode(files[0])
    assert len(part) < 60000 and any("partial" in str(w.message) for w in rec)


def test_split_field_validation():
    from stegodng import DngStego
    for kw in ({"split_id_field": "Nope"},
               {"split_seq_field": "Nope"},
               {"split_id_field": "ImageDescription",
                "split_seq_field": "ImageDescription"}):
        try:
            DngStego().encode_split(
                b"z" * 100, _tmp("v.dng"), 50, width=256, height=192,
                seed=5, thumbnail="synthetic", **kw)
        except ValueError:
            pass
        else:
            raise AssertionError(f"should reject {kw}")
    try:
        DngStego().encode_split(
            b"z", _tmp("v.dng"), 0, width=256, height=192, seed=5,
            thumbnail="synthetic")
    except ValueError:
        pass
    else:
        raise AssertionError("split_size=0 should fail")


def test_split_partial_markers_error():
    # Every file has a UUID but no sequence: precise error, not generic mix.
    from stegodng import DngStego
    payload = os.urandom(40000)
    d = tempfile.mkdtemp()
    infos = DngStego().encode_split(
        payload, os.path.join(d, "pm.dng"), 20000, width=512, height=384,
        seed=5, thumbnail="synthetic", split_id="partialset",
        split_seq_field="ImageDescription")
    files = [i["path"] for i in infos]
    try:
        DngStego().decode(files)
    except ValueError as exc:
        assert "none carries sequence markers" in str(exc)
    else:
        raise AssertionError("uuid-only set should fail clearly")
    # ... but decodes once told the right seq field
    assert DngStego().decode(
        files, split_seq_field="ImageDescription") == payload


def test_cli_split_roundtrip():
    import subprocess
    d = tempfile.mkdtemp()
    src_p = os.path.join(d, "in.bin")
    enc = os.path.join(d, "out.dng")
    rec = os.path.join(d, "back.bin")
    with open(src_p, "wb") as f:
        f.write(os.urandom(50000))
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "encode", "-i", src_p, "-o", enc,
         "--seed", "5", "--width", "512", "--height", "384",
         "--thumbnail", "synthetic", "--split-file", "20k",
         "--key", "pw"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "chunk 1/3" in r.stdout and "chunk 3/3" in r.stdout
    assert "bytes" not in r.stdout
    import glob as _glob
    files = sorted(_glob.glob(os.path.join(d, "out0*.dng")))
    assert len(files) == 3
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "decode", "-i"] + files +
        ["-o", rec, "--key", "pw"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    with open(src_p, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()
    # gap via CLI
    r = subprocess.run(
        [sys.executable, "stego_dng.py", "decode", "-i", files[0], files[2],
         "-o", rec], capture_output=True, text=True)
    assert r.returncode == 1 and "0002" in r.stderr


def test_split_imagenumber_fail_open_pinned():
    # ImageNumber carries no total: a consecutive-from-0001 subset
    # decodes WITHOUT error (fail-open). Use PageNumber to fail closed.
    from stegodng import DngStego
    payload = os.urandom(60000)
    d = tempfile.mkdtemp()
    infos = DngStego().encode_split(
        payload, os.path.join(d, "sp.dng"), 20000, width=512, height=384,
        seed=5, thumbnail="synthetic", split_id="failopen")
    assert len(infos) == 3
    files = [i["path"] for i in infos]
    assert DngStego().decode(files[:2]) == payload[:40000]


def test_auto_size_large_fast():
    import time
    from stegodng.sizing import recommend
    t = time.time()
    cfg = recommend(200_000_000, auto_size=True)
    dt = time.time() - t
    assert cfg["capacity"] >= 200_000_000, cfg
    assert cfg["width"] <= 23296 and cfg["height"] <= 17472, cfg
    assert dt < 1.0, dt


def test_split_frames_striped_roundtrip():
    import tifffile
    from stegodng import DngStego
    c1 = stego_dng.capacity_bytes_total(256 * 192 * 3, 1, 2)
    payload = os.urandom(int(c1 + 3000))  # forces striping over chunk 2
    d = tempfile.mkdtemp()
    infos = DngStego().encode_split(
        payload, os.path.join(d, "sf.dng"), int(c1), width=256, height=192,
        seed=5, thumbnail="synthetic", frames=2, split_id="framed")
    assert len(infos) == 2
    for info in infos:
        with tifffile.TiffFile(info["path"]) as tif:
            assert len(tif.pages[0].tags[330].value) == 2
    files = [i["path"] for i in infos]
    assert DngStego().decode(files) == payload


def test_split_offline_thumbs_differ():
    import tifffile
    from stegodng import DngStego
    import stegodng.stego as stego_mod
    from stegodng.thumbnails import ThumbnailError, ThumbnailProvider
    orig = stego_mod.ThumbnailProvider

    class OfflineProvider(ThumbnailProvider):
        def _fetch_random_bytes(self, tw):
            raise ThumbnailError("offline")

    stego_mod.ThumbnailProvider = OfflineProvider
    try:
        payload = os.urandom(40000)
        d = tempfile.mkdtemp()
        infos = DngStego().encode_split(
            payload, os.path.join(d, "off.dng"), 20000, width=512,
            height=384, seed=None, thumbnail="random")
        assert len(infos) == 2
        strips = []
        for info in infos:
            with tifffile.TiffFile(info["path"]) as tif:
                pg = tif.pages[0]
                offs = pg.tags[273].value
                counts = pg.tags[279].value
                off = offs[0] if isinstance(offs, tuple) else offs
                n = counts[0] if isinstance(counts, tuple) else counts
                with open(info["path"], "rb") as f:
                    f.seek(off)
                    strips.append(f.read(n))
        assert strips[0] != strips[1], "chunk fallback thumbs must differ"
    finally:
        stego_mod.ThumbnailProvider = orig


def test_streaming_chunked_roundtrip():
    # Force the multi-chunk path: tiny sample chunks over two frames,
    # unaligned payload lengths, planes 1/3/8/16 (uint16 throughout —
    # P=16 on a uint8 container would truncate high planes).
    from stegodng.codec import LsbCodec
    from stegodng.framing import PayloadFrame
    orig = LsbCodec._chunk_samples
    LsbCodec._chunk_samples = staticmethod(lambda p: 64)
    try:
        rng = np.random.default_rng(1234)
        c1 = (rng.integers(0, 65535, size=(64, 64, 3)).astype(np.uint16))
        c2 = (rng.integers(0, 65535, size=(48, 48, 3)).astype(np.uint16))
        for key in (None, b"chunk-key"):
            for P in (1, 3, 8, 16):
                cap = LsbCodec.capacity_bytes_total(c1.size, P, 1) \
                    + LsbCodec.capacity_bytes_total(c2.size, P, 1) \
                    + PayloadFrame.HEADER_LEN
                for nbytes in (100, 1000, min(2000, cap)):
                    payload = os.urandom(nbytes)
                    frame = PayloadFrame.pack(payload, key)
                    assert len(frame) * 8 <= c1.size * P + c2.size * P
                    stegos = LsbCodec.stripe_frames(
                        [c1.copy(), c2.copy()], frame, P)
                    # 2000-byte payload at P=1 must spill into frame 2
                    # (first cover holds only 12288 bits).
                    out = LsbCodec.extract_stream(
                        stegos, P, len(frame) * 8)
                    assert PayloadFrame.unpack(out, key)[0] == payload, (P, nbytes, key)
    finally:
        LsbCodec._chunk_samples = orig


def test_stripe_frames_overflow_raises():
    # Old code silently dropped bits past the cover slots; fail closed.
    from stegodng.codec import LsbCodec
    cover = np.zeros((8, 8, 3), dtype=np.uint16)
    try:
        LsbCodec.stripe_frames([cover], b"\xff" * 10000, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("oversize stripe_frames should raise")


def test_extract_bitarray_oversize_raises():
    from stegodng.codec import LsbCodec
    raw = np.zeros((8, 8, 3), dtype=np.uint16)
    try:
        LsbCodec.extract_bitarray(raw, 1, raw.size + 1)
    except ValueError:
        pass
    else:
        raise AssertionError("oversize extract_bitarray should raise")


def test_keystream_range_equivalence():
    from stegodng.framing import PayloadFrame
    key = b"range-key"
    full = PayloadFrame._keystream(key, 200)
    for off, ln in ((0, 18), (0, 200), (5, 100), (31, 33), (32, 64),
                    (100, 7), (63, 65)):
        assert PayloadFrame._keystream_range(key, off, ln) == full[off:off + ln]
    assert PayloadFrame._keystream_range(key, 10, 0) == b""


def test_seek_vs_buffer_parity():
    import stego_dng
    from stegodng import container as C
    out = _tmp("parity.dng")
    stego_dng.encode(b"parity-check", out, width=256, height=192, seed=9,
                     frames=2, thumbnail="synthetic")
    data = bytearray(open(out, "rb").read())
    ifd0 = C._ifd0_offset(data)
    with open(out, "rb") as f:
        assert C._seek_ifd0_offset(f) == ifd0
        assert C._seek_subifd_offsets(f, ifd0) == C._subifd_offsets(data, ifd0)
        for tag in (271, 330, 34665):
            e = C._find_ifd_entry(data, ifd0, tag)
            found = C._seek_ifd_entry(f, ifd0, tag)
            assert found is not None and found[0] == e, tag
            assert found[1:4] == C._entry_value_ptr(data, e), tag
        # Dummy 65000 is rewritten to ExifTag 34665 during finishing:
        # absent in both views.
        assert C._find_ifd_entry(data, ifd0, 65000) is None
        with open(out, "rb") as f2:
            assert C._seek_ifd_entry(f2, ifd0, 65000) is None


def test_bigtiff_seek_helpers_synthetic():
    import struct
    from stegodng import container as C

    def blob(ifd0_off, entries, blobs):
        data = bytearray(ifd0_off)
        data[0:4] = b"II+\x00"
        struct.pack_into("<Q", data, 8, ifd0_off)
        data += struct.pack("<Q", len(entries))
        for tag, typ, count, field in entries:
            data += struct.pack("<HHQ8s", tag, typ, count, field)
        data += struct.pack("<Q", 0)
        base = len(data)
        out = []
        for b in blobs:
            out.append(len(data))
            data += b
        return data, base, out

    def subifd(photo):
        return (struct.pack("<Q", 1)
                + struct.pack("<HHQ8s", 262, 3, 1,
                              struct.pack("<H", photo) + b"\x00" * 6)
                + struct.pack("<Q", 0))

    # External-offset branch: tag 330 LONG8 count 2 -> 8-byte array.
    ifd0 = 16
    arr_off = ifd0 + 8 + 2 * 20 + 8
    s1 = arr_off + 16
    s2 = s1 + 36
    data, base, _ = blob(
        ifd0,
        [(330, 18, 2, struct.pack("<Q", arr_off)),
         (274, 3, 1, struct.pack("<H", 1) + b"\x00" * 6)],
        [struct.pack("<QQ", s1, s2), subifd(2), subifd(2)])
    assert base == arr_off
    assert C._tiff_is_bigtiff(data) and C._ifd0_offset(data) == ifd0
    assert C._subifd_offsets(data, ifd0) == [s1, s2]
    e = C._find_ifd_entry(data, ifd0, 330)
    p = _tmp("syn_bt.dng")
    with open(p, "wb") as f:
        f.write(data)
    with open(p, "rb") as f:
        assert C._seek_ifd0_offset(f) == ifd0
        found = C._seek_ifd_entry(f, ifd0, 330)
        assert found is not None and found[0] == e
        assert found[1:4] == C._entry_value_ptr(data, e)
        assert C._seek_subifd_offsets(f, ifd0) == [s1, s2]

    # Inline branch: tag 330 count 1 fits the 8-byte value field.
    s1b = ifd0 + 8 + 1 * 20 + 8
    data2, _, _ = blob(
        ifd0,
        [(330, 18, 1, struct.pack("<Q", s1b))],
        [subifd(2)])
    assert C._subifd_offsets(data2, ifd0) == [s1b]
    p2 = _tmp("syn_bt_inline.dng")
    with open(p2, "wb") as f:
        f.write(data2)
    with open(p2, "rb") as f:
        assert C._seek_subifd_offsets(f, ifd0) == [s1b]


if __name__ == "__main__":

    for name, fn in sorted(
        [(k, v) for k, v in globals().items() if k.startswith("test_")]
    ):
        fn()
        print(f"{name} ... ok")
    print("all tests passed")
