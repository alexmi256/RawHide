# Profile generation tools

Regenerates `stegodng/profiles/` from the `dpreview-raw` sample tree.
All three scripts are deterministic given the same sample files.

```bash
# 1. per-file EXIF + DNG calibration -> /tmp/opencode/harvest_index.json (~10 min)
python3 tools/harvest_profiles.py
# 2. decoded-dim distribution per model -> /tmp/opencode/geom_all.json (~10 min)
python3 tools/geom_max.py
# 3. profiles + READMEs -> staged, then synced (seconds)
python3 tools/gen_profiles.py
```

`gen_profiles.py` stages into `stegodng/profiles.staging/` and syncs
slug dirs + `PROFILES.md` over; it never touches
`stegodng/profiles/__init__.py` (the registry loader) or the
hand-maintained `stegodng/profiles/custom/` namespace, so regeneration
cannot strand the package. Do **not** `rm -rf stegodng/profiles`.

Custom profiles added under `stegodng/profiles/custom/<slug>/` are loaded
by the registry alongside the harvested ones and are listed in the
`Custom profiles` section of `PROFILES.md`.

After regen: `python3 -m pytest tests/ -q` (includes
`test_camera_profile_data_valid`, which validates every `profile.json`).

## GainMap / OpcodeList2

`gainmap.py` inspects the `OpcodeList2` of a DNG or generates one from a
profile's `"gainmap"` base grid:

```bash
python3 tools/gainmap.py inspect images/pixel_xl/IMG_20261030_094221.dng
python3 tools/gainmap.py generate --profile custom_pixel_xl --seed 7 \
    --width 4048 --height 3036 -o /tmp/opcode_list2.bin
```

The generator lives in `stegodng/opcodes.py`; the profile format is
documented in `stegodng/profiles/custom/custom_pixel_xl/README.md`.

## Raw digests / MakerNote

`digests.py` verifies the two raw identity tags and summarizes the
opaque MakerNote of a DNG:

```bash
python3 tools/digests.py verify images/pixel_xl/IMG_20261030_094221.dng
python3 tools/digests.py makernote images/pixel_xl/IMG_20261030_094221.dng
```

`verify` decodes the raw image (tifffile, falling back to `rawpy` for
lossless-JPEG tiles) and recomputes `NewRawImageDigest` (tag 51111) and
`RawDataUniqueID` (tag 50781) with the DNG SDK rules; it exits 1 on a
mismatch. Both values are reproducible for the Pixel XL samples and for
files written by this package. `makernote` prints the length, head bytes
and byte entropy that the profile's `fidelity.makernote` block models.
