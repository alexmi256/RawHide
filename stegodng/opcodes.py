"""DNG ``OpcodeList2`` support, starting with the GainMap opcode.

Adobe-converted Pixel XL DNGs carry an ``OpcodeList2`` (tag 51009) with
four GainMap opcodes (ID 9), one per CFA phase.  The opcode list is a
big-endian sequence::

    uint32 count
    repeat count:
        uint32 opcode_id
        uint32 version
        uint32 flags
        uint32 parameter_size
        byte[parameter_size] parameters

Each GainMap parameter block is the DNG 1.3 layout::

    LONG   Top, Left, Bottom, Right
    LONG   Plane, Planes, RowPitch, ColPitch
    LONG   MapPointsV, MapPointsH
    DOUBLE MapSpacingV, MapSpacingH, MapOriginV, MapOriginH
    LONG   MapPlanes
    FLOAT  MapPointsV x MapPointsH x MapPlanes gains

The writer and parser stay independent of the camera profile: callers
pass a :class:`GainMapConfig` whose small base grid is interpolated to
the on-disk 30x40 map and perturbed per file.  The base grid in the
Pixel XL profile was averaged from six real files; per-file jitter keeps
two generated files from sharing an identical gain map.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import Any

import numpy as np

GAIN_MAP_OPCODE = 9
GAIN_MAP_VERSION = 0x01030000
GAIN_MAP_POINTS = (30, 40)
# CFA phase order used by the Pixel XL samples: B, G, G, R (BGGR).
GAIN_MAP_PHASES = ((1, 1), (1, 0), (0, 1), (0, 0))

_U32 = ">I"
_OPCODE_HEADER = ">IIII"
_GAIN_HEADER = ">10I4dI"
_GAIN_HEADER_SIZE = struct.calcsize(_GAIN_HEADER)


def _bilinear(grid: np.ndarray, shape: tuple[int, int]) -> np.ndarray:
    """Bilinearly resize a 2-D float grid to ``shape`` (edge-clamped)."""
    src_v, src_h = grid.shape
    dst_v, dst_h = shape
    if src_v < 2 or src_h < 2:
        raise ValueError("base grid needs at least 2x2 points")
    ys = np.linspace(0, src_v - 1, dst_v)
    xs = np.linspace(0, src_h - 1, dst_h)
    y0 = np.floor(ys).astype(np.intp)
    x0 = np.floor(xs).astype(np.intp)
    y1 = np.minimum(y0 + 1, src_v - 1)
    x1 = np.minimum(x0 + 1, src_h - 1)
    wy = (ys - y0)[:, None]
    wx = (xs - x0)[None, :]
    top = grid[y0][:, x0] * (1 - wx) + grid[y0][:, x1] * wx
    bottom = grid[y1][:, x0] * (1 - wx) + grid[y1][:, x1] * wx
    return top * (1 - wy) + bottom * wy


@dataclass(frozen=True, eq=False)
class GainMapConfig:
    """Per-profile GainMap base plus per-file variation settings.

    ``planes`` is a ``(4, V, H)`` grid ordered by :data:`GAIN_MAP_PHASES`.
    It is deliberately small (the Pixel XL profile uses 8x10) so it can
    live in ``profile.json``; :func:`generate_gainmaps` interpolates it to
    the 30x40 opcode grid.
    """

    planes: np.ndarray
    jitter: float = 0.025
    clip: tuple[float, float] = (1.0, 4.2)

    def __post_init__(self) -> None:
        planes = np.asarray(self.planes, dtype=np.float64)
        if planes.ndim != 3 or planes.shape[0] != 4:
            raise ValueError(
                "gainmap planes must be a 4 x V x H array (one per CFA phase)")
        if planes.shape[1] < 2 or planes.shape[2] < 2:
            raise ValueError("gainmap base grid needs at least 2x2 points")
        if not np.isfinite(planes).all() or (planes <= 0).any():
            raise ValueError("gainmap base values must be finite and positive")
        if not np.isfinite(self.jitter) or self.jitter < 0:
            raise ValueError("gainmap jitter must be a non-negative number")
        lo, hi = self.clip
        if not (np.isfinite(lo) and np.isfinite(hi) and 0 < lo < hi):
            raise ValueError("gainmap clip must be two increasing positives")
        object.__setattr__(self, "planes", planes)
        object.__setattr__(self, "clip", (float(lo), float(hi)))

    @property
    def grid(self) -> tuple[int, int]:
        return (int(self.planes.shape[1]), int(self.planes.shape[2]))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GainMapConfig":
        if not isinstance(data, dict):
            raise ValueError("gainmap must be a dict")
        grid = data.get("grid")
        planes = data.get("planes")
        if planes is None:
            raise ValueError("gainmap needs a planes grid")
        if grid is not None:
            if (not isinstance(grid, (list, tuple)) or len(grid) != 2
                    or any(int(n) < 2 for n in grid)):
                raise ValueError("gainmap grid must be [rows, cols] >= 2")
            expected = (int(grid[0]), int(grid[1]))
        else:
            arr = np.asarray(planes, dtype=np.float64)
            if arr.ndim != 3:
                raise ValueError("gainmap planes must be 4 x V x H")
            expected = (int(arr.shape[1]), int(arr.shape[2]))
        arr = np.asarray(planes, dtype=np.float64)
        if arr.shape != (4, *expected):
            raise ValueError(
                f"gainmap planes shape {arr.shape} does not match grid "
                f"{expected}")
        clip = data.get("clip", (1.0, 4.2))
        if not isinstance(clip, (list, tuple)) or len(clip) != 2:
            raise ValueError("gainmap clip must be [low, high]")
        return cls(
            planes=arr,
            jitter=float(data.get("jitter", 0.025)),
            clip=(float(clip[0]), float(clip[1])),
        )

    def to_dict(self, digits: int = 6) -> dict[str, Any]:
        return {
            "grid": list(self.grid),
            "jitter": self.jitter,
            "clip": list(self.clip),
            "planes": np.round(self.planes, digits).tolist(),
        }

    @classmethod
    def synthetic(cls, points: tuple[int, int] = (8, 10),
                  corner: float = 3.8) -> "GainMapConfig":
        """Radial fallback, for tests or profiles without a harvested base."""
        v, h = points
        yy, xx = np.mgrid[0:v, 0:h]
        x = xx / max(h - 1, 1) - 0.5
        y = yy / max(v - 1, 1) - 0.5
        r2 = (x * x + y * y) / 0.5
        gains = []
        for p in range(4):
            # Slightly different colour shading per CFA phase.
            k = 1.0 + (corner - 1.0) * (r2 ** 1.15) * (1.0 + 0.02 * p)
            gains.append(k)
        return cls(planes=np.stack(gains))


def generate_gainmaps(width: int, height: int, seed: int | None,
                      config: GainMapConfig) -> np.ndarray:
    """Return four ``(30, 40)`` gain maps for one file.

    The base grid is interpolated to the opcode grid, then a low-frequency
    Gaussian field is added with the configured jitter (normalised to a
    unit standard deviation after interpolation).  Output is deterministic
    for a given seed.
    """
    if width < 2 or height < 2:
        raise ValueError("GainMap bounds need width and height >= 2")
    rng = np.random.default_rng(0 if seed is None else seed)
    points = GAIN_MAP_POINTS
    out = np.empty((4, *points), dtype=np.float64)
    for plane in range(4):
        base = _bilinear(config.planes[plane], points)
        noise = _bilinear(rng.normal(size=config.grid), points)
        std = float(noise.std())
        if std > 0:
            noise /= std
        gains = base + config.jitter * noise
        out[plane] = np.clip(gains, *config.clip)
    return out


def _build_gainmap_params(width: int, height: int, top: int, left: int,
                          gains: np.ndarray) -> bytes:
    arr = np.asarray(gains, dtype=np.float64)
    if arr.ndim == 2:
        arr = arr[:, :, None]
    if arr.ndim != 3 or arr.shape[:2] != GAIN_MAP_POINTS:
        raise ValueError(
            f"gains must be {GAIN_MAP_POINTS[0]}x{GAIN_MAP_POINTS[1]}"
            " (optionally with map planes)")
    points_v, points_h, map_planes = arr.shape
    if arr.size and not np.isfinite(arr).all():
        raise ValueError("gains must be finite")
    if (arr <= 0).any():
        raise ValueError("gains must be positive")
    spacing_v = 1.0 / max(points_v - 1, 1)
    spacing_h = 1.0 / max(points_h - 1, 1)
    header = struct.pack(
        _GAIN_HEADER,
        int(top), int(left), int(height), int(width),
        0, 1, 2, 2,
        points_v, points_h,
        spacing_v, spacing_h, 0.0, 0.0,
        map_planes,
    )
    # DNG stores gain tables as big-endian 32-bit floats, row-major
    # (V, H, MapPlanes).
    return header + arr.astype(">f4").tobytes(order="C")


def build_opcode_list2(width: int, height: int, seed: int | None = 0,
                       config: GainMapConfig | None = None,
                       gains: np.ndarray | None = None) -> bytes:
    """Build an ``OpcodeList2`` with four GainMap opcodes.

    ``gains`` may be a precomputed ``(4, 30, 40)`` array; otherwise the
    maps are generated from ``config`` (a synthetic radial base is used
    when ``config`` is omitted).
    """
    if config is None and gains is None:
        config = GainMapConfig.synthetic()
    if gains is None:
        assert config is not None
        gains = generate_gainmaps(width, height, seed, config)
    arr = np.asarray(gains, dtype=np.float64)
    if arr.shape[0] != 4:
        raise ValueError("need four gain maps, one per CFA phase")
    parts = [struct.pack(_U32, 4)]
    for plane, (top, left) in enumerate(GAIN_MAP_PHASES):
        params = _build_gainmap_params(
            width, height, top, left, arr[plane])
        parts.append(struct.pack(
            _OPCODE_HEADER, GAIN_MAP_OPCODE, GAIN_MAP_VERSION, 0, len(params)))
        parts.append(params)
    return b"".join(parts)


@dataclass(frozen=True, eq=False)
class GainMap:
    """One parsed GainMap opcode."""

    top: int
    left: int
    bottom: int
    right: int
    plane: int
    planes: int
    row_pitch: int
    col_pitch: int
    points_v: int
    points_h: int
    spacing_v: float
    spacing_h: float
    origin_v: float
    origin_h: float
    map_planes: int
    gains: np.ndarray  # (points_v, points_h, map_planes)


def parse_opcode_list2(blob: bytes) -> list[GainMap]:
    """Parse an ``OpcodeList2`` and return its GainMap opcodes.

    Raises ``ValueError`` for truncated data, unsupported opcodes, or a
    trailing byte count that does not match the declared opcodes.
    """
    if len(blob) < 4:
        raise ValueError("opcode list is shorter than its count field")
    count = struct.unpack_from(_U32, blob, 0)[0]
    if count > 64:
        raise ValueError(f"implausible opcode count {count}")
    offset = 4
    out: list[GainMap] = []
    for index in range(count):
        if offset + 16 > len(blob):
            raise ValueError(f"opcode {index}: truncated header")
        opcode, version, flags, size = struct.unpack_from(
            _OPCODE_HEADER, blob, offset)
        offset += 16
        if offset + size > len(blob):
            raise ValueError(f"opcode {index}: truncated parameters")
        params = blob[offset:offset + size]
        offset += size
        if opcode != GAIN_MAP_OPCODE:
            raise ValueError(
                f"opcode {index}: unsupported id {opcode} (only GainMap "
                f"{GAIN_MAP_OPCODE} is handled)")
        if version != GAIN_MAP_VERSION:
            raise ValueError(
                f"opcode {index}: unexpected GainMap version 0x{version:08x}")
        if size < _GAIN_HEADER_SIZE:
            raise ValueError(f"opcode {index}: GainMap params too short")
        (top, left, bottom, right, plane, planes, row_pitch, col_pitch,
         points_v, points_h, spacing_v, spacing_h, origin_v, origin_h,
         map_planes) = struct.unpack_from(_GAIN_HEADER, params, 0)
        expected = points_v * points_h * map_planes * 4
        if size != _GAIN_HEADER_SIZE + expected:
            raise ValueError(
                f"opcode {index}: {size} parameter bytes, expected "
                f"{_GAIN_HEADER_SIZE + expected}")
        gains = np.frombuffer(
            params, dtype=">f4", count=points_v * points_h * map_planes,
            offset=_GAIN_HEADER_SIZE,
        ).astype(np.float64).reshape(points_v, points_h, map_planes)
        out.append(GainMap(
            top=top, left=left, bottom=bottom, right=right,
            plane=plane, planes=planes,
            row_pitch=row_pitch, col_pitch=col_pitch,
            points_v=points_v, points_h=points_h,
            spacing_v=spacing_v, spacing_h=spacing_h,
            origin_v=origin_v, origin_h=origin_h,
            map_planes=map_planes, gains=gains,
        ))
    if offset != len(blob):
        raise ValueError(
            f"{len(blob) - offset} trailing bytes after {count} opcodes")
    return out


def validate_opcode_list2(blob: bytes, *, expect: int = 4,
                          width: int | None = None,
                          height: int | None = None) -> list[GainMap]:
    """Validate the Pixel XL-style four-GainMap layout and return it."""
    maps = parse_opcode_list2(blob)
    if len(maps) != expect:
        raise ValueError(f"expected {expect} GainMap opcodes, got {len(maps)}")
    phases = [(m.top, m.left) for m in maps]
    if phases != list(GAIN_MAP_PHASES):
        raise ValueError(f"CFA phases {phases} != {list(GAIN_MAP_PHASES)}")
    for i, m in enumerate(maps):
        if m.plane != 0 or m.planes != 1:
            raise ValueError(f"opcode {i}: expected plane 0, planes 1")
        if (m.row_pitch, m.col_pitch) != (2, 2):
            raise ValueError(f"opcode {i}: expected 2x2 pitch")
        if m.map_planes != 1:
            raise ValueError(f"opcode {i}: expected one map plane")
        if m.bottom <= m.top or m.right <= m.left:
            raise ValueError(f"opcode {i}: empty gain map bounds")
        if (width is not None and m.right != width) or (
                height is not None and m.bottom != height):
            raise ValueError(
                f"opcode {i}: bounds {m.right}x{m.bottom} != "
                f"{width}x{height}")
        if not np.isfinite(m.gains).all() or (m.gains <= 0).any():
            raise ValueError(f"opcode {i}: gains must be finite and positive")
        if (m.gains < 1.0).any() or (m.gains > 4.2).any():
            raise ValueError(
                f"opcode {i}: gains {m.gains.min():.4f}..{m.gains.max():.4f}"
                " outside the observed Pixel XL range 1.0..4.2")
    return maps


def read_opcode_list2(path: str) -> bytes | None:
    """Return tag 51009 from the first raw SubIFD of ``path``, if present."""
    import tifffile

    with tifffile.TiffFile(path) as tif:
        # SubIFDs are exposed as separate pages inside a series; IFD0
        # itself is the preview page and has no OpcodeList2.
        for series in tif.series:
            for page in series.pages:
                tag = page.tags.get(51009)
                if tag is not None:
                    return bytes(tag.value)
    return None
