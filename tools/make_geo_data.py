#!/usr/bin/env python3
"""Regenerate ``stegodng/geo/zones.bin`` (plausible capture locations).

The runtime sampler needs three things per principal tz location:

* name, latitude, longitude  -- from ``zone1970.tab`` in the IANA tz
  database (public domain), so no dependency and no drift between
  installs;
* a land mask for the 25 km disk around it -- built once here from the
  1 km GLOBE mask (``pip install global-land-mask``), because testing
  the water at encode time would need a ~1 GB raster;
* an elevation -- queried once from the Open-Meteo elevation API
  (Copernicus DEM GLO-90) and cached in a JSON file so reruns are free.

Only the resulting ~35 KB blob ships; this script is a release tool, not
an import-time dependency.  Zones whose 25 km disk has no land at all
(narrow atolls the 1 km mask cannot resolve, e.g. Male) are dropped:
their tz coordinate can be a kilometre offshore, so a fallback point
would still be water.

Usage:
    python3 tools/make_geo_data.py                 # system zone1970.tab
    python3 tools/make_geo_data.py --tab /path/to/zone1970.tab \
        --out stegodng/geo/zones.bin

Requires numpy (runtime dependency) and global-land-mask (build only).
"""
from __future__ import annotations

import argparse
import json
import math
import re
import struct
import sys
import time
import urllib.parse
import urllib.request
import zlib
from pathlib import Path

SPAN_KM = 25.0          # grid covers [-SPAN_KM, +SPAN_KM] on both axes
CELL_KM = 0.5
GRID = int(round(2 * SPAN_KM / CELL_KM))   # 100 cells per side
MASK_BYTES = (GRID * GRID + 7) // 8
MAGIC = b"STGEO1"
KM_PER_DEG = 111.32
ELEVATION_BATCH = 100
ELEVATION_URL = "https://api.open-meteo.com/v1/elevation"

_ISO6709 = re.compile(
    r"([+-])(\d{2})(\d{2})(\d{2})?([+-])(\d{3})(\d{2})(\d{2})?")


class Zone:
    __slots__ = ("name", "lat", "lon", "elevation", "mask")

    def __init__(self, name: str, lat: float, lon: float) -> None:
        self.name = name
        self.lat = lat
        self.lon = lon
        self.elevation: int | None = None
        self.mask: bytes | None = None

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return f"Zone({self.name!r}, {self.lat:.4f}, {self.lon:.4f})"


def _coord(text: str) -> tuple[float, float]:
    match = _ISO6709.fullmatch(text)
    if match is None:
        raise ValueError(f"unsupported ISO 6709 coordinate {text!r}")
    s, dd, mm, ss, s2, ddd, m2, s2s = match.groups()
    lat = (int(dd) + int(mm) / 60 + (int(ss) / 3600 if ss else 0.0))
    lon = (int(ddd) + int(m2) / 60 + (int(s2s) / 3600 if s2s else 0.0))
    return (-lat if s == "-" else lat), (-lon if s2 == "-" else lon)


def parse_zone_tab(path: Path) -> list[Zone]:
    """Read ``zone1970.tab`` rows that carry a principal location."""
    zones: list[Zone] = []
    seen: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t")
        if len(fields) < 3:
            continue
        lat, lon = _coord(fields[1])
        name = fields[2]
        if name in seen:
            continue
        seen.add(name)
        zones.append(Zone(name, lat, lon))
    return zones


def build_mask(zone: Zone) -> bytes:
    """Pack a GRID x GRID land bitmap for the zone's 25 km disk."""
    import numpy as np
    from global_land_mask import globe

    offsets = -SPAN_KM + (np.arange(GRID) + 0.5) * CELL_KM
    xs, ys = np.meshgrid(offsets, offsets)          # rows = y, cols = x
    coslat = max(0.05, math.cos(math.radians(zone.lat)))
    lats = zone.lat + ys / KM_PER_DEG
    lons = (zone.lon + xs / (KM_PER_DEG * coslat) + 180.0) % 360.0 - 180.0
    land = np.asarray(globe.is_land(lats, lons), dtype=bool)
    # Row-major (y outer, x inner), little-endian bit order so the
    # runtime test is simply (mask[k >> 3] >> (k & 7)) & 1.
    return np.packbits(land.reshape(-1), bitorder="little").tobytes()


