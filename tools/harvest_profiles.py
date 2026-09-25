#!/usr/bin/env python3
"""Harvest per-camera profile data from dpreview-raw RAWs.

For every unique (Make, Model) found via exiv2:
  - representative file (prefer true RAW extensions over heic/jpg)
  - EXIF pools across all files of the model (lens, ISO, exposure, fnumber,
    focal, metering, exp-program, software, serials presence)
  - native geometry via `identify` on the representative
  - full DNG calibration via tifffile when representative is .dng/.DNG

Writes stegodng/profiles/<slug>/{profile.json,README.md}.
Skips models with no true RAW file (heic/jpg-only) and placeholder models.
"""
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

BASE = "/home/alex/PycharmProjects/ImageSteg2/dpreview-raw"
# NOTE: this script only writes /tmp/opencode/harvest_index.json;
# tools/gen_profiles.py turns that index into stegodng/profiles/.

RAW_EXTS = {".arw", ".nef", ".nrw", ".raf", ".rw2", ".orf", ".cr2", ".cr3",
            ".dng", ".3fr", ".fff", ".pef", ".x3f", ".gpr", ".raw"}
SKIP_MODELS = {("SONY", "MODEL-NAME")}  # placeholder, not a real camera

KEYS = [
    "Exif.Image.Make", "Exif.Image.Model", "Exif.Image.Software",
    "Exif.Image.BitsPerSample",
    "Exif.Photo.LensMake", "Exif.Photo.LensModel",
    "Exif.Photo.PixelXDimension", "Exif.Photo.PixelYDimension",
    "Exif.Photo.ISOSpeedRatings", "Exif.Photo.ExposureTime",
    "Exif.Photo.FNumber", "Exif.Photo.FocalLength",
    "Exif.Photo.FocalLengthIn35mmFilm", "Exif.Photo.ExposureProgram",
    "Exif.Photo.MeteringMode", "Exif.Photo.WhiteBalance",
    "Exif.Photo.BodySerialNumber",
    "Exif.Image.CameraSerialNumber",
    "Exif.Canon.SerialNumber", "Exif.Nikon3.SerialNumber",
    "Exif.Nikon3.SerialNumber2",
    "Exif.Sony.SerialNumber", "Exif.Fujifilm.SerialNumber",
    "Exif.Panasonic.SerialNumber", "Exif.Olympus.SerialNumber2",
    "Exif.Leica.SerialNumber", "Exif.Sigma.SerialNumber",
    "Exif.Pentax.SerialNumber",
]

SHORT_DISPLAY = {
    # (make-prefix, model) -> short display handled generically; overrides:
}


def slugify(make, model):
    s = f"{make} {model}".lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    s = re.sub(r"_+", "_", s)
    return s


def exiv2_keys(path, keys):
    cmd = ["exiv2"] + [x for k in keys for x in ("-K", k)] + [path]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except Exception:
        return {}
    out = {}
    for line in r.stdout.splitlines():
        parts = line.split(None, 3)
        # Exif.Image.Make  Ascii  9  FUJIFILM  -> key=parts[0]
        if len(parts) == 4:
            out.setdefault(parts[0], parts[3].strip())
    return out


def all_files():
    acc = []
    for d in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            fp = os.path.join(p, f)
            if os.path.isfile(fp) and not f.startswith("."):
                acc.append(fp)
    return acc


def parse_rational(s):
    """'1/125 s' -> (1,125); 'F8' -> None; '63.0 mm' -> 63.0."""
    m = re.match(r"\s*(\d+)\s*/\s*(\d+)", s or "")
    if m:
        return (int(m.group(1)), int(m.group(2)))
    return None


