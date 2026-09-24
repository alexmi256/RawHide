"""TIFF/DNG container: XMP + EXIF builders and in-place IFD surgery.

tifffile cannot write IFD-pointer tags (ExifTag 34665) or LinearRaw
photometrics for RGB-shaped data, so :class:`DngContainer` finishes the
file after writing: it rewrites a same-size dummy tag into the ExifTag
link, appends the EXIF Sub-IFD, and patches SubIFD photometrics. Both
classic TIFF and 64-bit BigTIFF (DNG 1.6) layouts are handled.
"""
from __future__ import annotations

import math
import struct

import tifffile


class DngContainer:
    """A written DNG file: patch photometrics, attach EXIF, read raws."""

    LINEAR_RAW = 34892
    CFA = 32803

    def __init__(self, path: str) -> None:
        self.path = path

    # -- reading ------------------------------------------------------
    def raw_frames(self) -> list:
        """Raw SubIFD pixel arrays in file order (thumbnail excluded).

        Note: tifffile merges identical SubIFDs into a single series
        (e.g. shape ``(N, H, W, C)``), so one array may hold several
        frames. C-order flattening preserves write order either way,
        which is what the striped bitstream relies on.
        """
        with tifffile.TiffFile(self.path) as tif:
            return [s.asarray() for s in _raw_series_all(tif)]

    def exif(self) -> dict:
        """Parsed EXIF sub-IFD dict of IFD0."""
        with tifffile.TiffFile(self.path) as tif:
            return dict(tif.pages[0].tags[34665].value)

    def split_markers(self, id_field: str = "ImageUniqueID",
                      seq_field: str = "ImageNumber") -> dict:
        """Read split chunk markers: ``{"id", "seq", "total",
        "id_present", "seq_present"}`` (seq 1-based, total may be None).

        Raises ValueError for unknown field names or unparseable values.
        """
        from .split import SPLIT_ID_FIELDS, SPLIT_SEQ_FIELDS, parse_seq_value
        with tifffile.TiffFile(self.path) as tif:
            ifd0 = tif.pages[0]
            exif = (dict(ifd0.tags[34665].value)
                    if 34665 in ifd0.tags else {})
            out = {"id": None, "seq": None, "total": None,
                   "id_present": False, "seq_present": False}
            if id_field != "none":
                if id_field not in SPLIT_ID_FIELDS:
                    raise ValueError(
                        f"unknown split id field {id_field!r}: choose from "
                        f"{sorted(SPLIT_ID_FIELDS) + ['none']}")
                spec = SPLIT_ID_FIELDS[id_field]
                raw = (_exif_lookup(exif, spec["tag"], id_field)
                       if spec["ifd"] == "exif"
                       else ifd0.tags[spec["tag"]].value
                       if spec["tag"] in ifd0.tags else None)
                if raw is not None:
                    out["id_present"] = True
                    out["id"] = str(raw).rstrip("\x00")
            if seq_field != "none":
                if seq_field not in SPLIT_SEQ_FIELDS:
                    raise ValueError(
                        f"unknown split seq field {seq_field!r}: choose from "
                        f"{sorted(SPLIT_SEQ_FIELDS) + ['none']}")
                spec = SPLIT_SEQ_FIELDS[seq_field]
                raw = (_exif_lookup(exif, spec["tag"], seq_field)
                       if spec["ifd"] == "exif"
                       else ifd0.tags[spec["tag"]].value
                       if spec["tag"] in ifd0.tags else None)
                if raw is not None:
                    try:
                        seq, total = parse_seq_value(seq_field, raw)
                    except ValueError as exc:
                        raise ValueError(
                            f"{self.path}: {exc}") from exc
                    out["seq_present"] = True
                    out["seq"] = seq
                    out["total"] = total
            return out

    @property
    def is_bigtiff(self) -> bool:
        with open(self.path, "rb") as f:
            return _tiff_is_bigtiff(f.read(4))

    # -- post-write finishing ------------------------------------------
    def patch_linear_raw(self) -> None:
        """RGB(2) -> LinearRaw(34892) on every raw SubIFD (see module docs)."""
        _patch_linear_raw(self.path)

    def append_exif(self, meta: dict, thumb_w: int, thumb_h: int) -> None:
        """Append the EXIF Sub-IFD at EOF and link it from IFD0."""
        _append_exif(self.path, meta, thumb_w, thumb_h)


