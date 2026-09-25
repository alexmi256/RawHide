# RAW Image Steganography

Embed arbitrary binary data in the **raw sensor data** of a DNG file whose
structure and metadata mimic Fujifilm GFX 100 / GFX 100 II
Pixel Shift Combiner output. `stego_dng.py` provides `encode` and `decode`
(API + CLI), synthetic TIFF/DNG generation, and per-file metadata
randomization so a batch of files does not share identical fingerprints.

## TL;DR

```bash
pip install -r requirements.txt            # numpy, tifffile[all]
pip install -r requirements-dev.txt        # pytest + pytest-cov (dev)
python stego_dng.py encode -i secret.bin -o out.dng --seed 42
python stego_dng.py decode -i out.dng -o recovered.bin
pytest tests/ -q                           # roundtrip tests
pytest tests/ -q --cov=stegodng --cov=stego_dng --cov-report=term-missing  # coverage
```

## 1. Research findings

### 1.1 TIFF/EP and DNG

* DNG (Adobe Digital Negative, ISO 12234-4) is a TIFF/EP profile: a classic
  TIFF container (`II*\0`, IFD tag directory) plus mandated metadata
  (DNGVersion, ColorMatrix, BlackLevel, …) and EXIF/XMP sub-IFDs.
* TIFF/EP itself defines `SubIFDs` (tag 330), CFA layout tags
  (`CFARepeatPatternDim` 33421, `CFAPattern` 33422), `CFAPlaneColor` (50710)
  and `CFALayout` (50711) — the hooks that describe mosaic sensor data.
* Compression tag 7 = JPEG. DNG readers must support baseline DCT JPEG for
  thumbnails; raw data additionally uses lossless JPEG, and since DNG 1.4
  also Deflate (tag 8, uncompressed = 1).

### 1.2 What the sample files actually contain (`images/`)

Analyzed with `tiffdump`, `exiv2 -pa` and `tifffile`:

| file | size | finding |
|---|---|---|
| `DSCF0143.raf` … (GFX 100 II) | ~199 MB | `FUJIFILMCCD-RAW` header, embedded JPEG/EXIF preview at offset 0x94, proprietary compressed mosaic |
| `image1-original.RAF`, `DSF0349.RAF` (GFX 100) | 70–116 MB | same layout, older firmware (`Ver3.00`) |
| `image1-pixelshift.DNG`, `DSF0350.DNG`, `DSCF1294.DNG`, `fujifilm_gfx_100_pixel_shift_*.dng` | 1.0–1.6 GB | Pixel Shift Combiner output (see below) |

Every combiner DNG has the **same two-IFD skeleton**:

* **IFD0 — JPEG thumbnail**: 4000×3000, 8-bit YCbCr (`Photometric = 6`),
  `Compression = 7`, single strip, `NewSubfileType = 1` (reduced preview).
  Plus `Make = FUJIFILM`, `Model = GFX 100`,
  `Software = FUJIFILM Pixel Shift Combiner`, `DateTime`, `SubIFDs → offset`,
  12288-byte `XMP` (Rating 0 + space padding), `ExifTag → offset`, DNG tags
  (`DNGVersion 1.4.0.0`, `UniqueCameraModel`, `ColorMatrix1/2`,
  `AsShotNeutral`, `CameraSerialNumber`, `LensInfo`, huge `DNGPrivateData`
  81–121 MB, `CalibrationIlluminant 17/21`).
* **SubIFD — the raw image**: **23296×17472 (407 MP)**, 16-bit × 3 ch,
  `PhotometricInterpretation = 34892` (LinearRaw, already demosaiced RGB),
  tiled 128×96 (33124 tiles), `Compression = 7` (lossless JPEG),
  `BlackLevel 255/256`, `WhiteLevel 65535`, `DefaultScale/Crop`,
  `AntiAliasStrength`, `BestQualityScale`, 256-byte `OpcodeList3`.