def main():
    files = all_files()
    print(f"files: {len(files)}", flush=True)

    # Phase 1: Make/Model per file (fast, 3 keys)
    def mm(fp):
        d = exiv2_keys(fp, ["Exif.Image.Make", "Exif.Image.Model"])
        return fp, d.get("Exif.Image.Make", ""), d.get("Exif.Image.Model", "")

    groups = defaultdict(list)
    with ThreadPoolExecutor(max_workers=8) as ex:
        for fp, make, model in ex.map(mm, files):
            if not make and not model:
                groups[("UNKNOWN", "UNKNOWN")].append(fp)
            else:
                groups[(make, model)].append(fp)
    print(f"models: {len(groups)}", flush=True)

    # Phase 2: full keys per file (pools)
    filemeta = {}

    def full(fp):
        return fp, exiv2_keys(fp, KEYS)

    with ThreadPoolExecutor(max_workers=8) as ex:
        for i, (fp, d) in enumerate(ex.map(full, files)):
            filemeta[fp] = d
            if i % 400 == 0:
                print(f"  meta {i}/{len(files)}", flush=True)

    os.makedirs("/tmp/opencode", exist_ok=True)
    used_slugs = {}
    index = []
    skipped = []

    for (make, model), fps in sorted(groups.items()):
        if (make, model) in SKIP_MODELS or (make, model) == ("UNKNOWN", "UNKNOWN"):
            skipped.append({"make": make, "model": model,
                            "reason": "placeholder/unknown model",
                            "files": [os.path.relpath(f, BASE) for f in fps]})
            continue
        raws = [f for f in fps
                if os.path.splitext(f)[1].lower() in RAW_EXTS]
        if not raws:
            skipped.append({"make": make, "model": model,
                            "reason": "no true RAW file (heic/jpg only)",
                            "files": [os.path.relpath(f, BASE) for f in fps]})
            continue
        # representative: prefer .dng (richest calibration), then first raw
        dngs = [f for f in raws if f.lower().endswith(".dng")]
        rep = sorted(dngs or raws)[0]

        metas = [filemeta[f] for f in fps if f in filemeta]
        softwares = sorted({m.get("Exif.Image.Software", "")
                            for m in metas if m.get("Exif.Image.Software")})
        lenses = sorted({(m.get("Exif.Photo.LensMake", ""),
                          m.get("Exif.Photo.LensModel", ""))
                         for m in metas if m.get("Exif.Photo.LensModel")})
        isos = sorted({m.get("Exif.Photo.ISOSpeedRatings", "")
                       for m in metas if m.get("Exif.Photo.ISOSpeedRatings")})
        exps = sorted({m.get("Exif.Photo.ExposureTime", "")
                       for m in metas if m.get("Exif.Photo.ExposureTime")})
        fnums = sorted({m.get("Exif.Photo.FNumber", "")
                        for m in metas if m.get("Exif.Photo.FNumber")})
        focals = sorted({m.get("Exif.Photo.FocalLength", "")
                         for m in metas if m.get("Exif.Photo.FocalLength")})
        f35 = sorted({m.get("Exif.Photo.FocalLengthIn35mmFilm", "")
                      for m in metas
                      if m.get("Exif.Photo.FocalLengthIn35mmFilm")})
        progs = sorted({m.get("Exif.Photo.ExposureProgram", "")
                        for m in metas
                        if m.get("Exif.Photo.ExposureProgram")})
        meters = sorted({m.get("Exif.Photo.MeteringMode", "")
                         for m in metas if m.get("Exif.Photo.MeteringMode")})
        serial_keys = sorted({k for m in metas for k in m
                              if "serial" in k.lower() and m[k]})
        serial_samples = {}
        for k in serial_keys:
            vals = sorted({m[k] for m in metas if m.get(k)})
            serial_samples[k] = vals[:2]
        px = sorted({m.get("Exif.Photo.PixelXDimension", "")
                     for m in metas if m.get("Exif.Photo.PixelXDimension")})
        py = sorted({m.get("Exif.Photo.PixelYDimension", "")
                     for m in metas if m.get("Exif.Photo.PixelYDimension")})

        # geometry via identify on representative
        geom = ""
        try:
            r = subprocess.run(["identify", "-format", "%w %h",
                                rep], capture_output=True, text=True,
                               timeout=60)
            geom = r.stdout.strip()
        except Exception as e:
            geom = f"ERR {e}"

        # DNG calibration via tifffile
        calib = None
        if rep.lower().endswith(".dng"):
            calib = harvest_dng(rep)

        slug = slugify(make, model)
        if slug in used_slugs:
            slug = f"{slug}_{len(used_slugs)}"
        used_slugs[slug] = (make, model)

        data = {
            "slug": slug, "make": make, "model": model,
            "representative": os.path.relpath(rep, BASE),
            "n_files": len(fps),
            "all_files": sorted(os.path.relpath(f, BASE) for f in fps),
            "softwares": softwares,
            "lenses": [{"make": a, "model": b} for a, b in lenses],
            "iso_observed": isos, "exposure_observed": exps,
            "fnumber_observed": fnums, "focal_observed": focals,
            "focal35_observed": f35,
            "exposure_program_observed": progs,
            "metering_observed": meters,
            "serial_keys_present": serial_keys,
            "serial_samples": serial_samples,
            "pixel_dimensions": {"x": px, "y": py},
            "identify_geometry": geom,
            "dng_calibration": calib,
        }
        index.append(data)

    with open("/tmp/opencode/harvest_index.json", "w") as f:
        json.dump({"profiles": index, "skipped": skipped}, f, indent=1)
    print(f"profiles: {len(index)} skipped: {len(skipped)}", flush=True)
    for s in skipped:
        print(f"SKIP {s['make']!r} {s['model']!r}: {s['reason']}", flush=True)


