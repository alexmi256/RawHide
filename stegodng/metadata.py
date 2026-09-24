"""Per-file metadata randomization.

Static calibration fields stay identical to the reference combiner output;
every identifiable field (timestamps, exposure, serials, lens choice, ...)
is re-rolled so a batch of files shares no surface fingerprint.
See README for the static-vs-randomized table.
"""
from __future__ import annotations

import datetime as _dt
import random


class MetadataRandomizer:
    # Plausible GF lenses: (model, min_focal_mm, max_focal_mm, max_aperture)
    LENSES = [
        ("GF63mmF2.8 R WR", 63.0, 63.0, 2.8),
        ("GF120mmF4 R LM OIS WR Macro", 120.0, 120.0, 4.0),
        ("GF55mmF1.7 R WR", 55.0, 55.0, 1.7),
        ("GF110mmF2 R LM WR", 110.0, 110.0, 2.0),
        ("GF32-64mmF4 R LM WR", 32.0, 64.0, 4.0),
        ("GF100-200mmF5.6 R LM OIS WR", 100.0, 200.0, 5.6),
        ("GF23mmF4 R LM WR", 23.0, 23.0, 4.0),
        ("GF250mmF4 R LM OIS WR", 250.0, 250.0, 4.0),
    ]

    ISO_CHOICES = [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800,
                   1000, 1250, 1600, 3200, 6400]
    # (numerator, denominator) exposure times seen on Fuji bodies + neighbours
    EXPOSURE_CHOICES = [
        (10, 8000), (10, 4000), (10, 2000), (10, 1000), (10, 500), (10, 250),
        (10, 125), (10, 60), (10, 30), (10, 21), (10, 17), (10, 16), (10, 8),
        (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (15, 10), (20, 10),
        (30, 10), (50, 10), (60, 10),
    ]
    FNUMBER_CHOICES = [170, 200, 250, 280, 320, 400, 560, 710, 800, 1100, 1600, 2200, 3200]
    METERING_CHOICES = [2, 3, 5]  # center-weighted, spot, multi-segment
    EXPPROG_CHOICES = [1, 2, 3, 4]  # manual, program, aperture-prio, shutter-prio

    def __init__(self, seed: int | None = None) -> None:
        self._rng = random.Random(seed)

    @staticmethod
    def _rand_serial(rng: random.Random, prefix: str = "") -> str:
        alphabet = "0123456789ABCDEF"
        body = "".join(rng.choice(alphabet) for _ in range(8 - len(prefix)))
        return prefix + body

    def randomize(self) -> dict:
        """Fresh metadata dict with identifiable fields randomized."""
        rng = self._rng
        lens = rng.choice(self.LENSES)
        focal = round(rng.uniform(lens[1], lens[2]), 1)
        iso = rng.choice(self.ISO_CHOICES)
        exp_n, exp_d = rng.choice(self.EXPOSURE_CHOICES)
        fnum = rng.choice(self.FNUMBER_CHOICES)
        base = _dt.datetime(2019, 1, 1) + _dt.timedelta(
            seconds=rng.randint(0, 5 * 365 * 24 * 3600)
        )
        dt = base.strftime("%Y:%m:%d %H:%M:%S")
        serial = self._rand_serial(rng, rng.choice(["92A", "94A", "93A", "95A"]))
        body_serial = rng.choice(["33000087", "94000525", serial])
        lens_serial = self._rand_serial(rng, rng.choice(["75A", "86A", "35A", "19A"]))
        r35 = int(round(focal * 0.79))  # GFX 0.79x crop factor
        asn_r = rng.randint(5000, 7600)   # AsShotNeutral varies with WB
        asn_b = rng.randint(4000, 5600)
        bexp = rng.randint(-60, 60)       # +/- 0.006 EV baseline tweaks
        return {
            "datetime": dt,
            "exposure_time": (exp_n, exp_d),
            "fnumber": (fnum, 100),
            "exposure_program": rng.choice(self.EXPPROG_CHOICES),
            "iso": iso,
            "metering": rng.choice(self.METERING_CHOICES),
            "focal": focal,
            "focal_rational": (int(round(focal * 100)), 100),
            "focal_35mm": r35,
            "max_aperture": (int(round(lens[3] * 100)), 100),
            "lens": lens[0],
            "lens_spec": (
                int(round(lens[1] * 100)), 100, int(round(lens[2] * 100)), 100,
                int(round(lens[3] * 100)), 100, int(round(lens[3] * 100)), 100,
            ),
            "camera_serial": serial,
            "body_serial": body_serial,
            "lens_serial": lens_serial,
            "image_number": rng.randint(1000, 99999),
            "sequence": rng.randint(0, 9),
            "as_shot_neutral": [(asn_r, 10000), (10000, 10000), (asn_b, 10000)],
            "baseline_exposure": (bexp, 10000),
            "brightness": (rng.randint(100, 600), 100),
            "exposure_bias": (rng.choice([0, 0, 0, -33, 33, -67, 67]), 100),
            "subsec": f"{rng.randint(0, 99):02d}",
            "offset": rng.choice(["+08:00", "+09:00", "+01:00", "+02:00", "-05:00"]),
        }


def randomize_metadata(seed: int | None = None) -> dict:
    """Backwards-compatible wrapper: fresh randomized metadata dict."""
    return MetadataRandomizer(seed).randomize()


# Module-level aliases for the choice pools (also re-exported by the
# legacy ``stego_dng`` shim).
LENSES = MetadataRandomizer.LENSES
ISO_CHOICES = MetadataRandomizer.ISO_CHOICES
EXPOSURE_CHOICES = MetadataRandomizer.EXPOSURE_CHOICES
FNUMBER_CHOICES = MetadataRandomizer.FNUMBER_CHOICES
METERING_CHOICES = MetadataRandomizer.METERING_CHOICES
EXPPROG_CHOICES = MetadataRandomizer.EXPPROG_CHOICES
