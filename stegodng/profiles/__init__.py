"""Camera profile registry: one directory per camera under this package.

Each ``<slug>/`` directory holds ``profile.json`` (machine-readable data
harvested from ``dpreview-raw`` samples) plus ``README.md`` (camera name,
sample metadata, static-vs-randomized fields, subprofile definitions).
:func:`get_profile` builds :class:`CameraProfile` instances on demand and
caches them; the built-in ``gfx_100`` reference profile is always
available even when no data directories are present.
"""
from __future__ import annotations

import json
from pathlib import Path

from stegodng.profile import DEFAULT_PROFILE, CameraProfile

_DATA_DIR = Path(__file__).resolve().parent

_CACHE: dict[str, CameraProfile] | None = None


def _load_all() -> dict[str, CameraProfile]:
    global _CACHE
    if _CACHE is not None:
        return _CACHE
    profiles: dict[str, CameraProfile] = {"gfx_100": DEFAULT_PROFILE}
    if _DATA_DIR.is_dir():
        for child in sorted(_DATA_DIR.iterdir()):
            data_file = child / "profile.json"
            if child.is_dir() and data_file.is_file():
                try:
                    data = json.loads(data_file.read_text())
                except (OSError, ValueError):
                    continue  # corrupt entry: skip, never fail the import
                if not isinstance(data, dict):
                    continue
                slug = data.get("slug", child.name)
                if slug == "gfx_100":
                    continue  # built-in reference stays byte-stable
                try:
                    profiles[slug] = CameraProfile.from_dict(data)
                except Exception:
                    continue  # one bad file must not break all profiles
    _CACHE = profiles
    return profiles


def list_profiles() -> list[str]:
    """Sorted slugs of every available ``--camera-profile`` (base names)."""
    return sorted(_load_all())


def get_profile(slug: str) -> CameraProfile:
    """Return the profile for ``slug`` (raises ValueError when unknown)."""
    profiles = _load_all()
    if slug not in profiles:
        raise ValueError(
            f"unknown camera profile {slug!r}: choose from "
            f"{', '.join(list_profiles())}")
    return profiles[slug]


def resolve(spec: str) -> tuple[CameraProfile, str | None]:
    """Split ``slug[-subprofile]`` into (profile, subprofile-or-None).

    The longest registered slug wins, so ``gfx_100-pixelshift`` resolves
    to profile ``gfx_100`` + subprofile ``pixelshift``. Raises ValueError
    for unknown slugs or unknown subprofiles.
    """
    profiles = _load_all()
    if spec in profiles:
        return profiles[spec], None
    if "-" in spec:
        parts = spec.split("-")
        for i in range(len(parts) - 1, 0, -1):
            slug, sub = "-".join(parts[:i]), "-".join(parts[i:])
            if slug in profiles:
                profile = profiles[slug]
                if sub in profile.subprofiles:
                    return profile, sub
                raise ValueError(
                    f"unknown sub-profile {sub!r} for camera {slug!r}: "
                    f"choose from {sorted(profile.subprofiles)}")
    raise ValueError(
        f"unknown camera profile {spec!r}: choose from "
        f"{', '.join(list_profiles())}")


def reload() -> None:  # pragma: no cover - test helper
    """Drop the registry cache (picks up newly generated profiles)."""
    global _CACHE
    _CACHE = None