XMP_LEN = 12288


def build_xmp() -> bytes:
    core = (
        b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
        b'<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21">\n'
        b'<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
        b'<rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n'
        b"<xmp:Rating>0</xmp:Rating>\n"
        b"</rdf:Description>\n</rdf:RDF>\n</x:xmpmeta>\n"
        b'<?xpacket end="w"?>\n'
    )
    if len(core) > XMP_LEN:
        raise ValueError("XMP core too long")  # pragma: no cover
    return core + b" " * (XMP_LEN - len(core))


# ---------------------------------------------------------------------------
# EXIF Sub-IFD construction (appended at EOF, offset patched into tag 34665)
# ---------------------------------------------------------------------------

# tag -> TIFF datatype name
_EXIF_TAGS: list[tuple[int, str]] = [
    (33434, "RATIONAL"),     # ExposureTime
    (33437, "RATIONAL"),     # FNumber
    (34850, "SHORT"),        # ExposureProgram
    (34855, "SHORT"),        # ISOSpeedRatings
    (34864, "SHORT"),        # SensitivityType
    (34865, "LONG"),         # StandardOutputSensitivity
    (36864, "UNDEFINED"),    # ExifVersion
    (36867, "ASCII"),        # DateTimeOriginal
    (36868, "ASCII"),        # DateTimeDigitized
    (36880, "ASCII"),        # OffsetTime
    (36881, "ASCII"),        # OffsetTimeOriginal
    (36882, "ASCII"),        # OffsetTimeDigitized
    (37377, "SRATIONAL"),    # ShutterSpeedValue
    (37378, "RATIONAL"),     # ApertureValue
    (37379, "SRATIONAL"),    # BrightnessValue
    (37380, "SRATIONAL"),    # ExposureBiasValue
    (37381, "RATIONAL"),     # MaxApertureValue
    (37383, "SHORT"),        # MeteringMode
    (37384, "SHORT"),        # LightSource
    (37385, "SHORT"),        # Flash
    (37386, "RATIONAL"),     # FocalLength
    (37520, "ASCII"),        # SubSecTime
    (37521, "ASCII"),        # SubSecTimeOriginal
    (37522, "ASCII"),        # SubSecTimeDigitized
    (40961, "SHORT"),        # ColorSpace
    (40962, "LONG"),         # PixelXDimension
    (40963, "LONG"),         # PixelYDimension
    (41486, "RATIONAL"),     # FocalPlaneXResolution
    (41487, "RATIONAL"),     # FocalPlaneYResolution
    (41488, "SHORT"),        # FocalPlaneResolutionUnit
    (41495, "SHORT"),        # SensingMethod
    (41728, "UNDEFINED"),    # FileSource
    (41729, "UNDEFINED"),    # SceneType
    (41985, "SHORT"),        # CustomRendered
    (41986, "SHORT"),        # ExposureMode
    (41987, "SHORT"),        # WhiteBalance
    (41989, "SHORT"),        # FocalLengthIn35mmFilm
    (41990, "SHORT"),        # SceneCaptureType
    (42033, "ASCII"),        # BodySerialNumber
    (42034, "RATIONAL"),     # LensSpecification (4 rationals)
    (42035, "ASCII"),        # LensMake
    (42036, "ASCII"),        # LensModel
    (42037, "ASCII"),        # LensSerialNumber
]

_DTYPE_NUM = {"BYTE": 1, "ASCII": 2, "SHORT": 3, "LONG": 4, "RATIONAL": 5,
              "UNDEFINED": 7, "SLONG": 9, "SRATIONAL": 10}