* **EXIF sub-IFD**: exposure (`ExposureTime`, `FNumber`, `ISOSpeedRatings`,
  `ShutterSpeedValue`, `BrightnessValue`, …), timestamps, focus/drive info,
  Fuji MakerNote (~1.2 KB), `BodySerialNumber`, `LensSpecification/Make/
  Model/SerialNumber`.
* **RAF → DNG conversion**: the GFX bodies write RAF, not DNG.
  `DNGPrivateData` starts with `FUJIFILM…<name>.RAF` followed by a full
  `FUJIFILMCCD-RAW` stream — i.e. the combiner **embeds the source RAF**
  inside the DNG (priv-data length ≈ on-disk RAF size: 111 MB vs 70–116 MB).

### 1.3 Animation / frames in DNG/TIFF — verdict

TIFF supports multi-page files (`NextIFD` chains), SubIFD trees
(DNG thumbnails/full raw), and SubIFD chains. There is **no video/
animation timeline** in still DNG (CinemaDNG = sequence of DNGs, out of
scope). So "frames" give us *layout* options, not temporal hiding:

1. ✅ **Used**: IFD0 thumbnail + SubIFD raw (exactly like the combiner).
2. ⚠️ **Documented alternative**: an extra hidden page/SubIFD carrying an
   encrypted blob — trivially detectable by `exiv2`/tag dump, so it is
   *not* the primary channel (a forensic `tiffdump` lists every IFD).
3. ❌ Rejected: stuffing everything into one metadata tag (detectable,
   size-limited, violates the brief).

### 1.4 Bit depth — verdict

* Combiner output is **16-bit** (`BitsPerSample 16 16 16`,
  `WhiteLevel 65535`) even though the sensor ADC is 14/16-bit — headroom
  that an LSB scheme exploits almost invisibly.
* The tool supports `--bit-depth 8, 10, 12, 14, 16` (default 16).
  Each depth is written as a **real packed `BitsPerSample`** tag
  (8 → uint8 container; 10/12/14 → uint16 container with packed BPS;
  verified with `exiv2` + `tifffile`), with matching `WhiteLevel`
  (`2**depth - 1`) and scaled `BlackLevel` (256 @ 16-bit reference).
  The synthetic cover is rescaled per depth so exposure stays constant
  instead of saturating, and values are quantized to packed steps so
  files round-trip exactly. `rawpy`/LibRaw opens every depth in both
  `linear` and `cfa` modes.
* Key point: **capacity scales with `--lsb-planes`, not with bit depth**
  (`samples × planes / 8 − 18` bytes). Depth controls plausibility and
  file size (packed 12-bit raw ≈ 25% smaller than 16-bit), while planes
  1–16 trade stealth for up to 16× capacity (see §1.6 for the
  detection cost of 5+). Depths below 14 are
  spec-legal TIFF/DNG but less plausible as GFX 100 II output (the body
  offers 14/16-bit), so prefer 14/16 for the cover story.
* Deliberately **not** offered: 24/32-bit *integer* (`BitsPerSample`
  24/32) — verified that LibRaw rejects such DNGs
  (`LibRawFileUnsupportedError`), so files would fail the "opens in a
  real RAW decoder" check. 32-bit *float* (DNG 1.4 HDR) is rawpy-readable
  but needs a separate mantissa-bit codec — documented future work, not
  implemented.

### 1.5 Embedding options (as requested)

| # | channel | payload home | stealth | implemented |
|---|---|---|---|---|
| 1 | **LSB substitution in raw samples** (1–16 planes, 8/10/12/14/16-bit, spread over all tiles/channels, optional SHA-256 keystream; at 16 planes samples are pure payload, no cover remains) | raw SubIFD pixels | high (1–2) → moderate (3–4) → low (5–8) → none (9–16) — survives only lossless codecs | ✅ primary (`encode`/`decode`) |
| 5 | **Multiple raw frames** (`--raw-frames 1–8`): full-res SubIFDs sharing one file, payload striped across them (burst/stack style) | N raw SubIFDs | very low — no still-DNG camera output looks like this | ✅ (`encode`/`decode` handle striping) |
| 2 | Hidden extra IFD/SubIFD frame | file structure | low — listed by any TIFF tool | documented only |
| 3 | `DNGPrivateData` / MakerNote / XMP padding blob | metadata | low — single-field anomaly | placeholder-size field only |
| 4 | sub-16-bit slack (e.g. 14-bit values in packed container) | raw pixels | very high | ✅ via `--bit-depth 14` (also 8/10/12) |

