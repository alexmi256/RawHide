"""Opaque MakerNote blocks (the Google/Pixel ``HDRP`` blob and siblings).

The Pixel XL reference DNGs carry a ``Exif.Photo.MakerNote`` of 2640-2757
bytes that begins with ``HDRP``, a two-byte version (``02 ef``) and nine
further bytes that are identical in every sample, followed by
high-entropy data (7.9 bits/byte, all 256 byte values present, no
repeating structure and no ASCII strings).  It is Google's HDR+
processing metadata; no public parser decodes it, and in the samples the
payload differs between files even at equal offsets, so it cannot be
derived from a profile or copied between files.

The generator therefore reproduces the observable envelope only: the
constant prefix plus seeded pseudo-random bytes at a realistic length.
That keeps the tag present at a plausible size instead of absent (which
is what a non-Google DNG looks like), but a byte-level comparison with a
real HDR+ blob would show it is not a real payload.  Profiles opt in
through ``fidelity.makernote``; see the Pixel XL profile README.
"""
from __future__ import annotations

import random
from dataclasses import dataclass


def _bytes_from(value, name: str) -> bytes:
    """Hex string or bytes -> bytes (used for the constant prefix)."""
    if isinstance(value, (bytes, bytearray)):
        return bytes(value)
    if isinstance(value, str):
        try:
            return bytes.fromhex(value.replace(" ", ""))
        except ValueError as exc:
            raise ValueError(f"{name} must be hex bytes: {exc}") from exc
    raise ValueError(f"{name} must be bytes or a hex string")


def _text_bytes(value, name: str) -> bytes:
    """Plain text or bytes -> bytes (used for the magic)."""
    if isinstance(value, (bytes, bytearray)):
        return bytes(value)
    if isinstance(value, str):
        try:
            return value.encode("ascii")
        except UnicodeEncodeError as exc:
            raise ValueError(f"{name} must be ASCII: {exc}") from exc
    raise ValueError(f"{name} must be bytes or text")


@dataclass(frozen=True)
class MakernoteConfig:
    """Envelope of one camera's opaque MakerNote.

    ``prefix`` holds the constant bytes that follow ``magic``; together
    they must fit inside the shortest allowed block.  ``length`` is the
    inclusive total-size range observed in the reference files.
    """

    magic: bytes = b"HDRP"
    prefix: bytes = b""
    length: tuple[int, int] = (2640, 2757)

    def __post_init__(self) -> None:
        magic = _text_bytes(self.magic, "makernote.magic")
        prefix = _bytes_from(self.prefix, "makernote.prefix")
        if not magic:
            raise ValueError("makernote.magic must not be empty")
        try:
            low, high = (int(self.length[0]), int(self.length[1]))
        except (TypeError, IndexError, ValueError) as exc:
            raise ValueError("makernote.length must be two integers") from exc
        if low > high or low < 1:
            raise ValueError("makernote.length must be low <= high, low >= 1")
        if len(magic) + len(prefix) > low:
            raise ValueError(
                "makernote prefix is longer than the shortest allowed block")
        object.__setattr__(self, "magic", magic)
        object.__setattr__(self, "prefix", prefix)
        object.__setattr__(self, "length", (low, high))

    @classmethod
    def from_dict(cls, data: dict) -> "MakernoteConfig":
        if not isinstance(data, dict):
            raise ValueError("fidelity.makernote must be a dict")
        length = data.get("length", (2640, 2757))
        if not isinstance(length, (list, tuple)) or len(length) != 2:
            raise ValueError("makernote.length must be [low, high]")
        return cls(
            magic=_text_bytes(data.get("magic", "HDRP"), "makernote.magic"),
            prefix=_bytes_from(data.get("prefix_hex", ""),
                               "makernote.prefix_hex"),
            length=(int(length[0]), int(length[1])),
        )

    def to_dict(self) -> dict:
        return {
            "magic": self.magic.decode("latin-1"),
            "prefix_hex": self.prefix.hex(),
            "length": list(self.length),
        }

    def generate(self, seed: int | None = None) -> bytes:
        """Deterministic block for one file (same seed -> same bytes)."""
        seed = 0 if seed is None else seed
        size_rng = random.Random(f"makernote-size:{seed}")
        total = size_rng.randint(*self.length)
        body_len = total - len(self.magic) - len(self.prefix)
        body_rng = random.Random(f"makernote-body:{seed}")
        body = bytes(body_rng.getrandbits(8) for _ in range(body_len))
        return self.magic + self.prefix + body