def _exif_values(meta: dict, thumb_w: int, thumb_h: int) -> dict[int, object]:
    exp_n, exp_d = meta["exposure_time"]
    # ShutterSpeedValue ~= -log2(exposure); ApertureValue ~= 2*log2(fnumber)
    exp_val = exp_n / exp_d
    sv = (-math.log2(exp_val), 1)
    fnum = meta["fnumber"][0] / meta["fnumber"][1]
    av = (int(round(2 * math.log2(fnum) * 100)), 100)
    sv = (int(round(sv[0] * 100)), 100)
    values = {
        33434: [(exp_n, exp_d)],
        33437: [meta["fnumber"]],
        34850: [meta["exposure_program"]],
        34855: [meta["iso"]],
        34864: [1],
        34865: [meta["iso"]],
        36864: b"0230",
        36867: meta["datetime"],
        36868: meta["datetime"],
        36880: meta["offset"],
        36881: meta["offset"],
        36882: meta["offset"],
        37377: [sv],
        37378: [av],
        37379: [meta["brightness"]],
        37380: [meta["exposure_bias"]],
        37381: [meta["max_aperture"]],
        37383: [meta["metering"]],
        37384: [0],
        37385: [0],
        37386: [meta["focal_rational"]],
        37520: meta["subsec"],
        37521: meta["subsec"],
        37522: meta["subsec"],
        40961: [1],
        40962: [thumb_w],
        40963: [thumb_h],
        41486: [(913, 1)],
        41487: [(913, 1)],
        41488: [3],
        41495: [2],
        41728: b"\x03",
        41729: b"\x01",
        41985: [0],
        41986: [0],
        41987: [0],
        41989: [meta["focal_35mm"]],
        41990: [0],
        42033: meta["body_serial"],
        42034: [(meta["lens_spec"][0], meta["lens_spec"][1]),
                (meta["lens_spec"][2], meta["lens_spec"][3]),
                (meta["lens_spec"][4], meta["lens_spec"][5]),
                (meta["lens_spec"][6], meta["lens_spec"][7])],
        42035: "FUJIFILM",
        42036: meta["lens"],
        42037: meta["lens_serial"],
    }
    # Split markers (chunk-set UUID, sequence): written only on split
    # chunks. meta["split_exif"] maps tag -> value for EXIF-bound fields.
    for tag, value in meta.get("split_exif", {}).items():
        values[tag] = value
    return values


def _pack_val(dtype: str, value: object) -> tuple[int, bytes]:
    """Return (count, raw_bytes) for an EXIF value."""
    if dtype == "ASCII":
        assert isinstance(value, str)
        raw = value.encode("ascii") + b"\x00"
        return len(raw), raw
    if dtype == "UNDEFINED":
        assert isinstance(value, (bytes, bytearray))
        return len(value), bytes(value)
    if dtype == "SHORT":
        assert isinstance(value, (list, tuple))
        return len(value), struct.pack(f"<{len(value)}H", *value)
    if dtype == "LONG":
        assert isinstance(value, (list, tuple))
        return len(value), struct.pack(f"<{len(value)}I", *value)
    if dtype == "RATIONAL":
        assert isinstance(value, (list, tuple))
        return len(value), b"".join(struct.pack("<II", n, d) for n, d in value)
    if dtype == "SRATIONAL":
        assert isinstance(value, (list, tuple))
        return len(value), b"".join(struct.pack("<ii", n, d) for n, d in value)
    raise ValueError(dtype)  # pragma: no cover


SPLIT_EXIF_DTYPES = {
    42016: "ASCII",  # ImageUniqueID (split chunk-set UUID)
    37393: "LONG",  # ImageNumber (split chunk sequence)
}


def _build_exif_block(meta: dict, thumb_w: int, thumb_h: int,
                     exif_offset: int, bigtiff: bool,
                     extra_tags: list[tuple[int, str]] | None = None) -> bytes:
    """Build an EXIF Sub-IFD block with absolute offsets for `exif_offset`.

    Layout matches the container: classic TIFF uses 2-byte counts,
    12-byte entries and 4-byte offsets; BigTIFF (DNG 1.6 64-bit) uses
    8-byte counts, 20-byte entries and 8-byte offsets.
    """
    values = _exif_values(meta, thumb_w, thumb_h)
    tags = _EXIF_TAGS + (extra_tags or [])
    n = len(tags)
    field_len = 8 if bigtiff else 4
    count_fmt = "<Q" if bigtiff else "<H"
    count_len = 8 if bigtiff else 2
    entry_size = 20 if bigtiff else 12
    off_fmt = "<Q" if bigtiff else "<I"
    blobs: list[bytes] = []
    entries: list[bytes] = []
    data_start = exif_offset + count_len + entry_size * n + count_len
    cursor = data_start
    for tag, dtype in tags:
        count, raw = _pack_val(dtype, values[tag])
        if len(raw) <= field_len:
            field = raw + b"\x00" * (field_len - len(raw))
        else:
            field = struct.pack(off_fmt, cursor)
            blobs.append(raw)
            cursor += len(raw)
        entries.append(
            struct.pack("<HH" + ("Q" if bigtiff else "I")
                        + ("8s" if bigtiff else "4s"),
                        tag, _DTYPE_NUM[dtype], count, field)
        )
    return (struct.pack(count_fmt, n) + b"".join(entries)
            + struct.pack(count_fmt, 0) + b"".join(blobs))


