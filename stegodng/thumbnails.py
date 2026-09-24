"""Thumbnail pictures for the DNG preview (IFD0).

Desktop environments never render the 16-bit raw for an icon: Windows
Explorer goes through WIC RAW codecs and Nautilus through external
``.thumbnailer`` helpers (e.g. ``gnome-raw-thumbnailer``); both consume
the embedded IFD0 JPEG preview. This module supplies the *picture* that
goes into that JPEG.

Sources (``ThumbnailProvider.get``):

* ``"random"`` (default) — a random photo from Wikimedia Commons via
  ``Special:Random/Image`` (redirect resolved to the ``File:`` page,
  pixels fetched through ``Special:FilePath`` which renders a
  server-side downscale). Any failure (network, unexpected redirect,
  unsupported type, undecodable bytes) falls back to generated noise
  after a few attempts.
* ``"synthetic"`` — the built-in gradient cover (offline-safe).
* a filesystem path — the user's own image (errors are raised, not
  silently swapped for noise).

The picture is center-cropped to the thumbnail frame aspect and resized
with Lanczos to the recommended size (combiner parity: up to 4000x3000,
same frame the writer uses).
"""
from __future__ import annotations

import os
import urllib.parse
import urllib.request
from io import BytesIO

import numpy as np
from PIL import Image

from .cover import CoverGenerator

USER_AGENT = "ImageSteg-DNG/1.0 (random-thumbnail fetcher; contact: admin@example.invalid)"

# Photo-like types Pillow reliably decodes; everything else (SVG, TIFF,
# video, audio, archives, ...) triggers another random pick / fallback.
ALLOWED_EXTENSIONS = frozenset(
    {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"})


class ThumbnailError(Exception):
    """Fetching or decoding a thumbnail picture failed."""


def _default_opener(url: str, timeout: float) -> tuple[str, bytes]:
    """GET ``url`` (following redirects) -> (final URL, body bytes)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.geturl(), resp.read()


class ThumbnailProvider:
    """Fetch/prepare thumbnail pictures. ``opener`` is injectable for tests."""

    RANDOM_URL = "https://commons.wikimedia.org/wiki/Special:Random/Image"
    FILEPATH_URL = "https://commons.wikimedia.org/wiki/Special:FilePath/{}"

    def __init__(self, seed: int | None = None, timeout: float = 10.0,
                 max_attempts: int = 3, opener=None) -> None:
        self._seed = 0 if seed is None else seed
        self.timeout = timeout
        self.max_attempts = max_attempts
        self._opener = opener or _default_opener

    # -- public ---------------------------------------------------------
    def get(self, tw: int, th: int, source: str = "random"
            ) -> tuple[np.ndarray, str]:
        """Return (RGB uint8 array sized (th, tw, 3), source label)."""
        if source == "synthetic":
            return (CoverGenerator(self._seed).thumbnail(th, tw),
                    "synthetic-gradient")
        if source != "random" and not os.path.isfile(source):
            raise ThumbnailError(
                f"unknown thumbnail source {source!r}: expected 'random', "
                f"'synthetic', or a path to an image file")
        if os.path.isfile(source):
            with open(source, "rb") as f:
                data = f.read()
            return prepare(data, tw, th), f"file:{source}"
        last: Exception | None = None
        for _ in range(max(1, self.max_attempts)):
            try:
                data, name = self._fetch_random_bytes(tw)
                return prepare(data, tw, th), f"commons:{name}"
            except Exception as exc:  # noqa: BLE001 - any failure -> retry/fallback
                last = exc
        return self.noise(tw, th), "synthetic-noise-fallback"

    def noise(self, tw: int, th: int) -> np.ndarray:
        """Small random RGB noise image (offline fallback)."""
        rng = np.random.default_rng(self._seed + 31337)
        return np.ascontiguousarray(
            rng.integers(0, 256, size=(th, tw, 3)).astype(np.uint8))

    # -- fetching ---------------------------------------------------------
    def _fetch_random_bytes(self, tw: int) -> tuple[bytes, str]:
        """One random Commons pick -> (image bytes, filename)."""
        page_url, _ = self._opener(self.RANDOM_URL, self.timeout)
        path = urllib.parse.urlparse(page_url).path
        marker = "/wiki/File:"
        if marker not in path:
            raise ThumbnailError(
                f"unexpected redirect target {page_url!r}")
        filename = urllib.parse.unquote(path.split(marker, 1)[1])
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise ThumbnailError(
                f"unsupported media type {ext or '(none)'} for {filename!r}")
        width = min(max(tw, 64), 4096)
        dl_url = (self.FILEPATH_URL.format(urllib.parse.quote(filename))
                  + f"?width={width}")
        _, data = self._opener(dl_url, self.timeout)
        if len(data) < 1024:
            raise ThumbnailError(f"empty download for {filename!r}")
        return data, filename


#: Module-level aliases (kept in sync with the class attributes above).
RANDOM_URL = ThumbnailProvider.RANDOM_URL
FILEPATH_URL = ThumbnailProvider.FILEPATH_URL


def prepare(data: bytes, tw: int, th: int) -> np.ndarray:
    """Decode image bytes, center-crop to the tw:th frame aspect and
    Lanczos-resize to exactly (th, tw). Raises :class:`ThumbnailError`."""
    try:
        with Image.open(BytesIO(data)) as im:
            im.load()
            if im.mode in ("RGBA", "LA", "PA"):
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.split()[-1])
                im = bg
            else:
                im = im.convert("RGB")
            sw, sh = im.size
            if sw <= 0 or sh <= 0:
                raise ValueError("empty image")
            target = tw / th
            if sw / sh > target:
                # too wide: trim sides
                nw = round(sh * target)
                x0 = (sw - nw) // 2
                im = im.crop((x0, 0, x0 + nw, sh))
            else:
                # too tall: trim top/bottom
                nh = round(sw / target)
                y0 = (sh - nh) // 2
                im = im.crop((0, y0, sw, y0 + nh))
            im = im.resize((tw, th), Image.LANCZOS)
            arr = np.asarray(im, dtype=np.uint8)
    except ThumbnailError:
        raise
    except Exception as exc:
        raise ThumbnailError(f"cannot decode/resize thumbnail: {exc}") from exc
    if arr.shape != (th, tw, 3):
        raise ThumbnailError(f"unexpected prepared shape {arr.shape}")
    return np.ascontiguousarray(arr)