def _cache_load(path: Path) -> dict[str, int]:
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {str(k): int(v) for k, v in data.items() if isinstance(v, (int, float))}


def fetch_elevations(zones: list[Zone], cache_path: Path,
                     refresh: bool = False) -> None:
    cache = {} if refresh else _cache_load(cache_path)
    missing = [z for z in zones if z.name not in cache]
    for start in range(0, len(missing), ELEVATION_BATCH):
        batch = missing[start:start + ELEVATION_BATCH]
        query = urllib.parse.urlencode({
            "latitude": ",".join(f"{z.lat:.5f}" for z in batch),
            "longitude": ",".join(f"{z.lon:.5f}" for z in batch),
        })
        url = f"{ELEVATION_URL}?{query}"
        values = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=30) as response:
                    payload = json.loads(response.read().decode())
                values = payload.get("elevation")
                if isinstance(values, list) and len(values) == len(batch):
                    break
                values = None
            except (OSError, ValueError) as exc:
                print(f"elevation request failed ({exc}); retrying",
                      file=sys.stderr)
            time.sleep(2 ** attempt)
        if values is None:
            raise SystemExit(
                f"could not fetch elevations for {len(batch)} zones; "
                f"the cache at {cache_path} was left untouched")
        for zone, value in zip(batch, values):
            cache[zone.name] = int(round(float(value)))
        cache_path.write_text(json.dumps(cache, indent=1, sort_keys=True))
        print(f"elevations: {len(cache)}/{len(zones)} cached")
        if start + ELEVATION_BATCH < len(missing):
            time.sleep(1.0)
    for zone in zones:
        zone.elevation = cache[zone.name]


def serialize(zones: list[Zone]) -> bytes:
    parts = [MAGIC, struct.pack("<H", len(zones))]
    for zone in zones:
        assert zone.mask is not None and zone.elevation is not None
        name = zone.name.encode("utf-8")
        if len(name) > 255:
            raise SystemExit(f"zone name too long: {zone.name}")
        parts.append(struct.pack("<B", len(name)))
        parts.append(name)
        parts.append(struct.pack(
            "<iiHh",
            int(round(zone.lat * 1_000_000)),
            int(round(zone.lon * 1_000_000)),
            len(zone.mask),
            zone.elevation,
        ))
        parts.append(zone.mask)
    return zlib.compress(b"".join(parts), 9)


def main(argv: list[str] | None = None) -> int:
    default_tab = Path("/usr/share/zoneinfo/zone1970.tab")
    default_out = Path(__file__).resolve().parent.parent / "stegodng" / "geo" / "zones.bin"
    default_cache = Path("/tmp/opencode/geo_elevation_cache.json")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tab", type=Path, default=default_tab)
    parser.add_argument("--out", type=Path, default=default_out)
    parser.add_argument("--cache", type=Path, default=default_cache)
    parser.add_argument("--refresh-elevation", action="store_true")
    args = parser.parse_args(argv)

    if not args.tab.is_file():
        raise SystemExit(f"zone table not found: {args.tab}")
    zones = parse_zone_tab(args.tab)
    print(f"{len(zones)} principal locations in {args.tab}")

    fetch_elevations(zones, args.cache, refresh=args.refresh_elevation)

    kept: list[Zone] = []
    for zone in zones:
        zone.mask = build_mask(zone)
        if any(zone.mask):
            kept.append(zone)
    dropped = [z.name for z in zones if not any(z.mask or b"")]
    print(f"kept {len(kept)} zones with land in the 25 km disk")
    if dropped:
        print("dropped (1 km mask sees only water): " + ", ".join(dropped))

    blob = serialize(kept)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(blob)
    print(f"wrote {args.out} ({len(blob):,} bytes, "
          f"{MASK_BYTES} mask bytes/zone)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