def build_exif_block(meta: dict, thumb_w: int, thumb_h: int,
                     exif_offset: int) -> bytes:
    """Build an EXIF Sub-IFD block with absolute offsets for `exif_offset`."""
    return _build_exif_block(meta, thumb_w, thumb_h, exif_offset, False)


def _tiff_is_bigtiff(data: bytes | bytearray) -> bool:
    """True for BigTIFF (DNG 1.6 64-bit, needed past ~4 GB)."""
    return bytes(data[0:4]) == b"II+\x00"


def _ifd0_offset(data: bytes | bytearray) -> int:
    if _tiff_is_bigtiff(data):
        return struct.unpack_from("<Q", data, 8)[0]
    return struct.unpack_from("<I", data, 4)[0]


def _find_ifd_entry(data: bytes | bytearray, ifd_offset: int, tag: int):
    """Offset of the tag's directory entry (classic 12-byte or BigTIFF
    20-byte entries), or None."""
    big = _tiff_is_bigtiff(data)
    n = struct.unpack_from("<Q" if big else "<H", data, ifd_offset)[0]
    size = 20 if big else 12
    head = 8 if big else 2
    for i in range(n):
        e = ifd_offset + head + i * size
        t = struct.unpack_from("<H", data, e)[0]
        if t == tag:
            return e
    return None


def _entry_value_ptr(data: bytes | bytearray, entry: int):
    """(type, count, offset_of_value_field) for a directory entry."""
    big = _tiff_is_bigtiff(data)
    typ = struct.unpack_from("<H", data, entry + 2)[0]
    if big:
        (count,) = struct.unpack_from("<Q", data, entry + 4)
        return typ, count, entry + 12
    (count,) = struct.unpack_from("<I", data, entry + 4)
    return typ, count, entry + 8


_TYPE_SIZE = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 7: 1, 9: 4, 10: 8,
              13: 4, 16: 8, 17: 8, 18: 8}  # 13/18 need bigtiff fixup below


def _subifd_offsets(data: bytes | bytearray, ifd0: int) -> list[int]:
    """All SubIFD offsets linked from IFD0 tag 330 (one per raw frame)."""
    e = _find_ifd_entry(data, ifd0, 330)
    if e is None:  # pragma: no cover
        raise ValueError("SubIFDs tag (330) not found")
    big = _tiff_is_bigtiff(data)
    typ, count, vptr = _entry_value_ptr(data, e)
    elem = _TYPE_SIZE.get(typ, 4)
    if big and typ in (13, 18):
        elem = 8  # BigTIFF offsets are 8 bytes
    total = count * elem
    field = 8 if big else 4
    first, step = ((vptr, 8) if big else (vptr, 4)) if total > field else (vptr, 0)
    if step == 0:
        (off,) = struct.unpack_from("<Q" if big else "<I", data, vptr)
        return [off]
    (base,) = struct.unpack_from("<Q" if big else "<I", data, vptr)
    fmt = "<Q" if big else "<I"
    return [struct.unpack_from(fmt, data, base + i * step)[0]
            for i in range(count)]


