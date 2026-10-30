# Custom camera profiles

Hand-maintained profiles live here as `custom/<slug>/profile.json` +
`README.md`. They are loaded by the same registry as the harvested
`stegodng/profiles/<slug>/` entries, so `--camera-profile=<slug>` and the
Python API (`get_profile`, `list_profiles`, `resolve`) work unchanged.

Use this namespace for profiles built from personal camera samples or for
cover stories that should not be overwritten by `tools/gen_profiles.py`.
The generator preserves this directory when it prunes stale harvested
profiles.

Each `profile.json` follows the same schema as a harvested profile; the
per-profile `README.md` documents where the values came from and what the
current writer does and does not reproduce.
