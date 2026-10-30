"""Per-file metadata randomization.

Static calibration fields stay identical to the reference combiner output;
every identifiable field (timestamps, exposure, serials, lens choice, ...)
is re-rolled so a batch of files shares no surface fingerprint.
See README for the static-vs-randomized table.
"""
from __future__ import annotations

import datetime as _dt
import math
import random

from .filetime import normalize_image_time, utc_image_time


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
        fidelity = (profile.fidelity if profile is not None else None)
        self._fidelity = fidelity
        self._orientations = (list(fidelity.orientations)
                              if fidelity and fidelity.orientations else [1])
        self._software_variants = (
            list(fidelity.software_variants)
            if fidelity and fidelity.software_variants
            else ([profile.software] if profile is not None
                  and profile.software else []))
        self._date_bounds = fidelity.date_bounds() if fidelity else None
        self._asn_r = (fidelity.asn_r if fidelity else None) or (5000, 7600)
        self._asn_b = (fidelity.asn_b if fidelity else None) or (4000, 5600)
        self._baseline = ((fidelity.baseline_exposure if fidelity else None)
                          or (-60, 60))
        self._subject_distance = (fidelity.subject_distance
                                  if fidelity else ())
        self._subject_range = (fidelity.subject_distance_range
                               if fidelity else ())
        self._gps = bool(fidelity and fidelity.emit_gps)
        self._exposure_bias = (fidelity.exposure_bias
                               if fidelity and fidelity.exposure_bias
                               else (0, 0, 0, -33, 33, -67, 67))
        self._flash = (fidelity.flash
                       if fidelity and fidelity.flash is not None else 0)
        self._noise_s = fidelity.noise_s if fidelity else None
        self._noise_o = fidelity.noise_o if fidelity else None
        self._subsec_digits = fidelity.subsec_digits if fidelity else 2
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

    def randomize(self, image_time: _dt.datetime | None = None) -> dict:
        """Fresh metadata dict with identifiable fields randomized.

        ``image_time`` pins the capture timestamp (DateTimeOriginal,
        DateTimeDigitized, OffsetTime* and GPS date/time) instead of
        drawing a random one; the remaining fields still come from the
        seeded stream.  The RNG draw order is unchanged so a given seed
        produces the same non-time metadata either way.
        """
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
        if self._date_bounds:
            start, end = self._date_bounds
            span = max(1, int((end - start).total_seconds()))
            random_base = start + _dt.timedelta(seconds=rng.randint(0, span))
        else:
            random_base = _dt.datetime(2019, 1, 1) + _dt.timedelta(
                seconds=rng.randint(0, 5 * 365 * 24 * 3600)
            )
        if image_time is not None:
            base, offset = normalize_image_time(image_time)
            gps_base = utc_image_time(image_time)
        else:
            base = random_base
            offset = None
            gps_base = base
        dt = base.strftime("%Y:%m:%d %H:%M:%S")
        # Keep the historical RNG draw order for profiles without a
        # fidelity block: only draw these fields when the profile opts in.
        if self._fidelity is not None and self._software_variants:
            software = rng.choice(self._software_variants)
        else:
            software = self._software_variants[0] if self._software_variants else ""
        if self._fidelity is not None and self._orientations:
            orientation = rng.choice(self._orientations)
        else:
            orientation = 1
        if self._fidelity is not None and self._subject_distance:
            subject_distance = rng.choice(self._subject_distance)
            n, d = subject_distance
            if n in (0, 0xFFFFFFFF):
                subject_range = 3          # infinity / distant view
            else:
                metres = n / d if d else 0.0
                subject_range = 1 if metres <= 1.0 else (
                    2 if metres <= 2.0 else 3)
        else:
            subject_distance = (0, 0)
            subject_range = 0
        gps = None
        if self._gps:
            def _deg(max_deg: int) -> tuple[int, int, tuple[int, int]]:
                deg = rng.randint(0, max_deg)
                minute = rng.randint(0, 59)
                sec = rng.randint(0, 59 * 32768 + 32767)
                return deg, minute, (sec, 32768)
            lat = _deg(89)
            lon = _deg(179)
            lat_ref = rng.choice(("N", "S"))
            lon_ref = rng.choice(("E", "W"))
            altitude_mm = rng.randint(0, 500_000)
            gps_hour = rng.randint(0, 23)
            gps_minute = rng.randint(0, 59)
            gps_second = rng.randint(0, 59)
            dop = rng.randint(5_000, 20_000)
            gps = {
                "lat_ref": lat_ref,
                "lat": (lat[0], lat[1], lat[2]),
                "lon_ref": lon_ref,
                "lon": (lon[0], lon[1], lon[2]),
                "altitude_mm": altitude_mm,
                # GPSDateStamp/GPSTimeStamp are UTC; derive them from the
                # pinned local capture time so the two IFDs agree.
                "time": ((gps_base.hour, gps_base.minute, gps_base.second)
                         if image_time is not None
                         else (gps_hour, gps_minute, gps_second)),
                "dop": dop,
                "date": gps_base.strftime("%Y:%m:%d"),
            }
        noise_profile = None
        if self._noise_s and self._noise_o:
            s = math.exp(rng.uniform(math.log(self._noise_s[0]),
                                     math.log(self._noise_s[1])))
            o = math.exp(rng.uniform(math.log(self._noise_o[0]),
                                     math.log(self._noise_o[1])))
            noise_profile = (s, o, s, o, s, o)
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
        asn_r = rng.randint(*self._asn_r)  # AsShotNeutral varies with WB
        asn_b = rng.randint(*self._asn_b)
        bexp = rng.randint(*self._baseline)
        return {
            "datetime": dt,
            "software": software,
            "orientation": orientation,
            "subject_distance": subject_distance,
            "subject_distance_range": subject_range,
            "gps": gps,
            "noise_profile": noise_profile,
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
            "exposure_bias": (rng.choice(self._exposure_bias), 100),
            "flash": self._flash,
            "subsec": str(rng.randint(
                0, 10 ** self._subsec_digits - 1)).zfill(self._subsec_digits),
            "offset": (offset if image_time is not None
                       else rng.choice(["+08:00", "+09:00", "+01:00",
                                        "+02:00", "-05:00"])),
        }


def randomize_metadata(seed: int | None = None,
                       profile=None,
                       image_time: _dt.datetime | None = None) -> dict:
    """Backwards-compatible wrapper: fresh randomized metadata dict."""
    return MetadataRandomizer(seed, profile).randomize(image_time=image_time)


# Module-level aliases for the choice pools (also re-exported by the
# legacy ``stego_dng`` shim).
LENSES = MetadataRandomizer.LENSES
ISO_CHOICES = MetadataRandomizer.ISO_CHOICES
EXPOSURE_CHOICES = MetadataRandomizer.EXPOSURE_CHOICES
FNUMBER_CHOICES = MetadataRandomizer.FNUMBER_CHOICES
METERING_CHOICES = MetadataRandomizer.METERING_CHOICES
EXPPROG_CHOICES = MetadataRandomizer.EXPPROG_CHOICES