Framing: `DNGS` magic + version + flags + u64 length + CRC32, then payload
(XOR keystream when `--key` is given). Capacity:
`samples × planes / 8 − 18` bytes.

| geometry | mode | 1 plane | 2 planes | 4 planes | 16 planes |
|---|---|---|---|---|---|
| 2048×1536 (default demo) | linear RGB | ~1.1 MB | ~2.3 MB | ~4.7 MB | ~18.9 MB |
| 4000×3000 | linear RGB | ~4.5 MB | ~9 MB | ~18 MB | ~72 MB |
| 11648×8736 (`--gfx-native`, GFX 100 II) | linear RGB | ~38 MB | ~76 MB | ~152 MB | ~582 MB |
| 23296×17472 (`--pixelshift`, 407 MP) | linear RGB | ~145 MB | ~291 MB | ~610 MB | ~2.3 GB |
| any geometry | linear RGB, N `--raw-frames` | ×N | ×N | ×N | ×N (max: 8-frame pixelshift/16-plane ≈ 18.2 GiB) |
| any | CFA mosaic (1 sample/px) | ÷3 of linear | ÷3 | ÷3 | ÷3 |

### 1.6 Density: what cameras actually vary, and what we implemented

Capacity is `samples × planes × frames / 8 − 18` bytes, so density comes
from exactly three knobs — and they are the same knobs real cameras and
the DNG spec use:

1. **Resolution (samples).** The combiner's 23296×17472 output is already
   extreme (407 MP); presets span demo → combiner-scale → gfx-native →
   pixelshift, plus exact-fit `--auto-size` and free `--width/--height`.
2. **Bit depth (bits per sample).** GFX 100 II bodies offer 14/16-bit;
   the tool writes real packed 8/10/12/14/16-bit `BitsPerSample`.
3. **Channel count.** Combiner output is demosaiced LinearRaw (3
   samples/px); `cfa` mosaic mode carries 1 sample/px (÷3 capacity).
4. **Lossless compression — useless here, by measurement.** Random
   (and especially encrypted) payload bits are incompressible;
   `--compression adobe_deflate` saved only ~16% on a 2-plane test file,
   so it stays an opt-in for modest savings, never a density strategy.
5. **Multiple raw frames (`--raw-frames 1–8`).** Multi-image TIFFs are
   established practice (focus/exposure stacks ship as multi-page TIFFs;
   burst modes and CinemaDNG store frame sequences), but multiple
   *full-resolution raw SubIFDs in one still DNG* is non-standard — no
   GFX combiner output looks like this. Payload is striped bit-wise
   across frames in write order; `decode` concatenates frame bitstreams.
   File size grows ~linearly per frame.
6. **BigTIFF (DNG 1.6) as an enabler, not a strategy.** Past ~4 GB
   (e.g. pixelshift ×2+ frames) the writer switches to 64-bit BigTIFF
   and the EXIF/LinearRaw patch steps handle both layouts (verified at
   byte level). Caveat: exiv2 cannot parse BigTIFF at all; tifffile and
   rawpy can.

Deliberately **not** implemented, with reasons:

* **DNG 1.4 32-bit float (HDR).** Genuinely used for HDR merges and some
  phone HDR paths, and rawpy-readable — but hiding data means touching
  mantissa bits only, i.e. *fewer* payload bits per stored byte than
  integer full-replace. A stealth niche, never a density win.
* **24/32-bit integer.** LibRaw rejects such DNGs outright (verified),
  so files fail the real-decoder check.
* **DNG 1.7 JPEG XL.** Lossy modes destroy LSBs by design.

Detection-risk summary (every one of these also prints a CLI `warning:`
at encode time when triggered):

