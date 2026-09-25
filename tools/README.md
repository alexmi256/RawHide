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
`stegodng/profiles/__init__.py` (the registry loader), so regeneration
cannot strand the package. Do **not** `rm -rf stegodng/profiles`.

After regen: `python3 -m pytest tests/ -q` (includes
`test_camera_profile_data_valid`, which validates every `profile.json`).