def _seek_ifd_entry(f, ifd_off: int, tag: int):
    """(entry_file_offset, typ, count, value_field_off, big) for ``tag``.

    Seek-based: only the IFD header + entries are read (KBs), never the
    whole multi-GB file. Returns None when the tag is absent.
    """
    f.seek(0)
    magic = f.read(4)
    if magic[:2] != b"II" or magic[2:4] not in (b"*\x00", b"+\x00"):
        raise ValueError("not a little-endian TIFF")
    big = magic == b"II+\x00"
    f.seek(ifd_off)
    if big:
        (n,) = struct.unpack("<Q", f.read(8))
        size, head = 20, 8
    else:
        (n,) = struct.unpack("<H", f.read(2))
        size, head = 12, 2
    entries = f.read(n * size)
    for i in range(n):
        e = ifd_off + head + i * size
        (t,) = struct.unpack_from("<H", entries, i * size)
        if t == tag:
            typ = struct.unpack_from("<H", entries, i * size + 2)[0]
            if big:
                (count,) = struct.unpack_from("<Q", entries, i * size + 4)
                vptr = e + 12
            else:
                (count,) = struct.unpack_from("<I", entries, i * size + 4)
                vptr = e + 8
            return e, typ, count, vptr, big
    return None


def _seek_subifd_offsets(f, ifd0: int) -> list[int]:
    """All SubIFD offsets linked from IFD0 tag 330 (seek-based)."""
    found = _seek_ifd_entry(f, ifd0, 330)
    if found is None:  # pragma: no cover
        raise ValueError("SubIFDs tag (330) not found")
    _, typ, count, vptr, big = found
    elem = _TYPE_SIZE.get(typ, 4)
    if big and typ in (13, 18):
        elem = 8
    total = count * elem
    field = 8 if big else 4
    fmt = "<Q" if big else "<I"
    if total <= field:
        f.seek(vptr)
        (off,) = struct.unpack(fmt, f.read(field if big else 4)[:8 if big else 4])
        return [off]
    f.seek(vptr)
    (base,) = struct.unpack(fmt, f.read(8 if big else 4))
    f.seek(base)
    buf = f.read(count * (8 if big else 4))
    return [struct.unpack_from(fmt, buf, i * (8 if big else 4))[0]
            for i in range(count)]


def _seek_ifd0_offset(f) -> int:
    f.seek(0)
    magic = f.read(4)
    if magic[:2] != b"II" or magic[2:4] not in (b"*\x00", b"+\x00"):
        raise ValueError("not a little-endian TIFF")
    if magic == b"II+\x00":
        f.seek(8)
        return struct.unpack("<Q", f.read(8))[0]
    f.seek(4)
    return struct.unpack("<I", f.read(4))[0]


def _append_exif(path: str, meta: dict, thumb_w: int, thumb_h: int) -> None:
    """Append EXIF Sub-IFD at EOF and link it from IFD0.

    tifffile refuses to write IFD-pointer tags (34665) via extratags, so
    IFD0 is written with a same-sized dummy private tag (65000, SHORT,
    count 1) whose 12-byte entry is rewritten in place as
    (34665, LONG, 1, exif_offset). Also patches PhotometricInterpretation
    is handled separately by :func:`_patch_linear_raw`.

    Seek-based: the multi-GB pixel data is never read; one entry is
    rewritten in place and the (KB-sized) EXIF block is appended.
    """
    with open(path, "r+b") as f:
        ifd0 = _seek_ifd0_offset(f)
        found = _seek_ifd_entry(f, ifd0, 65000)
        if found is None:  # pragma: no cover
            raise ValueError("dummy tag 65000 not found in IFD0")
        e, _, _, _, big = found
        f.seek(0, 2)
        exif_offset = f.tell()
        # word-align
        if exif_offset % 2:
            f.write(b"\x00")
            exif_offset = f.tell()
        split_exif = meta.get("split_exif", {})
        extra = ([(tag, SPLIT_EXIF_DTYPES[tag]) for tag in split_exif]
                 if split_exif else None)
        block = _build_exif_block(meta, thumb_w, thumb_h, exif_offset, big,
                                  extra)
        # rewrite the dummy entry in place as ExifTag (34665, LONG, 1).
        # Same-sized entry, no byte shifting required.
        f.seek(e)
        if big:
            f.write(struct.pack("<HHQ", 34665, 4, 1))
            f.write(struct.pack("<Q", exif_offset))
        else:
            f.write(struct.pack("<HHI", 34665, 4, 1))
            f.write(struct.pack("<I", exif_offset))
        f.seek(exif_offset)
        f.write(block)