| option | telltales an inspector sees |
|---|---|
| `--lsb-planes 5–8` | cover heavily degraded; bit-plane statistics skewed |
| `--lsb-planes 9–15` | raw renders as degraded noise; histogram flat |
| `--lsb-planes 16` | **no cover at all** — samples are pure payload; trivially exposed by any bit-plane/entropy check (use `--key` so at least contents are opaque) |
| `--raw-frames 2–8` | N full-res SubIFDs in `tiffdump`/`exiv2`; ~N× file size |
| `--bit-depth 8/10/12` | `BitsPerSample` below every GFX 100 II option (14/16) |
| `--auto-size` | dimensions match no camera preset (e.g. 462×348) |
| packed depth + deflate | rejected outright (tifffile limitation) |

### 1.7 Thumbnails: how desktops show DNGs (researched)

Neither Windows Explorer nor Nautilus renders the 16-bit raw for an
icon — both show the **embedded IFD0 JPEG preview**, which is exactly
what this tool writes (Baseline JPEG, YCbCr, same layout as the
combiner files):

* **Windows Explorer** cannot parse DNG natively; thumbnails come from
  WIC codecs (Microsoft's *Raw Image Extension* from the Store, vendor
  codec packs, or the legacy Adobe DNG Codec). The codec reads the IFD0
  preview, never the raw mosaic.
* **Ubuntu Nautilus** never parses images itself: it shells out to
  registered `.thumbnailer` helpers (for RAW typically
  `gnome-raw-thumbnailer`, which extracts the embedded preview, or the
  darktable/RawTherapee thumbnailers). No RAW thumbnailer is installed
  in this container, so verify on a real desktop; any thumbnailer that
  handles combiner DNGs handles ours — same IFD0 construction.
* **Recommended size.** The DNG spec only requires *a* thumbnail in
  IFD0; viewers downscale it to 128–512 px cache entries regardless.
  We keep combiner parity: up to 4000×3000 (capped by image dims), same
  aspect as the raw frame. Verified: IFD0 extracts with `tifffile` and
  decodes with Pillow to the exact frame size with faithful colors.

The *picture* inside that JPEG defaults to a random photo from
Wikimedia Commons (`Special:Random/Image` → redirect resolved to the
`File:` page → pixels via `Special:FilePath?width=` server-side
downscale, non-photo types skipped with another pick). Chain verified
live, including the redirect hops. Behavior notes:

* source is center-cropped to the thumbnail frame aspect and
  Lanczos-resized — never stretched;
* any fetch/decode failure (offline included) falls back to a small
  generated noise image after 3 attempts (~10 s timeout each), so
  offline encodes keep working — pass `--thumbnail synthetic` to skip
  the network entirely, or `--thumbnail PATH` for your own picture;
* found and fixed while doing this: tifffile stores YCbCr JPEG planes
  verbatim, so the old code's RGB input decoded with swapped chroma
  (regression test: solid-red thumbnail decodes red-dominant).

## 2. Metadata: static vs randomized

Static fields are copied verbatim from the combiner samples
(`ColorMatrix1/2`, `CalibrationIlluminant 17/21`, `AnalogBalance`,
`OpcodeList3` 256-byte blob, `Make`, `Model`, `Software`, XMP skeleton…).
Every `encode` re-rolls the identifiable fields (seeded by `--seed`):

randomized: `DateTime` (+`DateTimeOriginal/Digitized`, `OffsetTime*`,
`SubSecTime*`), `ExposureTime`/`ShutterSpeedValue`, `FNumber`/`ApertureValue`,
`ExposureProgram`, `ISOSpeedRatings`, `MeteringMode`, `FocalLength`
(+35 mm equiv, consistent GF lens pick from 8 real lenses),
`MaxApertureValue`, `BrightnessValue`, `ExposureBiasValue`,
`CameraSerialNumber`, `BodySerialNumber`, `LensSerialNumber`,
`AsShotNeutral`, `BaselineExposure`, plus fresh cover and
thumbnail pixels. No GPS tags are written (samples have none).
(`ImageNumber` is *not* randomized — on split chunks it carries the
deterministic chunk sequence; plain files omit it.)

