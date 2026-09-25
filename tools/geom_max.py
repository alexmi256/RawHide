#!/usr/bin/env python3
"""Decoded-RAW geometry distribution per camera model.

identify(1) decodes some formats at preview size, but per-model the
*mode* of decoded dims tracks the sensor while hi-res composites
(OM-1 80 MP tripod mode, pixel-shift multis) and crop-mode files form
minority clusters. 8 workers, ~10 min for ~1700 files.

Writes <outdir>/geom_all.json:
  {"MAKE\\tMODEL": {"dims": [[w, h, count], ...], "n_files": N}}

Regen flow: run from the repo root, then run tools/gen_profiles.py,
which stages into stegodng/profiles.staging and syncs (never deletes
stegodng/profiles/__init__.py).
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

BASE = "/home/alex/PycharmProjects/ImageSteg2/dpreview-raw"
INDEX = sys.argv[1] if len(sys.argv) > 1 else "/tmp/opencode/harvest_index.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/opencode/geom_all.json"


def dims(fp):
    try:
        r = subprocess.run(["identify", "-format", "%w %h", fp],
                           capture_output=True, text=True, timeout=60)
        m = re.match(r"\s*(\d+)\s+(\d+)", r.stdout)
        if m:
            return fp, (int(m.group(1)), int(m.group(2)))
    except Exception:
        pass
    return fp, None


def main():
    index = json.load(open(INDEX))
    # map file -> (make, model)
    owner = {}
    for e in index["profiles"]:
        for f in e["all_files"]:
            owner[f] = (e["make"], e["model"])
    files = sorted(owner)
    print(f"files: {len(files)}", flush=True)
    dist: dict = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for i, (fp, wh) in enumerate(ex.map(dims, [os.path.join(BASE, f)
                                                   for f in files])):
            rel = os.path.relpath(fp, BASE)
            if wh:
                dist.setdefault(owner[rel], Counter())[wh] += 1
            if i % 400 == 0:
                print(f"  {i}/{len(files)}", flush=True)
    out = {}
    for k, c in dist.items():
        total = sum(c.values())
        out[f"{k[0]}\t{k[1]}"] = {
            "dims": [[w, h, n] for (w, h), n in
                     sorted(c.items(), key=lambda kv: -kv[1])],
            "n_files": total,
        }
    json.dump(out, open(OUT, "w"), indent=1)
    multi = sum(1 for v in out.values() if len(v["dims"]) > 1)
    print(f"models with geometry: {len(out)} "
          f"({multi} with >1 distinct dims)", flush=True)


main()