def harvest_dng(path):
    try:
        import tifffile
    except ImportError:
        return {"error": "tifffile unavailable"}
    try:
        import numpy as _np
    except ImportError:
        _np = None

    def conv(v, depth=0):
        if _np is not None and isinstance(v, _np.ndarray):
            if v.size > 16:
                import hashlib as _hl
                return {"len": int(v.size),
                        "sha1_prefix": _hl.sha1(
                            v.tobytes()).hexdigest()[:16]}
            return conv(v.tolist(), depth + 1)
        if _np is not None and isinstance(v, _np.generic):
            return v.item()
        if isinstance(v, bytes):
            if len(v) > 64:
                import hashlib as _hl
                return {"bytes_len": len(v),
                        "sha1_prefix": _hl.sha1(v).hexdigest()[:16],
                        "hex_prefix": v[:32].hex()}
            return {"hex": v.hex()}
        if isinstance(v, tuple):
            return [conv(x, depth + 1) for x in v]
        if isinstance(v, list):
            return [conv(x, depth + 1) for x in v]
        if isinstance(v, int) and not isinstance(v, bool):
            return v
        if isinstance(v, float):
            return v
        if isinstance(v, str):
            return v[:300]
        return str(v)[:300]

    try:
        with tifffile.TiffFile(path) as tif:
            pg = tif.pages[0]
            tags = pg.tags
            out = {"ifd0": {}, "raw": {}}

            def rat(v):
                if isinstance(v, (tuple, list)) and len(v) == 2 and \
                        all(isinstance(x, int) for x in v):
                    return [v[0], v[1]]
                return str(v)[:120]

            def mat(v):
                try:
                    flat = list(v)
                    nums = []
                    for x in flat:
                        if isinstance(x, (tuple, list)):
                            nums.extend(int(y) for y in x)
                        else:
                            nums.append(int(x))
                    if len(nums) % 2:
                        raise ValueError("odd")
                    return [[nums[i], nums[i + 1]]
                            for i in range(0, len(nums), 2)]
                except Exception:
                    return str(v)[:300]

            for code in (271, 272, 272, 50706, 50707, 50708, 50721, 50722,
                         50778, 50779, 50728, 50730, 50731, 50732, 50734,
                         50735, 50736, 50739, 50741, 50780, 50738, 258):
                if code in tags:
                    v = tags[code].value
                    name = tags[code].name
                    if code in (50721, 50722, 50736):
                        out["ifd0"][name] = mat(v)
                    else:
                        out["ifd0"][name] = conv(v)
            # raw SubIFD: first CFA/LinearRaw series
            for s in tif.series:
                ph = int(s.keyframe.photometric)
                if ph in (32803, 34892):
                    kf = s.keyframe
                    for code in (258, 277, 262, 50714, 50717, 50718,
                                 50719, 50720, 50710, 50711, 50712,
                                 33421, 33422, 50738, 50780, 50781,
                                 50829, 51022, 50741, 254, 50778, 50779,
                                 50706, 50708):
                        if code in kf.tags:
                            v = kf.tags[code].value
                            if code == 51022 and isinstance(v, bytes) \
                                    and len(v) <= 4096:
                                out["raw"][kf.tags[code].name] = {
                                    "hex": v.hex()}
                            else:
                                out["raw"][kf.tags[code].name] = conv(v)
                    out["raw"]["_shape"] = list(s.shape)
                    out["raw"]["_dtype"] = str(s.dtype)
                    out["raw"]["_photometric"] = ph
                    break
            return out
    except Exception as e:
        return {"error": f"{type(e).__name__}: {str(e)[:200]}"}


main()