## 3. Usage

```bash
# embed: omit sizing flags and the smallest fitting config is auto-chosen
python stego_dng.py encode -i secret.bin --seed 42  # -> secret.bin.dng (-o optional)
python stego_dng.py encode -i secret.bin -o out.dng --seed 42  # explicit output
# ... or exact-fit dimensions for the smallest possible file (see tradeoff below)
python stego_dng.py encode -i secret.bin -o small.dng --auto-size --seed 42
# ... or pin any subset explicitly (the rest still auto-fits)
python stego_dng.py encode -i secret.bin -o big.dng --gfx-native --seed 7 --key s3cret
python stego_dng.py encode -i secret.bin -o cfa.dng --mode cfa --bit-depth 14 --lsb-planes 2
python stego_dng.py encode -i secret.bin -o max.dng --gfx-native --bit-depth 16 --lsb-planes 4  # max stealth-off capacity
python stego_dng.py encode -i huge.bin -o stack.dng --auto-size --raw-frames 4 --lsb-planes 16 --key s3cret  # max density, max risk
python stego_dng.py encode -i secret.bin -o mypic.dng --thumbnail photo.jpg  # own preview picture
# split a big payload: ≤100 MB per DNG, DCF-style numbered files
python stego_dng.py encode -i huge.raw --split-file 100m --seed 7
# -> huge.raw0001.dng huge.raw0002.dng ... (shared UUID + sequence in metadata)
# (explicit -o still works: -o vol.dng -> vol0001.dng vol0002.dng ...)
python stego_dng.py decode -i vol0001.dng vol0002.dng -o huge.raw

# extract (--lsb-planes auto-detected; only --key must match)
python stego_dng.py decode -i out.dng -o recovered.bin
# opt-in safety cap on the declared payload per file (default: image
# capacity, so any file this tool can encode also decodes)
python stego_dng.py decode -i out.dng -o recovered.bin --max-bytes 500m

# helpers
python stego_dng.py capacity --width 23296 --height 17472 --lsb-planes 4
python stego_dng.py gen-tiff -o cover.tif --width 1024 --height 768
```

Auto-sizing (`recommend_config()`): with no sizing flags, `encode` walks
`2048x1536 -> 4000x3000 -> 11648x8736 (gfx-native) -> 23296x17472
(pixelshift)`, picking the smallest geometry — and within it the fewest
LSB planes (1-16, capped by the bit depth) — that fits the input
(defaults: `linear`, 16-bit; `--raw-frames` multiplies capacity).
Pinning `--width/--height` keeps your geometry and only bumps planes;
pinning `--lsb-planes` keeps your stealth level and only grows geometry.
A one-sided `--width`/`--height` completes via the 4:3 GFX aspect.
`--auto-size` instead computes the smallest even 4:3 width/height holding
the payload (floored at 64x48), ignoring the presets entirely — files get
much smaller (a 58.6 KB payload: 1.3 MB file vs 20.3 MB at the auto
2048x1536 preset), but arbitrary dimensions like 462x348 match no real
GFX output and may look unusual under inspection. That stealth-vs-size
tradeoff is the user's call; every `--auto-size` run prints a warning
saying so. `--auto-size` cannot be combined with
`--width/--height/--gfx-native/--pixelshift`.
If nothing fits, the error states the payload size, the relevant maximum
(absolute single-frame max: 23296x17472 linear 16-bit, 16 planes =
2,384,928.0 KB; `--raw-frames 8` multiplies any capacity ×8)
and suggests larger geometry / more planes / auto-sizing / splitting the
input. `decode` needs no sizing flags: it tries 1-16 planes and accepts the
one passing the magic+CRC check (explicit `--lsb-planes` = strict mode).
`decode` bounds the accepted payload by the image capacity, so every
encodable file decodes by default; `--max-bytes SIZE` (same `1g`/`100m`/
`500k`/bare-count syntax as `--split-file`) opts into a smaller safety cap per
file, and the API's `max_bytes=None` default behaves the same (pass an int
to cap). For untrusted files, pass an explicit `--max-bytes`/`max_bytes`
to bound the allocation before the capacity check runs. When a header match
is rejected by that cap or by capacity, the error names the limit instead
of the generic wrong-key hint.

