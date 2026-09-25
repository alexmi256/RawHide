#!/usr/bin/env python3
"""Generate stegodng/profiles/<slug>/{profile.json,README.md} from harvest_index.json.

Usage: python3 tools/gen_profiles.py   (run from the repo root)
Reads /tmp/opencode/harvest_index.json (and geom_all.json), stages into
stegodng/profiles.staging, then syncs into stegodng/profiles/ without
ever touching stegodng/profiles/__init__.py (the registry loader).
"""
import json
import os
import re
import shutil
import sys
from collections import Counter

INDEX = "/tmp/opencode/harvest_index.json"
REPO = "/home/alex/.local/share/opencode/worktree/5241a7d1ac4ca366825a7eef5700531d38754095/camera-profiles"
OUT = os.path.join(REPO, "stegodng", "profiles")
STAGE = OUT + ".staging"

# Reference pools (mirror stegodng.metadata.MetadataRandomizer).
REF_ISO = [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800,
           1000, 1250, 1600, 3200, 6400]
REF_EXP = [(10, 8000), (10, 4000), (10, 2000), (10, 1000), (10, 500),
           (10, 250), (10, 125), (10, 60), (10, 30), (10, 21), (10, 17),
           (10, 16), (10, 8), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1),
           (15, 10), (20, 10), (30, 10), (50, 10), (60, 10)]
REF_FNUM = [170, 200, 250, 280, 320, 400, 560, 710, 800, 1100, 1600, 2200,
            3200]
REF_METER = [2, 3, 5]
REF_EXPPROG = [1, 2, 3, 4]
REF_SERIAL_PREFIX = ["92A", "94A", "93A", "95A"]

MAKE_NICE = {
    "NIKON CORPORATION": "Nikon",
    "OLYMPUS CORPORATION": "Olympus",
    "OLYMPUS IMAGING CORP.": "Olympus",
    "OM Digital Solutions": "OM System",
    "RICOH IMAGING COMPANY, LTD.": "Ricoh",
    "FUJIFILM": "Fujifilm",
    "LEICA CAMERA AG": "Leica",
    "Leica Camera AG": "Leica",
    "SONY": "Sony",
    "Canon": "Canon",
    "Panasonic": "Panasonic",
    "SIGMA": "Sigma",
    "Sigma": "Sigma",
    "Hasselblad": "Hasselblad",
    "Phase One": "Phase One",
    "Apple": "Apple",
    "Google": "Google",
    "DJI": "DJI",
    "GoPro": "GoPro",
    "samsung": "Samsung",
    "vivo": "Vivo",
    "HUAWEI": "Huawei",
    "XIAOYI": "Xiaomi",
    "ZEISS": "Zeiss",
    "DxO": "DxO",
    "SEALIFE": "Sealife",
    "Skydio": "Skydio",
    "Autel Robotics": "Autel",
    "Camera Intelligence": "Camera Intelligence",
}

SONY_FRIENDLY = {
    "ILCE-7RM2": "a7R II", "ILCE-7RM3": "a7R III", "ILCE-7RM4": "a7R IV",
    "ILCE-7RM5": "a7R V", "ILCE-7RM6": "a7R VI",
    "ILCE-7M2": "a7 II", "ILCE-7M3": "a7 III", "ILCE-7M4": "a7 IV",
    "ILCE-7M5": "a7 V",
    "ILCE-7C": "a7C", "ILCE-7CM2": "a7C II", "ILCE-7CR": "a7CR",
    "ILCE-7SM2": "a7S II", "ILCE-7SM3": "a7S III",
    "ILCE-9": "a9", "ILCE-9M2": "a9 II", "ILCE-9M3": "a9 III",
    "ILCE-1": "a1", "ILCE-1M2": "a1 II",
    "ILCE-5100": "a5100", "ILCE-6100": "a6100", "ILCE-6300": "a6300",
    "ILCE-6400": "a6400", "ILCE-6500": "a6500", "ILCE-6600": "a6600",
    "ILCE-6700": "a6700",
    "ILCA-68": "a68", "ILCA-99M2": "a99 II",
    "ZV-1": "ZV-1", "ZV-1M2": "ZV-1 II", "ZV-E1": "ZV-E1",
    "ZV-E10": "ZV-E10", "ZV-E10M2": "ZV-E10 II",
    "DSC-RX100": "RX100", "DSC-RX100M5": "RX100 V",
    "DSC-RX100M6": "RX100 VI", "DSC-RX100M7": "RX100 VII",
    "DSC-RX10M3": "RX10 III", "DSC-RX10M4": "RX10 IV",
    "DSC-RX10M5": "RX10 V",
    "DSC-RX1RM2": "RX1R II", "DSC-RX1RM3": "RX1R III",
}