def set_ifd0_tag(path: str, dummy_code: int, tag: int, dtype_name: str,
                 value: object) -> None:
    """Rewrite a reserved dummy IFD0 entry as a real numeric tag.

    ``value`` is a tuple/list of ints stored inline (must fit the 4-byte
    classic / 8-byte BigTIFF value field). Same-sized entry rewrite, no
    byte shifting. Handles classic TIFF and BigTIFF. Seek-based: only
    the entry is rewritten, the pixel data is never read.
    """
    count, raw = _pack_val(dtype_name, value)
    with open(path, "r+b") as f:
        ifd0 = _seek_ifd0_offset(f)
        found = _seek_ifd_entry(f, ifd0, dummy_code)
        if found is None:  # pragma: no cover
            raise ValueError(f"dummy tag {dummy_code} not found in IFD0")
        e, _, _, _, big = found
        field_len = 8 if big else 4
        if len(raw) > field_len:  # pragma: no cover - defensive
            raise ValueError(f"value too large for inline IFD0 field: {value!r}")
        field = raw + b"\x00" * (field_len - len(raw))
        f.seek(e)
        f.write(struct.pack("<HH" + ("Q" if big else "I"),
                            tag, _DTYPE_NUM[dtype_name], count))
        f.write(field)


def append_ifd0_ascii(path: str, dummy_code: int, tag: int,
                      text: str) -> None:
    """Rewrite a dummy IFD0 entry as an ASCII tag with an EOF blob value.

    Seek-based: the blob is appended at EOF, one entry rewritten in
    place; pixel data is never read.
    """
    raw = text.encode("ascii") + b"\x00"
    with open(path, "r+b") as f:
        ifd0 = _seek_ifd0_offset(f)
        found = _seek_ifd_entry(f, ifd0, dummy_code)
        if found is None:  # pragma: no cover
            raise ValueError(f"dummy tag {dummy_code} not found in IFD0")
        e, _, _, _, big = found
        f.seek(0, 2)
        blob_off = f.tell()
        if blob_off % 2:
            f.write(b"\x00")
            blob_off = f.tell()
        f.write(raw)
        f.seek(e)
        f.write(struct.pack("<HH" + ("Q" if big else "I"),
                            tag, _DTYPE_NUM["ASCII"], len(raw)))
        f.write(struct.pack("<Q" if big else "<I", blob_off))


def _patch_linear_raw(path: str) -> None:
    """Change every SubIFD PhotometricInterpretation RGB(2) -> LinearRaw(34892).

    Handles classic TIFF and BigTIFF (DNG 1.6) layouts, and any number of
    raw frames linked from tag 330. Seek-based: only IFD headers are
    read and 2 bytes per SubIFD are rewritten; pixel data is never read.
    """
    with open(path, "r+b") as f:
        ifd0 = _seek_ifd0_offset(f)
        for subifd in _seek_subifd_offsets(f, ifd0):
            found = _seek_ifd_entry(f, subifd, 262)
            if found is None:  # pragma: no cover
                raise ValueError(
                    "PhotometricInterpretation not found in SubIFD")
            _, _, _, vptr, _ = found
            f.seek(vptr)
            f.write(struct.pack("<H", 34892))




def _raw_series_all(tif):
    """All raw SubIFD series in file order (LinearRaw 34892 / CFA 32803).

    Cannot use size: a single-channel CFA raw is smaller than the RGB
    thumbnail. SubIFDs are identified by photometric interpretation.
    """
    raws = [s for s in tif.series
            if int(s.keyframe.photometric) in (DngContainer.LINEAR_RAW,
                                               DngContainer.CFA)]
    if raws:
        return raws
    if len(tif.series) >= 2:
        return tif.series[1:]  # our files: thumbnail first, raw SubIFD(s) last
    raise ValueError("no SubIFD raw image found - not a stego DNG?")


def _raw_series(tif):
    """First raw SubIFD series (see :func:`_raw_series_all`)."""
    return _raw_series_all(tif)[0]


def _exif_lookup(exif: dict, code: int, name: str):
    """EXIF value by tag name or numeric code (tifffile keys either way)."""
    if name in exif:
        return exif[name]
    if code in exif:
        return exif[code]
    return None
