# AGENTS.md — ImageSteg2 (stegodng)

Steganography toolkit that embeds binary payloads in the raw sensor data
of TIFF/DNG files mimicking Fujifilm GFX 100 Pixel Shift Combiner output
(IFD0 JPEG thumbnail + SubIFD 16-bit LinearRaw, EXIF/XMP/DNG tags).
Deep background lives in `README.md` (§1 research, §3 usage); this file
is the operator's guide for changing code.

## Layout

| path | what |
|---|---|
| `stegodng/profile.py` | `CameraProfile` reference constants, depth/geometry limits |
| `stegodng/framing.py` | `PayloadFrame` (magic/len/CRC framing + keystream) |
| `stegodng/metadata.py` | `MetadataRandomizer` (seeded per-file EXIF variety) |
| `stegodng/cover.py` | `CoverGenerator` (synthetic raw covers + gradient thumbnails) |
| `stegodng/codec.py` | `LsbCodec` (LSB embed/extract, capacity, KB formatters) |
| `stegodng/container.py` | `DngContainer` (XMP/EXIF builders, IFD patching incl. BigTIFF, raw reading) |
| `stegodng/sizing.py` | `AutoSizer` (smallest-fit search, max-capacity errors, risk warnings) |
| `stegodng/split.py` | split sizes/naming, chunk-field registries, seq parse/format |
| `stegodng/stego.py` | `DngStego` (`encode`/`encode_split`/`decode`/`generate_tiff`) |
| `stegodng/thumbnails.py` | `ThumbnailProvider` (Commons random photo / synthetic / file) |
| `stegodng/cli.py` | `main()` — argparse commands |
| `stego_dng.py` | **thin compat shim** re-exporting the old single-file API |
| `tests/test_stego.py` | full suite (plain asserts, runnable directly) |
| `images/` | reference RAF/DNG samples (read-only, ~15 GB total, do not modify) |

## Dev environment

- Python 3.14 via the repo venv — always use `.venv/bin/python`
  (and `.venv/bin/pip`), never the system python.
- Install deps with `.venv/bin/pip install -r requirements.txt`
  (`numpy`, `pillow`, `tifffile[all]`; `rawpy` optional, decode checks only).
- Quick smoke: `.venv/bin/python stego_dng.py capacity --width 2048 --height 1536`

## Testing

- Run the suite with `.venv/bin/python tests/test_stego.py` (no pytest;
  every `test_*` must print `ok`, ends with `all tests passed`).
- Keep tests **hermetic**: no network. Pin `thumbnail="synthetic"` on
  every `encode` call; test thumbnail fetching with injected `opener`
  callables (see `test_thumbnail_random_with_fake_opener`).
- After touching IFD/exec paths, also verify with real tools:
  `tiffdump`, `exiv2 -pa` (note: exiv2 cannot parse BigTIFF at all),
  and `rawpy.imread` + `postprocess` where applicable.
- When adding a feature, add tests for it — roundtrip, error paths,
  and CLI subprocess coverage for new flags.

## Architecture notes

- `DngStego` is the orchestrator; `encode()` stays byte-stable (see below).
  New write paths go through `_write_container()`; new read paths through
  `DngContainer`.
- `decode()` accepts one path or a list (chunked sets); planes auto-detect
  1–16 via magic+CRC. Explicit `lsb_planes=` means strict mode.
- Dim/auto logic lives in `AutoSizer.recommend()`; chunk naming/parsing in
  `stegodng/split.py` (`parse_size` accepts `1g/100m/500k/2G/64KB`/bytes).
- CLI (`cli.py`) prints `auto-config`, `warning:`, and `note:` lines to
  stdout, `error:` lines to stderr with exit 1. **All user-facing sizes
  are kilobytes** (`format_kb*` in `codec.py`); never print raw byte counts.

## Gotchas (learned the hard way)

- **Python 3.14 silently drops indented `def` blocks** following blank
  lines at module level (no error, method just missing). After any
  structural edit: `py_compile` AND assert the methods exist / actual
  behavior runs — import success proves nothing.
- `tifffile` merges identical SubIFDs into one series (C-order preserved,
  which striped decode relies on); `DngContainer.raw_frames()` documents this.
- `tifffile` stores YCbCr JPEG planes **verbatim** — convert RGB→YCbCr
  with Pillow before writing or colors come out swapped (there is a
  solid-red regression test; keep it).
- tifffile limitations to route around, not fight: no IFD-pointer tags
  via `extratags` (we rewrite a same-size dummy tag post-write), no
  packed-BPS + compression combo, no `bitspersample` with compression.
- LibRaw (rawpy) rejects Deflate DNGs and >16-bit integer DNGs in this
  environment — raw output defaults to uncompressed for that reason.
- Classic TIFF helpers in `container.py` must stay BigTIFF-aware
  (`_tiff_is_bigtiff`, 8-byte offsets, LONG8/IFD8 element sizes).

## Compatibility rules

- `stego_dng.py` must keep re-exporting the **entire** legacy namespace.
  `test_shim_delegates_to_package` pins the name list — extend it when
  adding public API. Add new public names to both `stegodng/__init__.py`
  (`__all__`) and the shim.
- `DngStego.encode()` output must stay byte-identical for fixed inputs:
  verify with `thumbnail="synthetic"` against known-good files by
  comparing raw arrays + all non-offset tags (offsets legitimately shift
  with JPEG size; skip tags 273/279/324/325/330/34665).
- `README.md` is the user manual: document every new flag, field,
  warning, and detection tradeoff there (see §1.6/§3 for the pattern).

## PR checklist

- `.venv/bin/python tests/test_stego.py` fully green.
- New/changed behavior covered by tests (incl. error messages users see).
- `README.md` + `--help` text updated; new detection risks documented
  with what an inspector would actually observe.
- No network access in tests; no changes under `images/`.