SHORT_MAKE = {
    "NIKON CORPORATION": "nikon",
    "OLYMPUS CORPORATION": "olympus",
    "OLYMPUS IMAGING CORP.": "olympus",
    "OM Digital Solutions": "om_system",
    "RICOH IMAGING COMPANY, LTD.": "ricoh",
    "LEICA CAMERA AG": "leica",
    "Leica Camera AG": "leica",
    "Autel Robotics": "autel",
    "Camera Intelligence": "caira",
    "Phase One": "phase_one",
}


def _slugify(make, model):
    s = f"{make} {model}".lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return re.sub(r"_+", "_", s)


def slug_for(make, model):
    """Compact slug without stutter ("Canon EOS R5" -> canon_eos_r5)."""
    base = SHORT_MAKE.get(make, make.lower())
    m = model
    ml = m.lower()
    for tok in (make.lower(), make.split()[0].lower(), base,
                MAKE_NICE.get(make, make).lower()):
        if tok and (ml.startswith(tok + " ") or ml.startswith(tok + "_")
                    or ml.startswith(tok + "-") or ml == tok):
            m = m[len(tok) + 1:] if len(m) > len(tok) else ""
            ml = m.lower()
            break
    return _slugify(base, m)



def nice_make(make):
    return MAKE_NICE.get(make, make)


def display_name(make, model):
    nm = nice_make(make)
    m = model
    # strip redundant make prefixes ("NIKON Z 7" -> "Z 7")
    for tok in (make, make.split()[0], nm, nm.upper()):
        if tok and m.startswith(tok + " "):
            m = m[len(tok) + 1:]
            break
    if make == "SONY" and m in SONY_FRIENDLY:
        m = SONY_FRIENDLY[m]
    if make == "DJI" and m.startswith("FC"):
        return f"DJI {m} (drone camera unit)"
    return f"{nm} {m}"


def parse_ints(values):
    out = []
    for v in values:
        v = (v or "").strip()
        if re.fullmatch(r"\d{1,6}", v):
            out.append(int(v))
    return sorted(set(out))


def parse_exposure(values):
    out = []
    for v in values:
        m = re.match(r"\s*(\d+)\s*/\s*(\d+)", v or "")
        if m and int(m.group(2)) != 0:
            out.append((int(m.group(1)), int(m.group(2))))
            continue
        m = re.match(r"\s*(\d+(?:\.\d+)?)\s*s", v or "")
        if m:
            f = float(m.group(1))
            if f > 0:
                out.append((max(1, int(round(f * 10000))), 10000))
    return sorted(set(out), key=lambda t: t[0] / t[1] if t[1] else 0)


def parse_fnumber(values):
    out = []
    for v in values:
        m = re.match(r"\s*F?\s*(\d+(?:\.\d+)?)", v or "")
        if m:
            n = int(round(float(m.group(1)) * 100))
            if n > 0:
                out.append((n, 100))
    return sorted(set(out))


def parse_float_mm(values):
    out = []
    for v in values:
        m = re.match(r"\s*(\d+(?:\.\d+)?)", v or "")
        if m:
            out.append(float(m.group(1)))
    return sorted(set(out))


LENS_RE = re.compile(
    r"(?P<range>(?P<lo>\d+(?:\.\d+)?)\s*-\s*(?P<hi>\d+(?:\.\d+)?)|"
    r"(?P<prime>\d+(?:\.\d+)?))\s*mm.*?[Ff]\s*/?\s*(?P<ap>\d+(?:\.\d+)?)")

# "LUMIX S 20-60/F3.5-5.6", "XCD 35-100E@100": range without "mm",
# aperture optional (falls back to the observed minimum).
RANGE_RE = re.compile(
    r"(?P<lo>\d+(?:\.\d+)?)\s*-\s*(?P<hi>\d+(?:\.\d+)?)"
    r"(?:.*?[Ff]\s*/?\s*(?P<ap>\d+(?:\.\d+)?))?")

