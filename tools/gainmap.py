#!/usr/bin/env python3
"""Inspect or generate DNG ``OpcodeList2`` GainMap blobs.

Usage:
    python3 tools/gainmap.py inspect IMG_0001.dng
    python3 tools/gainmap.py generate --width 4048 --height 3036 \
        --seed 7 --profile custom_pixel_xl -o opcode_list2.bin
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stegodng.opcodes import (  # noqa: E402
    GainMapConfig,
    build_opcode_list2,
    parse_opcode_list2,
    read_opcode_list2,
)


def _summary(maps) -> dict:
    return {
        "opcodes": len(maps),
        "phases": [[m.top, m.left] for m in maps],
        "bounds": [maps[0].right, maps[0].bottom],
        "grid": [maps[0].points_v, maps[0].points_h],
        "map_planes": maps[0].map_planes,
        "gain_range": [
            round(float(min(m.gains.min() for m in maps)), 6),
            round(float(max(m.gains.max() for m in maps)), 6),
        ],
        "plane_ranges": [
            [round(float(m.gains.min()), 4), round(float(m.gains.max()), 4)]
            for m in maps
        ],
    }


def cmd_inspect(args) -> int:
    blob = read_opcode_list2(args.path)
    if blob is None:
        print(f"{args.path}: no OpcodeList2")
        return 1
    maps = parse_opcode_list2(blob)
    out = _summary(maps)
    out["file_bytes"] = len(blob)
    print(json.dumps(out, indent=2))
    return 0


def cmd_generate(args) -> int:
    if args.profile:
        from stegodng.profiles import get_profile
        config = get_profile(args.profile).gainmap
        if config is None:
            print(f"{args.profile}: profile has no gainmap block", file=sys.stderr)
            return 1
    else:
        config = GainMapConfig.synthetic()
    blob = build_opcode_list2(
        args.width, args.height, seed=args.seed, config=config)
    with open(args.output, "wb") as f:
        f.write(blob)
    print(json.dumps({
        "path": args.output,
        "bytes": len(blob),
        **_summary(parse_opcode_list2(blob)),
    }, indent=2))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("inspect", help="parse OpcodeList2 from a DNG")
    p.add_argument("path")
    p.set_defaults(func=cmd_inspect)

    g = sub.add_parser("generate", help="write a synthetic OpcodeList2")
    g.add_argument("--width", type=int, default=4048)
    g.add_argument("--height", type=int, default=3036)
    g.add_argument("--seed", type=int, default=0)
    g.add_argument("--profile", default=None,
                   help="use this profile's gainmap base (default: synthetic)")
    g.add_argument("--output", "-o", required=True)
    g.set_defaults(func=cmd_generate)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
