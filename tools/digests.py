#!/usr/bin/env python3
"""Inspect and verify the raw image digests of a DNG.

Usage:
    python3 tools/digests.py verify IMG_0001.dng
    python3 tools/digests.py makernote IMG_0001.dng

``verify`` decodes the raw image, recomputes ``NewRawImageDigest``
(tag 51111) and ``RawDataUniqueID`` (tag 50781) with the DNG SDK rules
and reports whether they match the stored tags.  ``makernote`` prints the
MakerNote envelope (length, constant prefix, byte entropy) used by the
profile's ``fidelity.makernote`` block.

Requires ``rawpy`` only when tifffile cannot decode the raw image itself
(e.g. lossless-JPEG tiles).
"""
from __future__ import annotations

import argparse
import collections
import math
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stegodng.digests import (  # noqa: E402
    NEW_RAW_IMAGE_DIGEST_TAG,
    RAW_DATA_UNIQUE_ID_TAG,
    new_raw_image_digest,
    raw_data_unique_id,
)

_TYPE_SIZE = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 6: 1, 7: 1, 8: 2, 9: 4,
              10: 8, 11: 4, 12: 8, 13: 4}


def _ifd(data: bytes, offset: int) -> dict[int, tuple[int, int, bytes]]:
    count = struct.unpack_from("<H", data, offset)[0]
    tags: dict[int, tuple[int, int, bytes]] = {}
    for index in range(count):
        base = offset + 2 + index * 12
        code, dtype, n = struct.unpack_from("<HHI", data, base)
        size = _TYPE_SIZE[dtype] * n
        value_at = base + 8 if size <= 4 else struct.unpack_from(
            "<I", data, base + 8)[0]
        tags[code] = (dtype, n, data[value_at:value_at + size])
    return tags


def _rationals(raw: bytes) -> tuple[tuple[int, int], ...]:
    return tuple((struct.unpack_from("<I", raw, i * 8)[0],
                  struct.unpack_from("<I", raw, i * 8 + 4)[0])
                 for i in range(len(raw) // 8))


def _raw_array(path: str):
    try:
        from stegodng.container import DngContainer
        frames = DngContainer(path).raw_frames()
        if frames:
            return frames[0]
    except Exception:  # pragma: no cover - decoder specific
        pass
    try:
        import rawpy
    except ImportError:
        return None
    with rawpy.imread(path) as raw:
        return raw.raw_image.copy()


def _makernote(data: bytes) -> bytes | None:
    ifd0 = _ifd(data, struct.unpack_from("<I", data, 4)[0])
    if 34665 not in ifd0:
        return None
    exif = _ifd(data, struct.unpack("<I", ifd0[34665][2][:4])[0])
    if 37500 not in exif:
        return None
    return exif[37500][2]


def cmd_verify(args) -> int:
    data = open(args.path, "rb").read()
    ifd0 = _ifd(data, struct.unpack_from("<I", data, 4)[0])
    if 330 not in ifd0:
        print(f"{args.path}: no SubIFD raw image", file=sys.stderr)
        return 1
    sub = _ifd(data, struct.unpack("<I", ifd0[330][2][:4])[0])
    raw = _raw_array(args.path)
    if raw is None:
        print("cannot decode the raw image (install rawpy)", file=sys.stderr)
        return 1
    digest = new_raw_image_digest(raw)
    stored_digest = ifd0.get(NEW_RAW_IMAGE_DIGEST_TAG, (0, 0, b""))[2]
    unique_id = raw_data_unique_id(
        digest, ifd0[50708][2].decode("ascii").rstrip("\x00"),
        crop_size=_rationals(sub[50720][2]),
        crop_origin=_rationals(sub[50719][2]),
        user_crop=_rationals(sub.get(51125, (0, 0, b""))[2])
        if 51125 in sub else ((0, 1), (0, 1), (1, 1), (1, 1)),
        opcode_lists=(None, sub.get(51009, (0, 0, b""))[2] or None,
                      sub.get(51022, (0, 0, b""))[2] or None),
    )
    stored_uid = ifd0.get(RAW_DATA_UNIQUE_ID_TAG, (0, 0, b""))[2]
    print(f"raw             {raw.shape[1]}x{raw.shape[0]} "
          f"{raw.dtype}")
    print(f"NewRawImageDigest  computed {digest.hex()}  "
          f"stored {stored_digest.hex() or '-'}  "
          f"{'MATCH' if digest == stored_digest else 'DIFFERS'}")
    print(f"RawDataUniqueID    computed {unique_id.hex()}  "
          f"stored {stored_uid.hex() or '-'}  "
          f"{'MATCH' if unique_id == stored_uid else 'DIFFERS'}")
    return 0 if digest == stored_digest and unique_id == stored_uid else 1


# The constant 15-byte head documented in the Pixel XL profile README
# (fidelity.makernote.magic + prefix_hex); checked so the report backs
# the same claim the profile makes.
HDRP_PREFIX = bytes.fromhex("4844525002ef64356d5e701e2ceae3")


def cmd_makernote(args) -> int:
    data = open(args.path, "rb").read()
    blob = _makernote(data)
    if blob is None:
        print(f"{args.path}: no MakerNote")
        return 1
    counts = collections.Counter(blob)
    entropy = -sum(n / len(blob) * math.log2(n / len(blob))
                   for n in counts.values())
    matched = 0
    while (matched < min(len(HDRP_PREFIX), len(blob))
           and blob[matched] == HDRP_PREFIX[matched]):
        matched += 1
    print(f"length       {len(blob)}")
    print(f"head         {blob[:32].hex(' ')}")
    print(f"ascii head   {blob[:16]!r}")
    print(f"prefix match {matched}/{len(HDRP_PREFIX)} bytes")
    print(f"entropy      {entropy:.2f} bits/byte over {len(counts)} values")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify", help="recompute and compare the digests")
    v.add_argument("path")
    v.set_defaults(func=cmd_verify)

    m = sub.add_parser("makernote", help="summarize the MakerNote envelope")
    m.add_argument("path")
    m.set_defaults(func=cmd_makernote)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
