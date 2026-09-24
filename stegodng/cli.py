"""Command-line interface: ``encode`` / ``decode`` / ``capacity`` / ``gen-tiff``."""
from __future__ import annotations

import argparse
import sys

from .codec import capacity_bytes, format_kb
from .container import DngContainer
from .profile import (
    GFX_NATIVE_H,
    GFX_NATIVE_W,
    MAX_FRAMES,
    MAX_LSB_PLANES,
    PIXELSHIFT_H,
    PIXELSHIFT_W,
)
from .sizing import recommend, risk_warnings
from .split import (
    SPLIT_ID_FIELDS,
    SPLIT_SEQ_FIELDS,
    chunk_path,
    parse_chunk_name,
    parse_size,
)
from .stego import decode, encode, encode_split, generate_tiff


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="RAW DNG image steganography")
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("encode", help="embed a file into a new DNG")
    e.add_argument("--input", "-i", required=True)
    e.add_argument("--output", "-o", required=True)
    e.add_argument("--width", type=int, default=None,
                   help="raw image width (default: auto from input size)")
    e.add_argument("--height", type=int, default=None,
                   help="raw image height (default: auto from input size)")
    e.add_argument("--seed", type=int, default=None)
    e.add_argument("--key", default=None, help="passphrase for payload encryption")
    e.add_argument("--lsb-planes", type=int, default=None,
                   choices=tuple(range(1, MAX_LSB_PLANES + 1)),
                   help="LSB planes used (default: fewest fitting the input; "
                   "capacity scales linearly; 3+ degrade the cover, 9+ "
                   "destroy most of it, 16 = samples are pure payload)")
    e.add_argument("--bit-depth", type=int, default=None, choices=(8, 10, 12, 14, 16),
                   help="packed BitsPerSample of the raw SubIFD (default: 16)")
    e.add_argument("--mode", default=None, choices=("linear", "cfa"),
                   help="raw layout (default: linear)")
    e.add_argument("--compression", default="none",
                   choices=("none", "adobe_deflate"),
                   help="raw SubIFD compression (none = widest viewer support; "
                   "adobe_deflate only with bit_depth 8/16)")
    e.add_argument("--thumbnail", default="random",
                   help="preview picture: 'random' (Wikimedia Commons photo, "
                   "noise fallback offline), 'synthetic' (built-in "
                   "gradient), or a path to an image file")
    e.add_argument("--split-file", default=None, metavar="SIZE",
                   help="split the payload into chunks of at most SIZE per "
                   "DNG (e.g. 1g, 100m, 500k, 2G, 64KB, or bytes); files "
                   "are named <stem>0001<suffix> ... (DCF-style 4-digit "
                   "sequence)")
    e.add_argument("--split-file-metadata-id", default="ImageUniqueID",
                   choices=tuple(sorted(SPLIT_ID_FIELDS) + ["none"]),
                   help="metadata field for the UUID shared by all chunks "
                   "of one split (default ImageUniqueID: a genuine EXIF "
                   "UUID field; ImageDescription also available; 'none' "
                   "writes nothing and relies on filenames)")
    e.add_argument("--split-file-metadata-seq", default="ImageNumber",
                   choices=tuple(sorted(SPLIT_SEQ_FIELDS) + ["none"]),
                   help="metadata field for the chunk sequence number "
                   "(default ImageNumber: TIFF/EP's image-sequence tag, "
                   "but it carries no total so a consecutive subset "
                   "decodes without error; PageNumber stores "
                   "sequence+total natively and fails closed, "
                   "ImageDescription stores 'NNNN/MMMM' text; 'none' "
                   "writes nothing and relies on filenames)")
    e.add_argument("--split-file-id", default=None, metavar="UUID",
                   help="override the generated chunk-set UUID (default: "
                   "fresh random per split)")
    e.add_argument("--no-randomize", action="store_true")
    e.add_argument("--gfx-native", action="store_true",
                   help=f"use {GFX_NATIVE_W}x{GFX_NATIVE_H}")
    e.add_argument("--pixelshift", action="store_true",
                   help=f"use {PIXELSHIFT_W}x{PIXELSHIFT_H} (needs lots of RAM)")
    e.add_argument("--raw-frames", type=int, default=1,
                   choices=tuple(range(1, MAX_FRAMES + 1)),
                   help="full-resolution raw SubIFDs sharing one file "
                   f"(burst/stack style, 1-{MAX_FRAMES}); capacity scales "
                   "with frames but so does file size, and multiple raw "
                   "frames are non-standard for still DNGs)")
    e.add_argument("--auto-size", action="store_true",
                   help="compute the smallest 4:3 width/height fitting the "
                   "input (smaller files, but non-standard dimensions may "
                   "look unusual under inspection; cannot be combined with "
                   "--width/--height/--gfx-native/--pixelshift)")

    d = sub.add_parser("decode", help="extract a file from DNG(s)")
    d.add_argument("--input", "-i", required=True, nargs="+",
                   help="one DNG, or several chunk files to concatenate "
                   "(verified via split metadata, else 0001-style names)")
    d.add_argument("--output", "-o", required=True)
    d.add_argument("--key", default=None)
    d.add_argument("--lsb-planes", type=int, default=None,
                   choices=tuple(range(1, MAX_LSB_PLANES + 1)),
                   help="LSB planes used at encode time (default: auto-detect)")
    d.add_argument("--split-file-metadata-id", default="ImageUniqueID",
                   choices=tuple(sorted(SPLIT_ID_FIELDS) + ["none"]),
                   help="metadata field holding the shared chunk-set UUID "
                   "(must match the encode setting)")
    d.add_argument("--split-file-metadata-seq", default="ImageNumber",
                   choices=tuple(sorted(SPLIT_SEQ_FIELDS) + ["none"]),
                   help="metadata field holding the chunk sequence "
                   "(must match the encode setting)")

    c = sub.add_parser("capacity", help="print capacity for a geometry")
    c.add_argument("--width", type=int, default=2048)
    c.add_argument("--height", type=int, default=1536)
    c.add_argument("--mode", default="linear", choices=("linear", "cfa"))
    c.add_argument("--lsb-planes", type=int, default=1,
                   choices=tuple(range(1, MAX_LSB_PLANES + 1)))
    c.add_argument("--raw-frames", type=int, default=1,
                   choices=tuple(range(1, MAX_FRAMES + 1)))

    t = sub.add_parser("gen-tiff", help="generate a plain TIFF cover")
    t.add_argument("--output", "-o", required=True)
    t.add_argument("--width", type=int, default=2048)
    t.add_argument("--height", type=int, default=1536)
    t.add_argument("--seed", type=int, default=None)

    args = ap.parse_args(argv)
    if args.cmd == "encode":
        if args.auto_size and (args.width is not None
                               or args.height is not None
                               or args.gfx_native or args.pixelshift):
            ap.error("--auto-size cannot be combined with "
                     "--width/--height/--gfx-native/--pixelshift")
        w, h = args.width, args.height
        if args.gfx_native:
            w, h = GFX_NATIVE_W, GFX_NATIVE_H
        if args.pixelshift:
            w, h = PIXELSHIFT_W, PIXELSHIFT_H
        with open(args.input, "rb") as f:
            payload = f.read()
        split_size = None
        if args.split_file is not None:
            try:
                split_size = parse_size(args.split_file)
            except ValueError as exc:
                print(f"error: {exc}", file=sys.stderr)
                return 1
        try:
            cfg = recommend(
                split_size if split_size is not None else len(payload),
                width=w, height=h, mode=args.mode,
                bit_depth=args.bit_depth, lsb_planes=args.lsb_planes,
                auto_size=args.auto_size, frames=args.raw_frames,
            )
            scope = (f"per {format_kb(split_size)} chunk "
                     f"(from {format_kb(len(payload))} input)"
                     if split_size is not None else
                     f"for {format_kb(len(payload))} input")
            if cfg["auto"]:
                print(f"auto-config ({', '.join(cfg['auto'])}): "
                      f"{cfg['width']}x{cfg['height']} {cfg['mode']} "
                      f"{cfg['bit_depth']}-bit, "
                      f"{cfg['lsb_planes']} LSB plane(s), "
                      f"capacity {format_kb(cfg['capacity'])} {scope}")
            if cfg["preset"] == "auto-size":
                print(f"warning: --auto-size chose non-standard dimensions "
                      f"{cfg['width']}x{cfg['height']} (no GFX preset "
                      f"matches); the file is smaller, but unusual "
                      f"dimensions may look suspicious under inspection.")
            for line in risk_warnings(cfg, key=bool(args.key)):
                print(line)
            key_bytes = args.key.encode() if args.key else None
            common = dict(
                width=cfg["width"], height=cfg["height"], seed=args.seed,
                key=key_bytes, lsb_planes=cfg["lsb_planes"],
                bit_depth=cfg["bit_depth"], mode=cfg["mode"],
                compression=args.compression,
                no_randomize=args.no_randomize, frames=cfg["frames"],
                thumbnail=args.thumbnail,
            )
            if split_size is not None:
                infos = encode_split(
                    payload, args.output, split_size,
                    split_id=args.split_file_id,
                    split_id_field=args.split_file_metadata_id,
                    split_seq_field=args.split_file_metadata_seq,
                    **common,
                )
            else:
                infos = [encode(
                    payload, args.output, **common,
                )]
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        if len(infos) == 1 and "chunk_seq" not in infos[0]:
            info = infos[0]
            if info["bigtiff"]:
                print("warning: raw data exceeds classic TIFF limits; written "
                      "as 64-bit BigTIFF (DNG 1.6). tifffile reads it, but "
                      "some tools (e.g. exiv2) cannot parse BigTIFF.")
            print(f"wrote {info['path']} ({format_kb(info['size'])})")
            print(f"payload {format_kb(info['payload_len'])} / "
                  f"capacity {format_kb(info['capacity'])}")
        else:
            total = infos[0]["chunk_total"]
            idf = infos[0]["split_id_field"]
            seqf = infos[0]["split_seq_field"]
            if any(i["bigtiff"] for i in infos):
                print("warning: raw data exceeds classic TIFF limits; written "
                      "as 64-bit BigTIFF (DNG 1.6). tifffile reads it, but "
                      "some tools (e.g. exiv2) cannot parse BigTIFF.")
            for info in infos:
                print(f"wrote {info['path']} "
                      f"(chunk {info['chunk_seq']}/{total}, "
                      f"{format_kb(info['payload_len'])} of "
                      f"{format_kb(len(payload))})")
            if idf == "none" and seqf == "none":
                print("note: no split markers written to metadata; keep the "
                      "0001-style filenames so decode can order the chunks.")
            else:
                print(f"note: chunks share {idf}={infos[0]['split_id']} "
                      f"(links the set; use --split-file-metadata-id none "
                      f"to avoid it)"
                      if idf != "none" else
                      "note: no shared chunk-set UUID written "
                      "(--split-file-metadata-id none)")
                if seqf == "none":
                    print("note: no sequence numbers in metadata; decode "
                          "orders by filename.")
        for info in infos:
            print(f"thumbnail: {info['path']}: {info['thumbnail']}")
        info = infos[0]
        print(f"meta: {info['metadata']['datetime']} ISO{info['metadata']['iso']} "
              f"{info['metadata']['lens']} S/N {info['metadata']['camera_serial']}")
    elif args.cmd == "decode":
        try:
            payload = decode(
                args.input,
                key=args.key.encode() if args.key else None,
                lsb_planes=args.lsb_planes,
                split_id_field=args.split_file_metadata_id,
                split_seq_field=args.split_file_metadata_seq,
            )
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        with open(args.output, "wb") as f:
            f.write(payload)
        print(f"recovered {format_kb(len(payload))} -> {args.output}")
        if len(args.input) > 1:
            # Fail-open warning: seq fields like ImageNumber carry no
            # total, so a consecutive subset decodes without error.
            try:
                marks = [DngContainer(p).split_markers(
                    args.split_file_metadata_id,
                    args.split_file_metadata_seq) for p in args.input]
            except ValueError:
                marks = []
            if marks and not any(m["total"] is not None for m in marks):
                print("note: no chunk totals found in metadata "
                      f"({args.split_file_metadata_seq} carries sequence "
                      f"numbers only); assuming the given files are the "
                      f"complete set. Use --split-file-metadata-seq "
                      f"PageNumber at encode time to fail closed.")
    elif args.cmd == "capacity":
        n = (args.width * args.height * (3 if args.mode == "linear" else 1)
             * args.raw_frames)
        print(f"samples: {n}")
        print(f"capacity ({args.lsb_planes} LSB plane(s)"
              f"{f' x {args.raw_frames} frames' if args.raw_frames > 1 else ''}): "
              f"{format_kb(capacity_bytes(n, args.lsb_planes))}")
    elif args.cmd == "gen-tiff":
        generate_tiff(args.output, args.width, args.height, args.seed)
        print(f"wrote {args.output}")
    return 0