# "100mm", "20.7 mm": prime without a parseable aperture.
PRIME_RE = re.compile(
    r"(?P<f>\d+(?:\.\d+)?)\s*mm"
    r"(?:.*?[Ff]\s*/?\s*(?P<ap>\d+(?:\.\d+)?))?")

# Leica-style "SUMMILUX 1:1.7/28 ASPH.": aperture after "1:", focal after "/".
LEICA_RE = re.compile(r"1\s*:\s*(?P<ap>\d+(?:\.\d+)?)\s*/\s*(?P<f>\d+(?:\.\d+)?)")

# Bare "40/2.5" style (focal/aperture, no "mm"): last resort before the
# observed-focal fallback.
SLASH_RE = re.compile(
    r"(?P<f>\d+(?:\.\d+)?)\s*/\s*[Ff]?\s*(?P<ap>\d+(?:\.\d+)?)")

# "XCD 120": Hasselblad names are bare focal lengths in mm.
XCD_RE = re.compile(r"XCD\s+(?P<f>\d+(?:\.\d+)?)")

# "Summicron TL 1:2 23 ASPH.": focal length directly before ASPH.
ASPH_RE = re.compile(r"(?P<f>\d+(?:\.\d+)?)\s+ASPH")

# Lens names that fell back to observed focals (audit aid, printed by main).
FALLBACK_LENSES: list = []


def lens_spec(lens_make, lens_model, observed_focals,
              observed_fnumbers=None):
    """(model, min_mm, max_mm, max_aperture, make) from name parsing."""
    m = LENS_RE.search(lens_model or "")
    if m:
        if m.group("prime"):
            lo = hi = float(m.group("prime"))
        else:
            lo, hi = float(m.group("lo")), float(m.group("hi"))
        ap = float(m.group("ap"))
        return (lens_model, lo, hi, ap, lens_make or "")
    m = RANGE_RE.search(lens_model or "")
    if m:
        lo, hi = float(m.group("lo")), float(m.group("hi"))
        ap = float(m.group("ap")) if m.group("ap") else None
        return (lens_model, lo, hi, ap or _fallback_ap(observed_fnumbers),
                lens_make or "")
    m = PRIME_RE.search(lens_model or "")
    if m:
        f = float(m.group("f"))
        ap = float(m.group("ap")) if m.group("ap") else None
        return (lens_model, f, f, ap or _fallback_ap(observed_fnumbers),
                lens_make or "")
    m = LEICA_RE.search(lens_model or "")
    if m:
        f = float(m.group("f"))
        return (lens_model, f, f, float(m.group("ap")), lens_make or "")
    m = SLASH_RE.search(lens_model or "")
    if m:
        f = float(m.group("f"))
        return (lens_model, f, f, float(m.group("ap")), lens_make or "")
    m = XCD_RE.search(lens_model or "")
    if m:
        f = float(m.group("f"))
        return (lens_model, f, f, _fallback_ap(observed_fnumbers),
                lens_make or "")
    m = ASPH_RE.search(lens_model or "")
    if m:
        f = float(m.group("f"))
        return (lens_model, f, f, _fallback_ap(observed_fnumbers),
                lens_make or "")
    FALLBACK_LENSES.append(lens_model)
    if observed_focals:
        lo, hi = min(observed_focals), max(observed_focals)
        return (lens_model, round(lo, 1), round(hi, 1),
                _fallback_ap(observed_fnumbers), lens_make or "")
    return (lens_model, 50.0, 50.0, 2.8, lens_make or "")


def _fallback_ap(observed_fnumbers):
    fnums = parse_fnumber(observed_fnumbers or [])
    if fnums:
        return round(min(n / d for n, d in fnums), 1)
    return 2.8


