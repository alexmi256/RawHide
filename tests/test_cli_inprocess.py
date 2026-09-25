"""In-process CLI tests (main) — covers stegodng/cli.py without subprocesses."""

import glob
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stegodng.cli import main


def _write_input(path, n=3000, seed=0):
    import random
    rng = random.Random(seed)
    with open(path, "wb") as f:
        f.write(bytes(rng.randrange(256) for _ in range(n)))


def test_cli_encode_decode_capacity_gentiff(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    enc = str(tmp_path / "o.dng")
    rec = str(tmp_path / "out.bin")
    _write_input(src, 2000)
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic"]) == 0
    out = capsys.readouterr().out
    assert "wrote" in out and "thumbnail:" in out and "meta:" in out
    assert main(["decode", "-i", enc, "-o", rec]) == 0
    with open(src, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()
    assert main(["capacity", "--width", "256", "--height", "192"]) == 0
    out = capsys.readouterr().out
    assert "samples:" in out and "KB" in out
    assert main(["capacity", "--width", "64", "--height", "48",
                 "--mode", "cfa", "--lsb-planes", "2",
                 "--raw-frames", "2"]) == 0
    assert "x 2 frames" in capsys.readouterr().out
    tiff = str(tmp_path / "c.tif")
    assert main(["gen-tiff", "-o", tiff, "--width", "32",
                 "--height", "24", "--seed", "1"]) == 0
    assert "wrote" in capsys.readouterr().out


def test_cli_auto_and_warnings(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    enc = str(tmp_path / "auto.dng")
    _write_input(src, 2000)
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--thumbnail", "synthetic"]) == 0
    assert "auto-config" in capsys.readouterr().out
    # High-risk options emit warnings; key suppresses the --key hint.
    enc2 = str(tmp_path / "risk.dng")
    assert main(["encode", "-i", src, "-o", enc2, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic",
                 "--lsb-planes", "6", "--raw-frames", "2",
                 "--bit-depth", "12", "--key", "pw"]) == 0
    out = capsys.readouterr().out
    assert "warning: 6 LSB planes" in out
    assert "warning: 2 full-resolution" in out
    assert "warning: 12-bit" in out


def test_cli_auto_size_and_conflict(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    _write_input(src, 500)
    with pytest.raises(SystemExit):
        main(["encode", "-i", src, "-o", str(tmp_path / "x.dng"),
              "--auto-size", "--width", "256"])
    enc = str(tmp_path / "as.dng")
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--auto-size", "--thumbnail", "synthetic"]) == 0
    out = capsys.readouterr().out
    assert "non-standard dimensions" in out


def test_cli_gfx_pixelshift_flags_mocked(tmp_path, monkeypatch, capsys):
    import stegodng.cli as cli_mod
    src = str(tmp_path / "in.bin")
    _write_input(src, 100)
    seen = {}

    def fake_recommend(n, **kw):
        seen.update(kw)
        w = kw.get("width") or 256
        h = kw.get("height") or 192
        return {"width": w, "height": h, "mode": "linear",
                "bit_depth": 16, "lsb_planes": 1, "frames": 1,
                "capacity": 99999, "auto": [], "preset": None}

    def fake_encode(payload, path, **kw):
        seen.update(kw)
        with open(path, "wb") as f:
            f.write(b"DNG")
        return {"path": path, "size": 3, "payload_len": len(payload),
                "capacity": 99999, "bigtiff": False,
                "thumbnail": "synthetic-gradient",
                "metadata": {"datetime": "2020:01:01 00:00:00",
                             "iso": 100, "lens": "L",
                             "camera_serial": "S"}}

    monkeypatch.setattr(cli_mod, "recommend", fake_recommend)
    monkeypatch.setattr(cli_mod, "encode", fake_encode)
    assert main(["encode", "-i", src, "-o", str(tmp_path / "g.dng"),
                 "--gfx-native", "--thumbnail", "synthetic"]) == 0
    assert seen["width"] == 11648 and seen["height"] == 8736
    assert main(["encode", "-i", src, "-o", str(tmp_path / "p.dng"),
                 "--pixelshift", "--thumbnail", "synthetic"]) == 0
    assert seen["width"] == 23296 and seen["height"] == 17472


def test_cli_bigtiff_warning_mocked(tmp_path, monkeypatch, capsys):
    import stegodng.cli as cli_mod
    src = str(tmp_path / "in.bin")
    _write_input(src, 100)

    def fake_encode(payload, path, **kw):
        with open(path, "wb") as f:
            f.write(b"DNG")
        return {"path": path, "size": 3, "payload_len": len(payload),
                "capacity": 99999, "bigtiff": True,
                "thumbnail": "t", "metadata": {"datetime": "d", "iso": 1,
                                               "lens": "l", "camera_serial": "s"}}

    monkeypatch.setattr(cli_mod, "encode", fake_encode)
    assert main(["encode", "-i", src, "-o", str(tmp_path / "b.dng"),
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic"]) == 0
    assert "BigTIFF" in capsys.readouterr().out


def test_cli_split_paths(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    _write_input(src, 15000, seed=1)
    enc = str(tmp_path / "sp.dng")
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic", "--split-file", "5k",
                 "--key", "pw"]) == 0
    out = capsys.readouterr().out
    assert "chunk 1/" in out and "note: chunks share" in out
    files = sorted(glob.glob(str(tmp_path / "sp0*.dng")))
    assert len(files) >= 2
    rec = str(tmp_path / "back.bin")
    assert main(["decode", "-i"] + files + ["-o", rec, "--key", "pw"]) == 0


def test_cli_split_none_none_notes(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    _write_input(src, 12000, seed=2)
    enc = str(tmp_path / "nn.dng")
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic", "--split-file", "4k",
                 "--split-file-metadata-id", "none",
                 "--split-file-metadata-seq", "none"]) == 0
    assert "no split markers" in capsys.readouterr().out
    # id none + seq default: sequence note branch.
    enc2 = str(tmp_path / "ns.dng")
    assert main(["encode", "-i", src, "-o", enc2, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic", "--split-file", "4k",
                 "--split-file-metadata-id", "none"]) == 0
    assert "no shared chunk-set UUID" in capsys.readouterr().out


def test_cli_split_bigtiff_warning_mocked(tmp_path, monkeypatch, capsys):
    import stegodng.cli as cli_mod
    src = str(tmp_path / "in.bin")
    _write_input(src, 100)

    def fake_split(payload, path, split_size, **kw):
        return [{"path": path + "0001", "size": 1, "payload_len": 1,
                 "capacity": 9, "bigtiff": True, "thumbnail": "t",
                 "chunk_seq": 1, "chunk_total": 2, "split_id": "u",
                 "split_id_field": "ImageUniqueID",
                 "split_seq_field": "ImageNumber",
                 "metadata": {"datetime": "d", "iso": 1, "lens": "l",
                              "camera_serial": "s"}},
                {"path": path + "0002", "size": 1, "payload_len": 1,
                 "capacity": 9, "bigtiff": False, "thumbnail": "t",
                 "chunk_seq": 2, "chunk_total": 2, "split_id": "u",
                 "split_id_field": "ImageUniqueID",
                 "split_seq_field": "ImageNumber",
                 "metadata": {"datetime": "d", "iso": 1, "lens": "l",
                              "camera_serial": "s"}}]

    monkeypatch.setattr(cli_mod, "encode_split", fake_split)
    assert main(["encode", "-i", src, "-o", str(tmp_path / "s.dng"),
                 "--split-file", "1k", "--thumbnail", "synthetic"]) == 0
    assert "BigTIFF" in capsys.readouterr().out


def test_cli_encode_errors(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    _write_input(src, 100)
    # Bad split size.
    r = main(["encode", "-i", src, "-o", str(tmp_path / "x.dng"),
              "--split-file", "bogus", "--thumbnail", "synthetic"])
    assert r == 1
    assert "error:" in capsys.readouterr().err
    # Oversize payload for tiny geometry.
    big = str(tmp_path / "big.bin")
    _write_input(big, 50000, seed=3)
    r = main(["encode", "-i", big, "-o", str(tmp_path / "y.dng"),
              "--width", "64", "--height", "48",
              "--thumbnail", "synthetic"])
    assert r == 1
    assert "error:" in capsys.readouterr().err
    # Thumbnail file + compression + cfa + no-randomize + split id opts.
    from PIL import Image
    png = str(tmp_path / "t.png")
    Image.new("RGB", (32, 32), (1, 2, 3)).save(png)
    enc = str(tmp_path / "full.dng")
    r = main(["encode", "-i", src, "-o", enc, "--seed", "7",
              "--width", "512", "--height", "384", "--mode", "cfa",
              "--bit-depth", "8", "--compression", "adobe_deflate",
              "--thumbnail", png, "--no-randomize", "--raw-frames", "1",
              "--split-file", "20k", "--split-file-id", "fixedid",
              "--split-file-metadata-id", "ImageDescription",
              "--split-file-metadata-seq", "PageNumber"])
    assert r == 0, capsys.readouterr().err


def test_cli_decode_errors_and_notes(tmp_path, capsys):
    src = str(tmp_path / "in.bin")
    enc = str(tmp_path / "o.dng")
    rec = str(tmp_path / "r.bin")
    _write_input(src, 15000, seed=4)
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--width", "512", "--height", "384",
                 "--thumbnail", "synthetic",
                 "--split-file", "5k"]) == 0
    capsys.readouterr()
    files = sorted(glob.glob(str(tmp_path / "o0*.dng")))
    # Multi-file decode without totals -> advisory note.
    assert main(["decode", "-i"] + files + ["-o", rec]) == 0
    assert "no chunk totals" in capsys.readouterr().out
    # Bad max-bytes string.
    r = main(["decode", "-i", enc, "-o", rec, "--max-bytes", "bogus"])
    assert r == 1
    # Non-positive max-bytes.
    r = main(["decode", "-i", enc, "-o", rec, "--max-bytes", "0"])
    assert r == 1
    assert "positive" in capsys.readouterr().err
    # Undecodable single file.
    plain = str(tmp_path / "plain.txt")
    with open(plain, "wb") as f:
        f.write(b"not a dng")
    r = main(["decode", "-i", plain, "-o", rec])
    assert r == 1
    # Gap across chunks.
    r = main(["decode", "-i", files[0], files[-1], "-o", rec])
    assert r == 1
    assert "0002" in capsys.readouterr().err
    # Explicit planes + custom metadata fields + max-bytes ok. Single-chunk
    # decode warns about partial data (expected).
    with pytest.warns(UserWarning, match="partial data"):
        assert main(["decode", "-i", files[0], "-o", rec,
                     "--lsb-planes", "1", "--max-bytes", "10m"]) == 0


def test_cli_split_seq_none_note(tmp_path, capsys):
    # id active + seq none: covers the "no sequence numbers" note.
    src = str(tmp_path / "in.bin")
    _write_input(src, 12000, seed=6)
    enc = str(tmp_path / "seqnone.dng")
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic", "--split-file", "4k",
                 "--split-file-metadata-seq", "none"]) == 0
    assert "no sequence numbers in metadata" in capsys.readouterr().out


def test_cli_decode_marks_fallback(tmp_path, monkeypatch, capsys):
    # Multi-file decode where the post-decode marker re-read fails:
    # decode succeeds (mocked), split_markers raises -> marks=[] fallback.
    import stegodng.cli as cli_mod
    src = str(tmp_path / "in.bin")
    _write_input(src, 15000, seed=8)
    enc = str(tmp_path / "o.dng")
    assert main(["encode", "-i", src, "-o", enc, "--seed", "5",
                 "--width", "512", "--height", "384",
                 "--thumbnail", "synthetic",
                 "--split-file", "5k"]) == 0
    capsys.readouterr()
    files = sorted(glob.glob(str(tmp_path / "o0*.dng")))
    assert len(files) >= 2
    rec = str(tmp_path / "r.bin")
    monkeypatch.setattr(cli_mod, "decode", lambda *a, **k: b"data")
    def boom(self, id_field="ImageUniqueID", seq_field="ImageNumber"):
        raise ValueError("marker boom")
    monkeypatch.setattr(cli_mod.DngContainer, "split_markers", boom)
    assert main(["decode", "-i"] + files + ["-o", rec]) == 0
    out = capsys.readouterr().out
    assert "recovered" in out
    assert "no chunk totals" not in out


def test_cli_encode_default_output(tmp_path, capsys):
    src = str(tmp_path / "inputabc.ext")
    _write_input(src, 2000)
    assert main(["encode", "-i", src, "--seed", "5",
                 "--width", "256", "--height", "192",
                 "--thumbnail", "synthetic"]) == 0
    capsys.readouterr()
    assert os.path.isfile(src + ".dng")
    rec = str(tmp_path / "out.bin")
    assert main(["decode", "-i", src + ".dng", "-o", rec]) == 0
    with open(src, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()


def test_cli_encode_default_output_split(tmp_path, capsys):
    src = str(tmp_path / "inputabc.ext")
    _write_input(src, 15000, seed=8)
    assert main(["encode", "-i", src, "--seed", "5",
                 "--width", "512", "--height", "384",
                 "--thumbnail", "synthetic",
                 "--split-file", "5k"]) == 0
    capsys.readouterr()
    files = sorted(glob.glob(src + "????.dng"))
    assert len(files) >= 2
    assert files[0] == src + "0001.dng"
    assert files[1] == src + "0002.dng"
    rec = str(tmp_path / "out.bin")
    assert main(["decode", "-i"] + files + ["-o", rec]) == 0
    with open(src, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()


def test_cli_encode_default_output_split_single_chunk(tmp_path, capsys):
    # Payload fits in one chunk: plain single file, no sequence number.
    src = str(tmp_path / "inputabc.ext")
    _write_input(src, 500)
    assert main(["encode", "-i", src, "--seed", "5",
                 "--thumbnail", "synthetic",
                 "--split-file", "1m"]) == 0
    capsys.readouterr()
    assert os.path.isfile(src + ".dng")
    assert glob.glob(src + "????.dng") == []
    rec = str(tmp_path / "out.bin")
    assert main(["decode", "-i", src + ".dng", "-o", rec]) == 0
    with open(src, "rb") as f1, open(rec, "rb") as f2:
        assert f1.read() == f2.read()
