"""Image creation-time sources for ``--image-time``.

The default metadata story keeps the EXIF capture time random.  These
helpers resolve the three non-random choices: the input file's birth
time, its last-modified time, or the moment the output is generated.

Linux does not expose ``st_birthtime`` through :func:`os.stat` (Python
3.14 still lacks it), so the birth time is read with the ``statx``
syscall via :mod:`ctypes`.  Filesystems that do not record a birth time
fall back to ``st_ctime``, the closest available value; on Windows
``st_ctime`` *is* the creation time.
"""
from __future__ import annotations

import ctypes
import ctypes.util
import datetime as _dt
import os
import sys

# Values accepted by the CLI's --image-time option.  "random" leaves the
# existing per-seed timestamp behaviour untouched.
IMAGE_TIME_CHOICES = ("random", "input-created", "input-modified", "now")

_AT_FDCWD = -100
_STATX_BTIME = 0x00000800


class _StatxTimestamp(ctypes.Structure):
    _fields_ = [
        ("tv_sec", ctypes.c_int64),
        ("tv_nsec", ctypes.c_uint32),
        ("__reserved", ctypes.c_uint32),
    ]


class _Statx(ctypes.Structure):
    _fields_ = [
        ("stx_mask", ctypes.c_uint32),
        ("stx_blksize", ctypes.c_uint32),
        ("stx_attributes", ctypes.c_uint64),
        ("stx_nlink", ctypes.c_uint32),
        ("stx_uid", ctypes.c_uint32),
        ("stx_gid", ctypes.c_uint32),
        ("stx_mode", ctypes.c_uint16),
        ("__spare0", ctypes.c_uint16 * 1),
        ("stx_ino", ctypes.c_uint64),
        ("stx_size", ctypes.c_uint64),
        ("stx_blocks", ctypes.c_uint64),
        ("stx_attributes_mask", ctypes.c_uint64),
        ("stx_atime", _StatxTimestamp),
        ("stx_btime", _StatxTimestamp),
        ("stx_ctime", _StatxTimestamp),
        ("stx_mtime", _StatxTimestamp),
        ("stx_rdev_major", ctypes.c_uint32),
        ("stx_rdev_minor", ctypes.c_uint32),
        ("stx_dev_major", ctypes.c_uint32),
        ("stx_dev_minor", ctypes.c_uint32),
        ("stx_mnt_id", ctypes.c_uint64),
        ("stx_dio_mem_align", ctypes.c_uint32),
        ("stx_dio_offset_align", ctypes.c_uint32),
        ("__spare3", ctypes.c_uint64 * 12),
    ]


_statx = None
_statx_loaded = False


def _linux_birth_timestamp(path: str) -> float | None:
    """Birth time from Linux ``statx``, or None when unavailable."""
    global _statx, _statx_loaded
    if not sys.platform.startswith("linux"):
        return None
    if not _statx_loaded:
        _statx_loaded = True
        try:
            libc = ctypes.CDLL(ctypes.util.find_library("c") or "libc.so.6",
                               use_errno=True)
            _statx = libc.statx
        except (OSError, AttributeError):
            _statx = None
    if _statx is None:
        return None
    stat = _Statx()
    try:
        rc = _statx(_AT_FDCWD, os.fsencode(path), 0, _STATX_BTIME,
                    ctypes.byref(stat))
    except (OSError, TypeError, ValueError):
        return None
    if rc != 0 or not (stat.stx_mask & _STATX_BTIME):
        return None
    return stat.stx_btime.tv_sec + stat.stx_btime.tv_nsec / 1_000_000_000


def file_created_timestamp(path: str) -> float:
    """Best-effort creation time of ``path`` as a POSIX timestamp."""
    st = os.stat(path)
    birth = getattr(st, "st_birthtime", None)
    if birth is not None:
        return float(birth)
    birth = _linux_birth_timestamp(path)
    if birth is not None:
        return birth
    # POSIX st_ctime is inode-change time, not creation, but it is the
    # closest value a filesystem without birth-time support can offer.
    return float(st.st_ctime)


def file_modified_timestamp(path: str) -> float:
    """Last-modified time of ``path`` as a POSIX timestamp."""
    return float(os.stat(path).st_mtime)


def resolve_image_time(source: str, input_path: str) -> _dt.datetime | None:
    """Resolve an ``--image-time`` source to a local wall-clock datetime.

    ``random`` returns None so the existing seeded randomization applies.
    """
    if source == "random":
        return None
    if source == "now":
        return _dt.datetime.now()
    if source == "input-created":
        stamp = file_created_timestamp(input_path)
    elif source == "input-modified":
        stamp = file_modified_timestamp(input_path)
    else:
        raise ValueError(
            f"unknown image-time source {source!r}; choose one of "
            f"{', '.join(IMAGE_TIME_CHOICES)}")
    return _dt.datetime.fromtimestamp(stamp)


def normalize_image_time(value: _dt.datetime) -> tuple[_dt.datetime, str]:
    """Return naive local wall time and its EXIF ``±HH:MM`` offset.

    Aware datetimes are converted to the system's local timezone; naive
    ones are taken as local wall time.  EXIF's DateTimeOriginal has no
    timezone, so OffsetTime must describe the same local moment.
    """
    if not isinstance(value, _dt.datetime):
        raise TypeError("image_time must be a datetime.datetime or None")
    aware = value.astimezone()
    offset = aware.strftime("%z") or "+0000"
    offset = offset[:3] + ":" + offset[3:]
    return aware.replace(tzinfo=None), offset


def utc_image_time(value: _dt.datetime) -> _dt.datetime:
    """Naive UTC wall time for the GPS IFD (GPSDateStamp/GPSTimeStamp)."""
    if not isinstance(value, _dt.datetime):
        raise TypeError("image_time must be a datetime.datetime or None")
    return value.astimezone(_dt.timezone.utc).replace(tzinfo=None)