def crop_guess(make, model, focal_obs, f35_obs):
    pairs = []
    fs = parse_float_mm(focal_obs)
    c35 = parse_ints(f35_obs)
    if fs and c35 and len(fs) == len(c35):
        for f, c in zip(sorted(fs), sorted(c35)):
            if f > 0:
                pairs.append(round(c / f, 2))
    if pairs:
        pairs.sort()
        return pairs[len(pairs) // 2]
    m = f"{make} {model}".lower()
    if any(k in m for k in ("gfx", "x2d", "cfv", "907x", "h5d", "iq4",
                            "x1d", "hasselblad")):
        return 0.79
    if any(k in m for k in ("iphone", "pixel", "galaxy", "sm-g", "vivo",
                            "eva-l", "huawei", "xiaomi", "m1")):
        return 7.0
    if any(k in m for k in ("tg-", "tough", "dc-fz", "dmc-fz", "dc-zs",
                            "dmc-zs", "dsc-rx100", "z0", "g7 x", "g9 x",
                            "g5 x", "hero", "pocket", "fc3", "fc4", "fc7",
                            "fc8", "dji", "autel", "dxo", "h5d")):
        return 2.7
    if any(k in m for k in ("e-m", "pen", "om-1", "om-3", "om-5",
                            "dc-g", "dmc-g", "dc-gh", "dc-gx", "dc-lx")):
        return 2.0
    if any(k in m for k in ("ilce-6", "zv-e10", "x-t", "x-e", "x-h",
                            "x-s", "x-a", "x-m", "x-pro", "x100", "x70",
                            "xf10", "gr iii", "gr iv", "eos m", "eos r7",
                            "eos r10", "eos r50", "eos r100", "nikon z 30",
                            "nikon z 50", "z50_2", "z fc", "d3400",
                            "d3500", "d500", "d5600", "d7500", "k-3",
                            "k-70", "kp", "k-s2", "fp l", "sd quattro",
                            "x3f", "tl2", "cl ", "sigma bf", "leica cl",
                            "fujifilm x")):
        return 1.5
    if "canon" in m and any(k in m for k in ("eos m", "eos r7", "eos r10",
                                             "eos r50", "rebel", "77d",
                                             "80d", "90d")):
        return 1.6
    return 1.0


def bitdepth_guess(make, model, dng_bps):
    if dng_bps:
        return dng_bps
    m = f"{make} {model}".lower()
    if any(k in m for k in ("gfx", "x2d", "cfv", "907x", "h5d", "iq4",
                            "x1d")):
        return 16
    return 14


def serial_prefixes(entry, is_gfx):
    samples = entry.get("serial_samples", {})
    if not samples:
        if is_gfx:
            return (list(REF_SERIAL_PREFIX),
                    "reference (combiner lineage)")
        return (["1A", "4E", "7B", "C2"],
                "generic fallback (no serial tags observed)")
    prefs = []
    for vals in samples.values():
        for v in vals:
            v = v.strip()
            if re.match(r"^[A-Z0-9]{2,4}[A-Z0-9]+$", v) and len(v) >= 5:
                p = v[:3] if v[:1].isdigit() is False or v[1:2].isalpha() \
                    else v[:2]
                prefs.append(p)
    prefs = sorted(set(prefs))[:4]
    if prefs:
        return prefs, "observed serial formats"
    return list(REF_SERIAL_PREFIX), "fallback (serials non-alphanumeric)"


def main():
    with open(INDEX) as f:
        index = json.load(f)
    profiles = index["profiles"]
    skipped = index["skipped"]
    print(f"entries: {len(profiles)} skipped: {len(skipped)}")

    # global lens fallback per mount would be overkill; per-model observed
    # lenses + observed focals feed lens_spec().
    made = []
    used = {}
    for entry in profiles:
        make, model = entry["make"], entry["model"]
        slug = slug_for(make, model)
        if slug in used:  # keep slugs unique
            slug = f"{slug}_{len(used)}"
        used[slug] = (make, model)
        d = os.path.join(STAGE, slug)
        os.makedirs(d, exist_ok=True)

        is_gfx = model.upper().replace(" ", "").startswith("GFX")
        dng = entry.get("dng_calibration") or {}
        dng_ok = bool(dng) and "error" not in dng
        ifd0 = dng.get("ifd0", {}) if dng_ok else {}
        raw = dng.get("raw", {}) if dng_ok else {}

        def pair_list(key, ref):
            v = ifd0.get(key)
            if isinstance(v, list) and len(v) == len(ref):
                try:
                    return [[int(a), int(b)] for a, b in v]
                except Exception:
                    return None
            return None

        def rational(key):
            v = ifd0.get(key)
            if isinstance(v, list) and len(v) == 2:
                try:
                    return [int(v[0]), int(v[1])]
                except Exception:
                    return None
            return None

        cm1 = pair_list("ColorMatrix1", [0] * 9)
        cm2 = pair_list("ColorMatrix2", [0] * 9)
        bn = rational("BaselineNoise")
        bs = rational("BaselineSharpness")
        lrl = rational("LinearResponseLimit")
        softwares = entry.get("softwares", [])
        # Latest observed firmware: a newly converted file most plausibly
        # carries a recent version (not a pre-production 0.x build).
        software = sorted(softwares)[-1] if softwares else ""
        if is_gfx and not (dng_ok and cm1 and cm2):
            # Combiner lineage: keep the byte-stable reference calibration.
            cm1 = cm2 = None
            bn = bs = lrl = None
            software = "FUJIFILM Pixel Shift Combiner"
            calib_source = "reference-gfx-combiner"
        elif dng_ok and cm1 and cm2:
            calib_source = "harvested-dng"
        else:
            calib_source = "exif-plus-fallback"

        dng_ver = ifd0.get("DNGVersion")
        dng_back = ifd0.get("DNGBackwardVersion")

        def _ver(v):
            if isinstance(v, dict) and isinstance(v.get("hex"), str) \
                    and len(v["hex"]) == 8:
                try:
                    return [int(v["hex"][i:i + 2], 16)
                            for i in (0, 2, 4, 6)]
                except ValueError:
                    return None
            if isinstance(v, list) and len(v) == 4 and \
                    all(isinstance(x, int) for x in v):
                return v
            return None

        dng_ver, dng_back = _ver(dng_ver), _ver(dng_back)

        bl_ref = None
        wl = raw.get("WhiteLevel")
        bl = raw.get("BlackLevel")
        try:
            if isinstance(wl, int) and isinstance(bl, list) and bl:
                bl_ref = max(
                    1, round(int(bl[0]) * 65535 / wl))
            elif isinstance(wl, list) and isinstance(bl, list) and wl and bl:
                bl_ref = max(1, round(int(bl[0]) * 65535 / int(wl[0])))
        except Exception:
            bl_ref = None
        if calib_source == "reference-gfx-combiner":
            bl_ref = None  # reference default 256 applies

        opcode = raw.get("OpcodeList3")
        opcode_hex = None
        if isinstance(opcode, dict) and opcode.get("hex"):
            opcode_hex = opcode["hex"]
        if calib_source == "reference-gfx-combiner":
            opcode_hex = None

        geom = (entry.get("identify_geometry") or "").split()
        nw, nh = None, None
        geom_note = ""
        # geom_all.json: per-model decoded-dim distributions. The mode
        # tracks the sensor; hi-res composites (tripod/pixel-shift) and
        # crop-mode files form minority clusters and are excluded from
        # the native pin (but recorded in the note).
        try:
            gall = json.load(open("/tmp/opencode/geom_all.json"))
        except Exception:
            gall = {}
        try:
            gmax = json.load(open("/tmp/opencode/geom_max.json"))
        except Exception:
            gmax = {}
        dist = gall.get(f"{make}\t{model}")
        mode = None
        largest = None
        if dist and dist.get("dims"):
            top = max(n for _, _, n in dist["dims"])
            cands = [(w, h) for w, h, n in dist["dims"] if n == top]
            # tie -> smaller area (base sensor, not composite)
            mode = min(cands, key=lambda wh: wh[0] * wh[1])
            largest = max(((w, h) for w, h, _ in dist["dims"]),
                          key=lambda wh: wh[0] * wh[1])
        dcs = raw.get("DefaultCropSize")
        dcs_wh = None
        if isinstance(dcs, list) and len(dcs) == 2 and \
                all(isinstance(x, int) for x in dcs):
            dcs_wh = (dcs[0], dcs[1])
        if dcs_wh and mode and 0.5 <= (dcs_wh[0] * dcs_wh[1] /
                                       (mode[0] * mode[1])) <= 1.1:
            nw, nh = dcs_wh
            geom_note = (f"{nw}x{nh} active area (harvested "
                         f"DefaultCropSize)")
        elif mode:
            nw, nh = mode
            n_mode = next(n for w, h, n in dist["dims"]
                          if (w, h) == mode)
            geom_note = (f"{nw}x{nh} most common decoded dims across "
                         f"{dist['n_files']} sample(s)")
            if largest and largest != mode:
                n_large = next(n for w, h, n in dist["dims"]
                               if (w, h) == largest)
                ratio = (largest[0] * largest[1]) / (nw * nh)
                if n_large < n_mode and ratio > 1.5:
                    geom_note += (f" (largest seen {largest[0]}x{largest[1]} "
                                  f"hi-res composite excluded)")
                else:
                    geom_note += (f" (also seen {largest[0]}x{largest[1]})")
        elif dcs_wh:
            nw, nh = dcs_wh
            geom_note = (f"{nw}x{nh} active area (harvested "
                         f"DefaultCropSize)")
        else:
            gm = gmax.get(f"{make}\t{model}")
            if gm:
                nw, nh = gm
                geom_note = (f"{nw}x{nh} max decoded-RAW dims across "
                             f"the model's samples (incl. masked margins)")
            elif len(geom) == 2 and all(g.isdigit() for g in geom):
                nw, nh = int(geom[0]), int(geom[1])
                geom_note = (f"{nw}x{nh} decoded representative RAW "
                             f"(incl. masked margins)")
            else:
                geom_note = "unknown"
        doc_geom = geom_note

        lenses_obs = entry.get("lenses", [])[:12]
        focals = parse_float_mm(entry.get("focal_observed", []))
        lenses = [list(lens_spec(l.get("make", ""), l.get("model", ""),
                                 focals,
                                 entry.get("fnumber_observed", [])))
                  for l in lenses_obs]
        if not lenses and focals:
            # Fixed-lens camera (compact/drone/phone) with no LensModel
            # tag: synthesize one built-in zoom from the observed focal
            # range instead of falling back to the GF pool (wrong mount).
            fnums_all = parse_fnumber(entry.get("fnumber_observed", []))
            ap = min((f[0] / f[1] for f in fnums_all), default=2.8)
            lenses = [[f"{model} built-in lens", round(min(focals), 1),
                       round(max(focals), 1), round(ap, 1),
                       MAKE_NICE.get(make, make)]]
        if not lenses:
            lenses = None  # -> reference GF pool fallback (documented)

        isos = sorted(set(parse_ints(entry.get("iso_observed", []))
                            ) | set(REF_ISO))
        exps = sorted(set(parse_exposure(entry.get("exposure_observed", []))
                            ) | set(REF_EXP),
                      key=lambda t: t[0] / t[1])
        fnums = sorted(set(parse_fnumber(entry.get("fnumber_observed", []))
                             ) | {(f, 100) for f in REF_FNUM})
        meters = sorted(set(parse_ints(entry.get("metering_observed", []))
                              ) | set(REF_METER))
        progs = sorted(set(parse_ints(
            entry.get("exposure_program_observed", []))) | set(REF_EXPPROG))

        prefs, prefs_note = serial_prefixes(entry, is_gfx)
        crop = crop_guess(make, model, entry.get("focal_observed", []),
                          entry.get("focal35_observed", []))
        bps = raw.get("BitsPerSample")
        sdepth = bitdepth_guess(make, model,
                                bps if isinstance(bps, int) else None)
        cfa = None
        cfap = raw.get("CFAPattern")
        if isinstance(cfap, dict) and cfap.get("hex") == "00010102":
            cfa = "RGGB"
        elif cfap:
            cfa = "Bayer (unidentified)"

        uniq = model
        prof = {
            "schema": 1,
            "slug": slug,
            "display_name": display_name(make, model),
            "make": make,
            "model": model,
            "unique_camera_model": uniq,
            "software": software,
            "dng_version": dng_ver,
            "dng_backward": dng_back,
            "color_matrix1": cm1,
            "color_matrix2": cm2,
            "calib_illuminant1": 17,
            "calib_illuminant2": 21,
            "baseline_noise": bn,
            "baseline_sharpness": bs,
            "linear_response_limit": lrl,
            "shadow_scale": None,
            "black_level_ref": bl_ref,
            "opcode_list3_hex": opcode_hex,
            "native_width": nw,
            "native_height": nh,
            "native_geometry_note": doc_geom,
            "suggested_bit_depth": sdepth,
            "cfa_pattern": cfa,
            "crop_factor": crop,
            "lenses": lenses,
            "iso_choices": isos or None,
            "exposure_choices": [list(e) for e in exps] or None,
            "fnumber_choices": [list(f) for f in fnums] or None,
            "metering_choices": meters or None,
            "exposure_program_choices": progs or None,
            "serial_prefixes": prefs,
            "serial_prefixes_note": prefs_note,
            "subprofiles": ({"native": {"width": nw, "height": nh,
                                        "description":
                                        "native sensor geometry"}}
                            if nw and nh else {}),
            "calibration_source": calib_source,
            "sample_files": entry.get("all_files", []),
            "representative": entry.get("representative", ""),
        }
        with open(os.path.join(d, "profile.json"), "w") as f:
            json.dump(prof, f, indent=2)
            f.write("\n")
        with open(os.path.join(d, "README.md"), "w") as f:
            f.write(render_readme(prof, entry))
        made.append((slug, prof["display_name"], calib_source,
                     entry.get("n_files", 0)))

    # index page
    with open(os.path.join(STAGE, "PROFILES.md"), "w") as f:
        f.write("# Camera profiles\n\n")
        f.write(f"{len(made)} profiles harvested from `dpreview-raw` "
                f"samples. Base usage: `--camera-profile=<slug>`; "
                f"append `-native` to pin the native geometry "
                f"(e.g. `--camera-profile=sony_ilce_7rm5-native`). "
                f"`gfx_100` additionally offers `-pixelshift`.\n\n")
        f.write("| profile | camera | calibration | samples |\n")
        f.write("|---|---|---|---|\n")
        for slug, disp, src, n in sorted(made):
            f.write(f"| `{slug}` | {disp} | {src} | {n} |\n")
        f.write("\n## Skipped (no usable RAW data)\n\n")
        for s in skipped:
            f.write(f"- {s['make']!r} {s['model']!r}: {s['reason']}\n")
    print(f"wrote {len(made)} profiles")
    if FALLBACK_LENSES:
        print(f"lens name fallbacks ({len(FALLBACK_LENSES)}):")
        for name in sorted(set(FALLBACK_LENSES)):
            print(f"  {name}")
    sync_staging({slug for slug, _, _, _ in made})


def sync_staging(slugs: set) -> None:
    """Sync staged profiles into stegodng/profiles/.

    Copies each staged slug dir + PROFILES.md over; removes profile dirs
    that no longer exist upstream. Never touches __init__.py (file, not
    dir) or __pycache__.
    """
    os.makedirs(OUT, exist_ok=True)
    for slug in sorted(slugs):
        shutil.copytree(os.path.join(STAGE, slug),
                        os.path.join(OUT, slug), dirs_exist_ok=True)
    shutil.copy2(os.path.join(STAGE, "PROFILES.md"),
                 os.path.join(OUT, "PROFILES.md"))
    for child in sorted(os.listdir(OUT)):
        full = os.path.join(OUT, child)
        if os.path.isdir(full) and child not in slugs \
                and child != "__pycache__":
            shutil.rmtree(full)
            print(f"removed stale profile dir: {child}")
    shutil.rmtree(STAGE, ignore_errors=True)
    print(f"synced {len(slugs)} profiles into stegodng/profiles/")


def render_readme(prof, entry):
    l = []
    A = l.append
    A(f"# {prof['display_name']}\n")
    A(f"Profile slug: `{prof['slug']}`  \n"
      f"EXIF Make/Model: `{prof['make']}` / `{prof['model']}`\n")
    A(f"Native geometry: {prof['native_geometry_note'] or 'unknown'}  \n"
      f"Suggested bit depth: {prof['suggested_bit_depth']}  \n"
      f"CFA: {prof['cfa_pattern'] or 'unknown'}  \n"
      f"Crop factor: {prof['crop_factor']}  \n"
      f"Calibration source: `{prof['calibration_source']}`\n")
    A("\n## Sample metadata (from dpreview-raw)\n")
    A(f"Representative file: `{prof['representative']}`\n")
    A(f"Files seen: {entry.get('n_files')} "
      f"({', '.join(entry.get('all_files', [])[:4])}"
      f"{', ...' if entry.get('n_files', 0) > 4 else ''})\n")
    A(f"Software strings observed: "
      f"{', '.join(entry.get('softwares', [])) or 'none'}\n")
    A(f"Lenses observed: "
      f"{'; '.join(x['model'] for x in entry.get('lenses', [])) or 'none'}\n")
    A(f"ISO observed: {', '.join(entry.get('iso_observed', [])) or 'none'}\n")
    A(f"Exposure observed: "
      f"{', '.join(entry.get('exposure_observed', [])) or 'none'}\n")
    A(f"F-number observed: "
      f"{', '.join(entry.get('fnumber_observed', [])) or 'none'}\n")
    A(f"Focal length observed: "
      f"{', '.join(entry.get('focal_observed', [])) or 'none'}\n")
    if entry.get("pixel_dimensions", {}).get("x"):
        A(f"EXIF PixelDimensions observed: "
          f"{'/'.join(entry['pixel_dimensions']['x'])} x "
          f"{'/'.join(entry['pixel_dimensions']['y'])}\n")
    if entry.get("serial_keys_present"):
        A(f"Serial tags present: "
          f"{', '.join(entry['serial_keys_present'])} "
          f"({prof['serial_prefixes_note']})\n")
    else:
        A("Serial tags present: none "
          f"({prof['serial_prefixes_note']})\n")
    dng = entry.get("dng_calibration") or {}
    if dng and "error" not in dng:
        A("\n## Harvested DNG calibration\n")
        for k, v in dng.get("ifd0", {}).items():
            A(f"- IFD0 {k}: {json.dumps(v)[:160]}\n")
        for k, v in dng.get("raw", {}).items():
            A(f"- raw {k}: {json.dumps(v)[:160]}\n")
    elif dng.get("error"):
        A(f"\nDNG calibration: unavailable ({dng['error']})\n")
    A("\n## Static fields (identical in every output file)\n")
    A(f"- Make `{prof['make']}`, Model `{prof['model']}`, "
      f"UniqueCameraModel `{prof['unique_camera_model']}`, "
      f"Software `{prof['software']}`\n")
    A(f"- DNGVersion {prof['dng_version'] or 'default 1.4'}, "
      f"CalibrationIlluminants "
      f"{prof['calib_illuminant1']}/{prof['calib_illuminant2']}\n")
    A(f"- ColorMatrix1/2: "
      f"{'harvested from DNG' if prof['color_matrix1'] else 'GFX reference fallback'}\n")
    A(f"- BlackLevel ref {prof['black_level_ref'] or 256} "
      f"(scaled per bit depth); OpcodeList3: "
      f"{'harvested' if prof['opcode_list3_hex'] else 'GFX reference fallback'}\n")
    A("\n## Randomized per file (seeded)\n")
    A(f"- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)\n")
    A(f"- ExposureTime pool: "
      f"{prof['exposure_choices'] or 'reference defaults'}\n")
    A(f"- FNumber pool: {prof['fnumber_choices'] or 'reference defaults'}\n")
    A(f"- ISO pool: {prof['iso_choices'] or 'reference defaults'}\n")
    A(f"- Lens pool ({len(prof['lenses']) if prof['lenses'] else 'reference GF pool fallback'}): "
      f"{'; '.join(x[0] for x in (prof['lenses'] or []))[:200] or 'GF reference lenses'}\n")
    A(f"- FocalLength + 35mm equivalent (x{prof['crop_factor']}), "
      f"Metering {prof['metering_choices'] or 'defaults'}, "
      f"ExposureProgram {prof['exposure_program_choices'] or 'defaults'}\n")
    A(f"- Camera/lens serials (prefixes {prof['serial_prefixes']}), "
      f"ImageNumber, AsShotNeutral, BaselineExposure, Brightness, "
      f"ExposureBias\n")
    A("\n## Sub-profiles\n")
    if prof["subprofiles"]:
        for name, g in prof["subprofiles"].items():
            A(f"- `{prof['slug']}-{name}`: pins {g['width']}x{g['height']} "
              f"({g['description']})\n")
    else:
        A("(none: native geometry unknown, base profile auto-sizes)\n")
    A(f"\nBase `--camera-profile={prof['slug']}` auto-sizes like the "
      f"default profile but stamps this camera's Make/Model/lenses.\n")
    A("\n## Plausible-deniability notes\n")
    A("Output is a converted-to-DNG story: the payload carrier claims "
      "whatever RAW the user converted. Fidelity limits an inspector "
      "could spot:\n")
    if prof["calibration_source"] == "exif-plus-fallback":
        A("- Color matrices / opcode list are GFX reference values, not "
          "this camera's: a forensic comparison against Adobe DNG "
          "Converter output for this body would mismatch.\n")
    if not prof["lenses"]:
        A("- No lens observed in samples: GF reference lens pool is used, "
          "which mismatches this mount (visible in LensModel).\n")
    A("- Native geometry includes masked margins; exact active-area "
      "dimensions may differ by a few dozen pixels.\n")
    return "".join(l)


main()
