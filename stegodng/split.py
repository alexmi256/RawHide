"""Split-file support: chunk one payload across numbered DNG files.

Each chunk is an independent framed payload (own magic/length/CRC), so a
short last chunk needs no padding, no end marker and no geometry games;
a missing or corrupt chunk fails loudly on its own CRC.

Naming follows the DCF spirit (Design rule for Camera File system:
sequential 4-digit file numbers, starting at 0001)::

    out.dng  ->  out0001.dng, out0002.dng, ...

Chunk set membership (shared UUID) and ordering (sequence number, plus
the total where the field allows it) live in DNG metadata fields chosen
to look native; ``none`` disables either field for extra stealth, in
which case decode relies purely on the filename convention.
"""
from __future__ import annotations

import os
import re
import uuid

SIZE_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]*)\s*$")
SIZE_MULTIPLIERS = {
    "": 1, "b": 1,
    "k": 1024, "kb": 1024,
    "m": 1024 ** 2, "mb": 1024 ** 2,
    "g": 1024 ** 3, "gb": 1024 ** 3,
}

# Registry of metadata fields usable for the shared chunk-set UUID.
# ImageUniqueID (EXIF 42016) is the natural default: a genuine per-image
# UUID field whose 32-char hex format fits a uuid4 hex exactly.
SPLIT_ID_FIELDS = {
    "ImageUniqueID": {"tag": 42016, "dtype": "ASCII", "ifd": "exif"},
    "ImageDescription": {"tag": 270, "dtype": "ASCII", "ifd": "ifd0"},
}

# Registry for the per-chunk sequence field. ImageNumber (TIFF/EP 9211)
# is the default: it exists precisely to number images in a sequence.
# PageNumber natively stores (sequence, total); ImageDescription stores
# "NNNN/MMMM" text.
SPLIT_SEQ_FIELDS = {
    # ImageNumber is TIFF/EP tag 0x9211 = 37393 decimal, living in the
    # EXIF sub-IFD (Exif.Photo.ImageNumber). A scalar: no total, so a
    # consecutive-from-0001 subset decodes fail-open (see README).
    "ImageNumber": {"tag": 37393, "dtype": "LONG", "count": 1, "ifd": "exif"},
    "PageNumber": {"tag": 297, "dtype": "SHORT", "count": 2, "ifd": "ifd0"},
    "ImageDescription": {"tag": 270, "dtype": "ASCII", "ifd": "ifd0"},
}

CHUNK_NAME_RE = re.compile(
    r"^(?P<stem>.*?)(?P<num>\d{4})(?P<suffix>\.[A-Za-z0-9]+)?$")


def parse_size(text: str) -> int:
    """Parse ``1g``/``100m``/``500k`` (also ``gb``/``mb``/``kb``, any case,
    decimals, bare bytes) into an integer byte count."""
    m = SIZE_RE.match(text or "")
    if not m:
        raise ValueError(
            f"invalid size {text!r}: expected like 1g, 100m, 500k "
            f"(kilobytes/megabytes/gigabytes, e.g. 2G, 100MB, 500k)")
    number, unit = m.groups()
    mult = SIZE_MULTIPLIERS.get(unit.lower())
    if mult is None:
        raise ValueError(
            f"invalid size unit {unit!r} in {text!r}: use k, m or g "
            f"(e.g. 500k, 100m, 1g)")
    size = int(float(number) * mult)
    if size <= 0:
        raise ValueError(f"split size must be positive (got {text!r})")
    return size


def chunk_path(output_path: str, seq: int) -> str:
    """``out.dng`` + chunk 1 -> ``out0001.dng`` (DCF-style 4-digit)."""
    stem, suffix = os.path.splitext(output_path)
    return f"{stem}{seq:04d}{suffix}"