All user-facing sizes (encode/decode/capacity output and errors) are
reported in kilobytes.

### Splitting one payload across files

`--split-file SIZE` (kilobytes/megabytes/gigabytes: `500k`, `100m`,
`1g`, also `2G`, `64KB`, or bare bytes) caps the payload bytes per DNG.
`-o` is optional: without it the output defaults to `<input>.dng`
(e.g. `secret.bin` -> `secret.bin.dng`); with `--split-file` the
sequence numbers are inserted before that extension (e.g. `huge.raw`
-> `huge.raw0001.dng`, `huge.raw0002.dng`, …).
With an explicit `-o out.dng`, chunks become `out0001.dng`,
`out0002.dng`, … — 4-digit sequences
from 0001 in the spirit of DCF camera filenames. Each chunk is an
independent framed payload (own header/CRC), so a short last chunk
needs no padding and no resolution tricks; a corrupt chunk fails on its
own CRC. If everything fits in one chunk, output is a plain single DNG
with no split markers at all — i.e. `<input>.dng` on the default path
(or the exact `-o` path), not a `0001`-numbered file.

Chunk bookkeeping lives in two metadata fields (split-only; plain files
omit them):

| flag | default | alternatives | `none` |
|---|---|---|---|
| `--split-file-metadata-id` | `ImageUniqueID` (EXIF 42016: a genuine per-image UUID field; a UUID4 hex fits its 32-char format natively) | `ImageDescription` | shared set UUID unwritten |
| `--split-file-metadata-seq` | `ImageNumber` (TIFF/EP tag 0x9211 = 37393 decimal in EXIF: exists precisely to number images in a sequence; renders in exiv2 only with `-u` as `0x9211`, recognized by name in ExifTool) | `PageNumber` (stores sequence+total natively), `ImageDescription` (`0003/0012` text) | sequence unwritten |

Fail-open warning: `ImageNumber` stores a scalar with **no total**, so
decoding a consecutive-from-0001 subset (e.g. chunks 1–2 of 3) succeeds
and silently returns truncated data — pinned by test, not accidental.
Use `PageNumber` when a missing tail must fail closed (decode then
rejects subsets against the declared total).

Tradeoff to know: the shared UUID *links* the chunks (its purpose —
renamed files still reassemble by UUID order), which a forensic pass
can also see; `none`/`none` leaves sequencing purely to filenames.
`--split-file-id` overrides the generated UUID (handy for tests).

Decode takes several `-i` files and verifies the set: metadata (when
present) must agree on one UUID with 1..N sequences and matching
totals, otherwise filenames must be one stem with consecutive numbers
from 0001. Mixed sets (some files marked, some not), gaps
(`test0001` + `test0003` → missing `0002`), and starts past 0001 all
fail with the missing numbers spelled out. Without totals (fields
`none`), the given files are assumed complete — a forgotten file is on
you. One lone chunk decodes with a partial-data warning.

Python API (package `stegodng`; `stego_dng.py` remains as a thin
compatibility shim re-exporting the old names):

```python
from stegodng import DngStego, AutoSizer

stego = DngStego()
info = stego.encode(payload, "out.dng", seed=42)  # explicit geometry
payload = stego.decode("out.dng")                 # planes auto-detected
cfg = AutoSizer().recommend(len(payload))         # auto-sizing
```

Module layout:

