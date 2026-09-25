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

    def __init__(self, seed: int | None = None,
                 profile=None) -> None:
        self._rng = random.Random(seed)
        # Per-camera pools (None -> GFX reference pools above).
        self._profile = profile
        self._lenses = (list(profile.lenses) if profile is not None
                        and profile.lenses else list(self.LENSES))
        self._isos = (list(profile.iso_choices) if profile is not None
                      and profile.iso_choices else list(self.ISO_CHOICES))
        self._exposures = (list(profile.exposure_choices)
                           if profile is not None and profile.exposure_choices
                           else list(self.EXPOSURE_CHOICES))
        self._fnumbers = (list(profile.fnumber_choices)
                          if profile is not None and profile.fnumber_choices
                          else list(self.FNUMBER_CHOICES))
        self._metering = (list(profile.metering_choices)
                          if profile is not None and profile.metering_choices
                          else list(self.METERING_CHOICES))
        self._expprog = (list(profile.exposure_program_choices)
                         if profile is not None
                         and profile.exposure_program_choices
                         else list(self.EXPPROG_CHOICES))
        self._serial_prefixes = (list(profile.serial_prefixes)
                                 if profile is not None
                                 and profile.serial_prefixes
                                 else ["92A", "94A", "93A", "95A"])
        self._crop = (profile.crop_factor if profile is not None
                      else 0.79)
        self._lens_make_default = (profile.make if profile is not None
                                   else "FUJIFILM")
        # Serial pools: the reference profile keeps its legacy hardcoded
        # body/lens serials (byte stability); harvested profiles use
        # fresh random serials in observed prefix formats.
        self._legacy_serials = (profile is None
                                or getattr(profile, "slug", "") == "gfx_100")

    @staticmethod
    def _rand_serial(rng: random.Random, prefix: str = "") -> str:
        alphabet = "0123456789ABCDEF"
        body = "".join(rng.choice(alphabet) for _ in range(8 - len(prefix)))
        return prefix + body

    def randomize(self) -> dict:
        """Fresh metadata dict with identifiable fields randomized."""
        rng = self._rng
        lens = rng.choice(self._lenses)
        # Profile lenses carry (model, min, max, aperture[, make]);
        # reference LENSES are (model, min, max, aperture).
        lens_make = ((lens[4] or self._lens_make_default)
                     if len(lens) > 4 else self._lens_make_default)
        focal = round(rng.uniform(lens[1], lens[2]), 1)
        iso = rng.choice(self._isos)
        exp_n, exp_d = rng.choice(self._exposures)
        fnum = rng.choice(self._fnumbers)
        fnum_pair = tuple(fnum) if isinstance(fnum, (list, tuple)) else (fnum, 100)
        base = _dt.datetime(2019, 1, 1) + _dt.timedelta(
            seconds=rng.randint(0, 5 * 365 * 24 * 3600)
        )
        dt = base.strftime("%Y:%m:%d %H:%M:%S")
        serial = self._rand_serial(rng, rng.choice(self._serial_prefixes))
        if self._legacy_serials:
            body_serial = rng.choice(["33000087", "94000525", serial])
            lens_serial = self._rand_serial(
                rng, rng.choice(["75A", "86A", "35A", "19A"]))
        else:
            body_serial = self._rand_serial(
                rng, rng.choice(self._serial_prefixes))
            lens_serial = self._rand_serial(
                rng, rng.choice(self._serial_prefixes))
        r35 = int(round(focal * self._crop))  # sensor crop factor
        asn_r = rng.randint(5000, 7600)   # AsShotNeutral varies with WB
        asn_b = rng.randint(4000, 5600)
        bexp = rng.randint(-60, 60)       # +/- 0.006 EV baseline tweaks
        return {
            "datetime": dt,
            "exposure_time": (exp_n, exp_d),
            "fnumber": fnum_pair,
            "exposure_program": rng.choice(self._expprog),
            "iso": iso,
            "metering": rng.choice(self._metering),
            "focal": focal,
            "focal_rational": (int(round(focal * 100)), 100),
            "focal_35mm": r35,
            "max_aperture": (int(round(lens[3] * 100)), 100),
            "lens": lens[0],
            "lens_make": lens_make,
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


def randomize_metadata(seed: int | None = None,
                       profile=None) -> dict:
    """Backwards-compatible wrapper: fresh randomized metadata dict."""
    return MetadataRandomizer(seed, profile).randomize()


# Module-level aliases for the choice pools (also re-exported by the
# legacy ``stego_dng`` shim).
LENSES = MetadataRandomizer.LENSES
ISO_CHOICES = MetadataRandomizer.ISO_CHOICES
EXPOSURE_CHOICES = MetadataRandomizer.EXPOSURE_CHOICES
FNUMBER_CHOICES = MetadataRandomizer.FNUMBER_CHOICES
METERING_CHOICES = MetadataRandomizer.METERING_CHOICES
EXPPROG_CHOICES = MetadataRandomizer.EXPPROG_CHOICES