def iter_chunk_bounds(payload_len: int, split_size: int):
    """Yield ``(seq, total, start, end)`` for each chunk (1-based seq).

    Lazy counterpart of ``[payload[i:i + split_size] ...]``: bounds
    only, so callers slice (and hold) one chunk copy at a time instead
    of materializing every chunk beside the full payload.
    """
    if (isinstance(split_size, bool) or not isinstance(split_size, int)
            or split_size <= 0):
        raise ValueError(
            f"split_size must be a positive byte count (got {split_size!r})")
    total = ((payload_len + split_size - 1) // split_size
             if payload_len else 1)
    for seq in range(1, total + 1):
        yield seq, total, (seq - 1) * split_size, min(seq * split_size,
                                                     payload_len)


def parse_chunk_name(path: str) -> tuple[str, int, str] | None:
    """Split a basename into (stem, number, suffix); None if no 4-digit."""
    m = CHUNK_NAME_RE.match(os.path.basename(path))
    if not m:
        return None
    return m.group("stem"), int(m.group("num")), m.group("suffix") or ""


def new_split_id() -> str:
    """Fresh shared chunk-set UUID (32 hex chars, EXIF ImageUniqueID shape)."""
    return uuid.uuid4().hex


def format_seq_value(field: str, seq: int, total: int) -> object:
    """Encode (seq, total) for a seq field (1-based)."""
    if field == "PageNumber":
        return (seq, total)
    if field == "ImageDescription":
        return f"{seq:04d}/{total:04d}"
    return seq  # ImageNumber: plain integer


def parse_seq_value(field: str, raw: object) -> tuple[int, int | None]:
    """Decode a seq field value -> (seq, total|None). Raises ValueError."""
    if field == "PageNumber":
        vals = list(raw) if isinstance(raw, (tuple, list)) else [raw]
        if len(vals) != 2:
            raise ValueError(f"PageNumber needs (seq, total), got {raw!r}")
        return int(vals[0]), int(vals[1])
    if field == "ImageDescription":
        m = re.match(r"^\s*(\d+)\s*/\s*(\d+)\s*$", str(raw))
        if not m:
            raise ValueError(
                f"cannot parse chunk sequence from {raw!r} "
                f"(expected 'NNNN/MMMM')")
        return int(m.group(1)), int(m.group(2))
    # ImageNumber: scalar or 1-tuple
    v = raw[0] if isinstance(raw, (tuple, list)) else raw
    return int(v), None


def resolve_split_fields(id_field: str, seq_field: str):
    """Validate split metadata field names.

    Returns ``(id_spec|None, seq_spec|None)`` (None == ``"none"``).
    Raises ValueError for unknown names or for using the same field
    for both (they would overwrite each other).
    """
    if id_field == "none":
        id_spec = None
    elif id_field in SPLIT_ID_FIELDS:
        id_spec = SPLIT_ID_FIELDS[id_field]
    else:
        raise ValueError(
            f"unknown split id field {id_field!r}: choose from "
            f"{sorted(SPLIT_ID_FIELDS) + ['none']} "
            f"(ImageUniqueID is the default: a genuine EXIF UUID field)")
    if seq_field == "none":
        seq_spec = None
    elif seq_field in SPLIT_SEQ_FIELDS:
        seq_spec = SPLIT_SEQ_FIELDS[seq_field]
    else:
        raise ValueError(
            f"unknown split seq field {seq_field!r}: choose from "
            f"{sorted(SPLIT_SEQ_FIELDS) + ['none']} "
            f"(ImageNumber is the default: TIFF/EP's image-sequence tag; "
            f"PageNumber stores sequence+total natively, ImageDescription "
            f"stores 'NNNN/MMMM' text)")
    if (id_spec is not None and seq_spec is not None
            and id_field == seq_field):
        raise ValueError(
            f"split id and seq fields collide on {id_field!r}: pick "
            f"different fields (e.g. id=ImageUniqueID, seq=ImageNumber)")
    return id_spec, seq_spec