| module | classes | responsibility |
|---|---|---|
| `profile.py` | `CameraProfile` | GFX reference constants, per-depth levels, geometry presets/limits |
| `framing.py` | `PayloadFrame` | magic/length/CRC framing + keystream |
| `metadata.py` | `MetadataRandomizer` | per-file metadata re-rolling |
| `cover.py` | `CoverGenerator` | synthetic raw covers + JPEG thumbnails |
| `codec.py` | `LsbCodec` | LSB embed/extract, capacity, KB formatting |
| `container.py` | `DngContainer` | XMP/EXIF builders, BigTIFF-aware IFD patching, raw reading |
| `sizing.py` | `AutoSizer` | smallest-fit search, max-capacity errors, risk warnings |
| `split.py` | — | chunk sizing/naming, split-field registries, seq parse/format |
| `stego.py` | `DngStego` | `encode` / `decode` / `generate_tiff` orchestration |
| `cli.py` | — | `encode` / `decode` / `capacity` / `gen-tiff` commands |
| `thumbnails.py` | `ThumbnailProvider` | random-Commons / synthetic / file preview pictures, aspect crop + resize, noise fallback |


## 4. Implementation notes

* Writer: `tifffile.TiffWriter` (IFD0 JPEG thumbnail + SubIFD raw, tiled
  128×96 like the combiner) → in-place patch of SubIFD
  `PhotometricInterpretation` 2 → 34892 (LinearRaw; tifffile can only
  *write* that geometry as RGB) → EXIF Sub-IFD appended at EOF and linked
  via tag 34665 (tifffile filters IFD-pointer tags, so a same-size dummy
  private tag is repurposed — no byte shifting). CFA mode additionally
  writes `CFAPlaneColor`/`CFALayout`, which LibRaw requires.
* **Lossless only**: the raw SubIFD defaults to *uncompressed*. Reason
  found by experiment: the LibRaw in this environment decodes uncompressed
  DNG fine but fails on Adobe-Deflate DNG (`unexpected EOF`); lossy JPEG
  would destroy LSBs by design. `--compression adobe_deflate` remains as
  an opt-in (still lossless → payload-safe, tifffile-decodable).
* Verified: `tiffdump` layout ≈ reference, `exiv2 -pa` shows the full
  Maker/EXIF/DNG/XMP set, `rawpy.imread` + postprocess succeeds for both
  `linear` and `cfa` outputs at every supported depth (8/10/12/14/16) and
  1–16 LSB planes and 1–8 frames, and `decode(encode(x)) == x` for all
  combinations
  (see `tests/test_stego.py`).
* Constraint found by experiment: tifffile cannot combine packed
  `BitsPerSample` (10/12/14) with compression, so `--compression
  adobe_deflate` is only accepted with `--bit-depth 8/16` (full-width);
  packed depths always write uncompressed (still lossless → payload-safe).
* **In-place embedding (memory)**: `LsbCodec.stripe_frames` /
  `LsbCodec.embed_bits` embed directly into the passed cover arrays and
  return those same objects — a cover is *consumed* by embedding, so do
  not reuse it afterwards (re-embedding the same frame is idempotent,
  but old pixel values are gone). Contrast `embed_bitarray`, the legacy
  bit-array helper, which still allocates and returns a new array.
* `requirements.txt`: `numpy`, `tifffile[all]` (`rawpy` optional, decode
  verification only). Dev-only test deps (`pytest`, `pytest-cov`) live in
  `requirements-dev.txt`.

## 5. Limitations / out of scope

* No real sensor data: the cover is a synthetic gradient + noise (opening
  the DNG and judging photographic content is out of scope per the brief).
* `DNGPrivateData` is a small placeholder, not an embedded RAF (real files
  carry 80–120 MB); MakerNote is omitted for the same reason.
* `--pixelshift` (407 MP) writes a ~2.5 GB uncompressed file; peak
  encode RAM is analytically ~2x the payload plus one cover buffer
  (2.3 GB here, unmeasured at GB scale — e.g. ~4.3 GB for a 1 GB
  payload) — covers are embedded in place and `--split-file` chunks
  stream one at a time, so splitting keeps peak near a single chunk's
  cost. Removing the remaining framed-payload copy (streaming frame,
  P1) would cut roughly another 1x payload; `--gfx-native` (489 MB
  file, 20 MB payload) was tested end-to-end.
* Keystream XOR gives confidentiality against casual inspection, not
  authenticated encryption; wrong `--key` fails closed (magic/CRC check).
