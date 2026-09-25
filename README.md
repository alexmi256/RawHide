# RAW Image Steganography

Embed arbitrary binary data in the **raw sensor data** of a DNG file whose
structure and metadata mimic Fujifilm GFX 100 / GFX 100 II
Pixel Shift Combiner output. `stego_dng.py` provides `encode` and `decode`
(API + CLI), synthetic TIFF/DNG generation, and per-file metadata
randomization so a batch of files does not share identical fingerprints.

## TL;DR

```bash
pip install -r requirements.txt            # numpy, pillow, tifffile[all], tqdm
pip install -r requirements-dev.txt        # pytest + pytest-cov (dev)
python stego_dng.py encode -i secret.bin -o out.dng --seed 42
python stego_dng.py decode -i out.dng -o recovered.bin
pytest tests/ -q                           # roundtrip tests
pytest tests/ -q --cov=stegodng --cov=stego_dng --cov-report=term-missing  # coverage
```

## 1. What it does

- **Hides bytes in raw pixels.** The payload is framed (`DNGS` magic +
  version + flags + 64-bit length + CRC32, XOR keystream when `--key` is
  given) and written into the low N bit planes (`--lsb-planes 1–16`) of
  the raw SubIFD, spread over all tiles and channels.
- **Looks like a combiner DNG.** Every output has the same skeleton:
  IFD0 Baseline-JPEG thumbnail plus one or more raw SubIFDs, with EXIF,
  XMP, and DNG tags copied from GFX 100 reference values.
- **Capacity is predictable.** Usable bytes per file are approximately:

  `samples × planes × frames / 8 − 18`

  where samples = width × height × channels (3 for `linear`, 1 for `cfa`).

| geometry | 1 plane | 2 planes | 4 planes | 16 planes |
|---|---|---|---|---|
| 2048×1536 (default auto pick) | ~1.2 MB | ~2.4 MB | ~4.7 MB | ~18.9 MB |
| 4000×3000 | ~4.5 MB | ~9.0 MB | ~18.0 MB | ~72.0 MB |
| 11648×8736 (`--gfx-native`) | ~38.2 MB | ~76.3 MB | ~153 MB | ~611 MB |
| 23296×17472 (`--pixelshift`) | ~153 MB | ~305 MB | ~611 MB | ~2.44 GB |

  Table uses decimal MB/GB (1 MB = 1,000,000 bytes); the CLI itself
  reports KiB (1 KB = 1024 bytes, see `capacity` command).

  `--raw-frames 1–8` multiplies any row by N. `cfa` mosaic mode carries
  1 sample/px, so divide linear capacities by 3.

- **Decode needs almost nothing.** Plane count is auto-detected
  (magic + CRC trial over 1–16); only `--key` must match. Explicit
  `--lsb-planes` switches decode to strict mode.
- **Big payloads can split.** `--split-file SIZE` stripes one input
  across numbered DNGs with a shared UUID + sequence in metadata.
- **Every file looks different.** Cover pixels, thumbnail picture, and
  identifiable EXIF fields are re-rolled per encode (seeded by `--seed`).
  See §6 for the full field list.
- **Covers and previews are synthetic by default.** The raw is a
  gradient + noise field; the IFD0 JPEG is a random Commons photo
  (with offline noise fallback), a built-in gradient, or your own image.

## 2. Usage

### 2.1 Basic encode / decode

```bash
# smallest fitting preset is auto-chosen; -o optional (<input>.dng)
python stego_dng.py encode -i secret.bin --seed 42
python stego_dng.py encode -i secret.bin -o out.dng --seed 42

# encrypted payload
python stego_dng.py encode -i secret.bin -o big.dng --gfx-native --seed 7 --key s3cret

# mosaic layout, packed depth, 2 planes
python stego_dng.py encode -i secret.bin -o cfa.dng --mode cfa --bit-depth 14 --lsb-planes 2

# own preview picture instead of a random/synthetic one
python stego_dng.py encode -i secret.bin -o mypic.dng --thumbnail photo.jpg

# extract (planes auto-detected; only --key must match)
python stego_dng.py decode -i out.dng -o recovered.bin

# safety cap on the declared payload per file (default: image capacity)
python stego_dng.py decode -i out.dng -o recovered.bin --max-bytes 500m
```

### 2.2 Sizing

With no sizing flags, `encode` picks the smallest preset — and within it
the fewest LSB planes — that fits the input:

`2048x1536 -> 4000x3000 -> 11648x8736 (gfx-native) -> 23296x17472 (pixelshift)`

Defaults inside that search are `linear`, 16-bit, 1 frame.
The chosen config is printed as an `auto-config ...` line.

```bash
# exact-fit dimensions for the smallest possible file (see tradeoff below)
python stego_dng.py encode -i secret.bin -o small.dng --auto-size --seed 42

# maximum plausible single-frame density
python stego_dng.py encode -i secret.bin -o max.dng --gfx-native --bit-depth 16 --lsb-planes 4

# maximum absolute density (noisy, non-standard, encrypt it)
python stego_dng.py encode -i huge.bin -o stack.dng --auto-size --raw-frames 4 --lsb-planes 16 --key s3cret
```

Rules of thumb:

- Pinning `--width/--height` keeps your geometry and only bumps planes.
- Pinning `--lsb-planes` keeps your stealth level and only grows geometry.
- A one-sided `--width`/`--height` completes via the 4:3 GFX aspect.
- `--auto-size` computes the smallest even 4:3 frame holding the payload
  (floored at 64x48). Files get much smaller (a 58.6 KB payload: ~1.3 MB
  vs ~20.3 MB at the 2048x1536 preset), but dimensions like 462x348 match
  no real GFX output. Every `--auto-size` run prints a warning; the
  tradeoff is yours.
- `--auto-size` cannot be combined with
  `--width/--height/--gfx-native/--pixelshift`.
- If nothing fits, the error states the payload size, the relevant
  maximum, and suggests larger geometry, more planes, more frames,
  auto-sizing, or splitting.
- `decode` bounds the accepted payload by image capacity, so every
  encodable file decodes by default. For untrusted files, pass an
  explicit `--max-bytes` to bound the allocation first.

All user-facing sizes (output, errors, `capacity`) are kilobytes.

### 2.3 Splitting one payload across files

```bash
# ≤100 MB of payload per DNG, DCF-style numbered files in an album dir
python stego_dng.py encode -i huge.raw --split-file 100m --seed 7
# -> huge/huge.raw0001.dng huge/huge.raw0002.dng ...

# explicit -o still works: -o vol.dng -> huge/vol0001.dng huge/vol0002.dng ...
# (album dir is <output-dir>/<input-stem>; chunk stems come from -o)
python stego_dng.py encode -i huge.raw -o vol.dng --split-file 100m --seed 7
python stego_dng.py decode -i huge/vol0001.dng huge/vol0002.dng -o huge.raw

# flat layout (no album dir)
python stego_dng.py encode -i huge.raw -o vol.dng --split-file 100m \
  --no-split-file-album --seed 7
# -> vol0001.dng vol0002.dng ...
```

- `--split-file SIZE` accepts `500k`, `100m`, `1g` (also `2G`, `64KB`,
  or bare bytes) and caps payload bytes per DNG.
- Without `-o`, the default is `<input>.dng` with sequence numbers
  inserted before the extension.
- `--split-file-album` (on by default; `--no-split-file-album` disables)
  groups chunks in `<output-dir>/<input-stem>/`, where `<input-stem>` is
  the input basename minus its last extension (`huge.raw` -> `huge`).
  Only takes effect with `--split-file` (a single-chunk payload still
  lands inside the album dir).
- Each chunk is an independent framed payload (own header/CRC), so a
  short last chunk needs no padding. If everything fits in one chunk,
  output is a plain single DNG with no split markers.
- Chunks share a UUID and carry a sequence number in metadata (see §3.3).
  Decode verifies the set: one UUID, sequences 1..N, matching totals when
  the field stores them. Gaps, mixed sets, and starts past 0001 fail with
  the missing numbers spelled out. Without totals, the given files are
  assumed complete. One lone chunk decodes with a partial-data warning.

### 2.4 Python API

Package `stegodng`; `stego_dng.py` is a thin compatibility shim
re-exporting the old names.

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
| `progress.py` | — | tqdm helpers (stderr bars, `True`/`False`/`None`=auto) |
| `cli.py` | — | `encode` / `decode` / `capacity` / `gen-tiff` commands |
| `thumbnails.py` | `ThumbnailProvider` | random-Commons / synthetic / file preview pictures |

### 2.5 Helpers and progress bars

```bash
python stego_dng.py capacity --width 23296 --height 17472 --lsb-planes 4
python stego_dng.py gen-tiff -o cover.tif --width 1024 --height 768

# force progress bars on when piped (default: TTY only)
python stego_dng.py encode -i secret.bin -o out.dng --progress
```

Encode/decode show tqdm bars on a TTY (per-chunk `Embedding`/`Extracting`
bars plus an outer `Encoding chunks` / `Decoding chunks` counter for
`--split-file` sets). `--progress` forces them on, `--no-progress`
silences them. The Python API takes the same tri-state:
`progress=True/False/None` (`None` = auto, the default).

## 3. Options reference

### 3.1 `encode` flags

| flag | default | what it does |
|---|---|---|
| `-i, --input` | (required) | payload file to embed |
| `-o, --output` | `<input>.dng` | output DNG path; with `--split-file`, `0001`-style numbers go before the extension; with `--split-file-album` (on) chunks move into `<output-dir>/<input-stem>/` |
| `--width, --height` | auto | raw frame size; one-sided values complete via 4:3; pinned geometry only bumps planes |
| `--gfx-native` | off | shortcut for `11648x8736` (~102 MP sensor scale) |
| `--pixelshift` | off | shortcut for `23296x17472` (~407 MP combiner scale, GB-size file, needs lots of RAM) |
| `--auto-size` | off | compute the smallest even 4:3 frame that fits; smallest files, non-standard dims |
| `--lsb-planes 1–16` | fewest fitting | payload bit planes per sample; capacity scales linearly; 3+ visibly degrade, 9+ destroy most cover, 16 = pure payload |
| `--bit-depth 8/10/12/14/16` | 16 | packed `BitsPerSample`; controls plausibility and file size, not capacity per plane |
| `--mode linear\|cfa` | linear | demosaiced RGB (3 samples/px) vs mosaic (1 sample/px, ÷3 capacity) |
| `--raw-frames 1–8` | 1 | full-res raw SubIFDs in one file; capacity ×N, file size ~×N, non-standard for still DNGs |
| `--compression` | none | `none` (widest support) or `adobe_deflate` (lossless, only with 8/16-bit) |
| `--key` | none | passphrase; header + body are XOR-masked with a SHA-256 keystream |
| `--seed` | random | seeds cover pixels, thumbnail choice, and metadata re-rolling |
| `--no-randomize` | off | keep reference metadata as-is instead of re-rolling identifiable fields |
| `--thumbnail` | random | `random` (Commons photo, noise fallback offline), `synthetic` (built-in gradient), or path to an image |
| `--split-file SIZE` | off | split into chunks of at most SIZE per DNG (`500k`, `100m`, `1g`, `2G`, `64KB`, bare bytes) |
| `--split-file-album, --no-split-file-album` | on | group split chunks in `<output-dir>/<input-stem>/` (only with `--split-file`) |
| `--split-file-metadata-id` | ImageUniqueID | metadata field for the shared chunk UUID (`ImageDescription`, or `none` for filenames only) |
| `--split-file-metadata-seq` | ImageNumber | metadata field for the chunk number (`PageNumber`, `ImageDescription`, or `none`); see §3.3 |
| `--split-file-id UUID` | fresh random | override the generated chunk-set UUID (handy for tests) |
| `--progress / --no-progress` | auto (TTY) | force progress bars on / off |

### 3.2 `decode` flags

| flag | default | what it does |
|---|---|---|
| `-i, --input` | (required, repeatable) | one DNG, or several chunk files to concatenate |
| `-o, --output` | (required) | recovered payload path |
| `--key` | none | must match the encode passphrase; wrong key fails on magic/CRC |
| `--lsb-planes 1–16` | auto-detect | try 1–16 planes, accept the one passing magic+CRC; explicit value = strict mode |
| `--max-bytes SIZE` | image capacity | safety cap on the declared payload per file (`1g`, `500m`, `64KB`, bare count); pass an explicit cap for untrusted files |
| `--split-file-metadata-id` | ImageUniqueID | chunk-UUID field; must match the encode setting |
| `--split-file-metadata-seq` | ImageNumber | chunk-sequence field; must match the encode setting |
| `--progress / --no-progress` | auto (TTY) | force progress bars on / off |

`capacity` takes `--width/--height/--mode/--lsb-planes/--raw-frames` and
prints sample count + KB capacity. `gen-tiff` takes `-o/--width/--height/
--seed` and writes a plain TIFF cover (no payload).

### 3.3 Split bookkeeping fields

| flag | default | alternatives | `none` |
|---|---|---|---|
| `--split-file-metadata-id` | `ImageUniqueID` (EXIF 42016: genuine per-image UUID field) | `ImageDescription` | shared set UUID unwritten |
| `--split-file-metadata-seq` | `ImageNumber` (TIFF/EP 0x9211: image-sequence tag, but no total) | `PageNumber` (sequence+total, fails closed), `ImageDescription` (`0003/0012` text) | sequence unwritten |

Fail-open warning: `ImageNumber` stores a scalar with **no total**, so
decoding a consecutive-from-0001 subset (e.g. chunks 1–2 of 3) succeeds
and silently returns truncated data. Use `PageNumber` when a missing tail
must fail closed. `--split-file-id` overrides the generated UUID.

### 3.4 Full `--help` output

Regenerated with `COLUMNS=80`; if these blocks ever disagree with
`python stego_dng.py <cmd> --help`, trust the live CLI — the tables in
§3.1/§3.2 are the human-readable summary.

```text
usage: stego_dng.py encode [-h] --input INPUT [--output OUTPUT]
                           [--width WIDTH] [--height HEIGHT] [--seed SEED]
                           [--key KEY]
                           [--lsb-planes {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}]
                           [--bit-depth {8,10,12,14,16}] [--mode {linear,cfa}]
                           [--compression {none,adobe_deflate}]
                           [--thumbnail THUMBNAIL] [--split-file SIZE]
                           [--split-file-metadata-id {ImageDescription,ImageUniqueID,none}]
                           [--split-file-metadata-seq {ImageDescription,ImageNumber,PageNumber,none}]
                           [--split-file-id UUID]
                           [--split-file-album | --no-split-file-album]
                           [--no-randomize] [--gfx-native] [--pixelshift]
                           [--raw-frames {1,2,3,4,5,6,7,8}] [--auto-size]
                           [--progress] [--no-progress]

options:
  -h, --help            show this help message and exit
  --input, -i INPUT
  --output, -o OUTPUT   output DNG path (default: <input>.dng; with --split-
                        file the 0001-style sequence numbers are inserted
                        before the .dng extension; with --split-file-album (on
                        by default) chunks go in <output-dir>/<input-stem>/,
                        e.g. -o vol.dng + -i huge.raw -> huge/vol0001.dng ...)
  --width WIDTH         raw image width (default: auto from input size)
  --height HEIGHT       raw image height (default: auto from input size)
  --seed SEED
  --key KEY             passphrase for payload encryption
  --lsb-planes {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
                        LSB planes used (default: fewest fitting the input;
                        capacity scales linearly; 3+ degrade the cover, 9+
                        destroy most of it, 16 = samples are pure payload)
  --bit-depth {8,10,12,14,16}
                        packed BitsPerSample of the raw SubIFD (default: 16)
  --mode {linear,cfa}   raw layout (default: linear)
  --compression {none,adobe_deflate}
                        raw SubIFD compression (none = widest viewer support;
                        adobe_deflate only with bit_depth 8/16)
  --thumbnail THUMBNAIL
                        preview picture: 'random' (Wikimedia Commons photo,
                        noise fallback offline), 'synthetic' (built-in
                        gradient), or a path to an image file
  --split-file SIZE     split the payload into chunks of at most SIZE per DNG
                        (e.g. 1g, 100m, 500k, 2G, 64KB, or bytes); files are
                        named <stem>0001<suffix> ... (DCF-style 4-digit
                        sequence)
  --split-file-metadata-id {ImageDescription,ImageUniqueID,none}
                        metadata field for the UUID shared by all chunks of
                        one split (default ImageUniqueID: a genuine EXIF UUID
                        field; ImageDescription also available; 'none' writes
                        nothing and relies on filenames)
  --split-file-metadata-seq {ImageDescription,ImageNumber,PageNumber,none}
                        metadata field for the chunk sequence number (default
                        ImageNumber: TIFF/EP's image-sequence tag, but it
                        carries no total so a consecutive subset decodes
                        without error; PageNumber stores sequence+total
                        natively and fails closed, ImageDescription stores
                        'NNNN/MMMM' text; 'none' writes nothing and relies on
                        filenames)
  --split-file-id UUID  override the generated chunk-set UUID (default: fresh
                        random per split)
  --split-file-album, --no-split-file-album
                        group split chunks in a directory named after the
                        input file without its extension (default: on; only
                        with --split-file; use --no-split-file-album to write
                        chunks beside the output path)
  --no-randomize
  --gfx-native          use 11648x8736
  --pixelshift          use 23296x17472 (needs lots of RAM)
  --raw-frames {1,2,3,4,5,6,7,8}
                        full-resolution raw SubIFDs sharing one file
                        (burst/stack style, 1-8); capacity scales with frames
                        but so does file size, and multiple raw frames are
                        non-standard for still DNGs)
  --auto-size           compute the smallest 4:3 width/height fitting the
                        input (smaller files, but non-standard dimensions may
                        look unusual under inspection; cannot be combined with
                        --width/--height/--gfx-native/--pixelshift)
  --progress            force progress bars on (by default they show on a TTY
                        and stay quiet when output is piped)
  --no-progress         disable progress bars
```

```text
usage: stego_dng.py decode [-h] --input INPUT [INPUT ...] --output OUTPUT
                           [--key KEY]
                           [--lsb-planes {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}]
                           [--max-bytes SIZE]
                           [--split-file-metadata-id {ImageDescription,ImageUniqueID,none}]
                           [--split-file-metadata-seq {ImageDescription,ImageNumber,PageNumber,none}]
                           [--progress] [--no-progress]

options:
  -h, --help            show this help message and exit
  --input, -i INPUT [INPUT ...]
                        one DNG, or several chunk files to concatenate
                        (verified via split metadata, else 0001-style names)
  --output, -o OUTPUT
  --key KEY
  --lsb-planes {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
                        LSB planes used at encode time (default: auto-detect)
  --max-bytes SIZE      safety cap on the accepted declared payload per file
                        (e.g. 1g, 500m, 64KB, or bare count; default: image
                        capacity, so any file this tool can encode also
                        decodes; pass an explicit cap for untrusted files)
  --split-file-metadata-id {ImageDescription,ImageUniqueID,none}
                        metadata field holding the shared chunk-set UUID (must
                        match the encode setting)
  --split-file-metadata-seq {ImageDescription,ImageNumber,PageNumber,none}
                        metadata field holding the chunk sequence (must match
                        the encode setting)
  --progress            force progress bars on (by default they show on a TTY
                        and stay quiet when output is piped)
  --no-progress         disable progress bars
```

## 4. How it works

- **Container.** `tifffile.TiffWriter` writes IFD0 (tiled Baseline-JPEG
  thumbnail, YCbCr, 128×96 tiling like the combiner) plus the raw
  SubIFD(s). Post-write patching flips SubIFD
  `PhotometricInterpretation` 2 → 34892 (LinearRaw; tifffile can only
  *write* that geometry as RGB), appends an EXIF SubIFD at EOF, and links
  it via tag 34665 (tifffile filters IFD-pointer tags, so a same-size
  dummy private tag is repurposed — no byte shifting). CFA mode
  additionally writes `CFAPlaneColor`/`CFALayout`, which LibRaw requires.
  All offset handling is BigTIFF-aware.
- **Cover.** The raw starts as a synthetic gradient + noise field,
  rescaled per bit depth so exposure stays constant, quantized to packed
  steps so files round-trip exactly. `LsbCodec` embeds in place
  (the cover array is consumed — do not reuse it afterwards).
- **Codec and framing.** Payload → 18-byte header + body → LSB planes of
  every sample, striped bit-wise across frames in write order. `decode`
  concatenates frame bitstreams and accepts the first plane count passing
  magic + CRC. Capacity comes only from samples × planes × frames;
  bit depth changes file size and plausibility, not bytes per plane.
- **Lossless only.** The raw defaults to uncompressed: the LibRaw in this
  environment fails on Adobe-Deflate DNG, and any lossy codec would
  destroy LSBs by design. `--compression adobe_deflate` is an opt-in
  (still lossless, tifffile-decodable). Packed depths (10/12/14) cannot
  combine with compression (tifffile limitation), so they always write
  uncompressed.
- **Thumbnails.** The IFD0 JPEG is what desktops actually show (see §6).
  Sources: `random` (Commons photo, center-cropped and Lanczos-resized,
  3 attempts then noise fallback so offline encodes keep working),
  `synthetic` (built-in gradient), or a file path. RGB is converted to
  YCbCr before writing — tifffile stores JPEG planes verbatim, so writing
  RGB directly swaps chroma.
- **Sizing.** `AutoSizer.recommend()` walks presets smallest-first and
  picks the fewest planes that fit; `--auto-size` instead solves for the
  smallest even 4:3 frame. `frames` is never auto-bumped, only validated.
  `--lsb-planes` may not exceed `--bit-depth` (values would overflow the
  declared `WhiteLevel`).
- **Split sets.** One input → N independent framed chunks, 4-digit
  DCF-style names (`vol0001.dng` …), shared UUID + per-file sequence in
  the configured metadata fields (or filenames only with `none`/`none`).
- **Keystream.** Optional `--key` XOR-masks header and body with a
  SHA-256 counter stream. It hides contents from casual LSB inspection;
  it is not authenticated encryption. A wrong key fails closed on
  magic/CRC.
- **Verification.** `tiffdump` layout ≈ reference, `exiv2 -pa` shows the
  full Maker/EXIF/DNG/XMP set, `rawpy.imread` + postprocess succeeds for
  `linear` and `cfa` at every depth/plane/frame combination, and
  `decode(encode(x)) == x` across the matrix (see `tests/test_stego.py`).
- **Dependencies.** `numpy`, `pillow`, `tifffile[all]`, `tqdm`
  (`requirements.txt`); `rawpy` is optional, decode checks only.
  Test-only deps (`pytest`, `pytest-cov`) live in `requirements-dev.txt`.
- **Byte stability.** `DngStego.encode()` output is byte-stable for fixed
  inputs (modulo offset tags 273/279/324/325/330/34665, which legitimately
  shift with JPEG size).

## 5. Limitations / out of scope

- **No real sensor data.** The cover is synthetic gradient + noise.
  Judging photographic content is out of scope — but anyone opening the
  raw in a viewer sees a test pattern, not a photograph. High plane
  counts make that worse (see detection table below).
- **Thin metadata story.** `DNGPrivateData` is a small placeholder, not
  the 80–120 MB embedded RAF of real combiner files; MakerNote is
  omitted; no GPS tags are written (samples have none). An inspector
  comparing priv-data size against a real combiner DNG notices instantly.
- **Huge files, huge RAM.** `--pixelshift` writes a ~2.5 GB uncompressed
  file. Peak encode RAM is ~2x payload plus one cover buffer (~4.3 GB for
  a 1 GB payload); covers embed in place and `--split-file` streams one
  chunk at a time, so splitting keeps peak near a single chunk's cost.
  Only `--gfx-native` (489 MB file, 20 MB payload) was tested end-to-end
  at scale; pixelshift-scale RAM figures are analytical.
- **Weak encryption.** The `--key` XOR keystream gives confidentiality
  against casual inspection, not authenticated encryption. Use real
  encryption (e.g. age/gpg) before embedding if the payload needs it;
  wrong keys still fail closed via magic/CRC.
- **Lossy pipelines destroy payloads.** Any JPEG recompression, resize,
  or RAW-editor export of the raw wipes LSBs. Only lossless handling
  preserves data; `adobe_deflate` is safe, lossy JPEG is not.
- **Tooling gaps.** `exiv2` cannot parse BigTIFF at all (files past ~4 GB,
  e.g. pixelshift ×2+ frames); use `tifffile`/`rawpy` there. LibRaw
  rejects Deflate DNGs in this environment and rejects >16-bit integer
  DNGs outright — hence no 24/32-bit integer option and the uncompressed
  default. Packed depth + deflate is rejected (tifffile limitation).
- **Forensic visibility.** LSB data is invisible at a glance but not to
  analysis. Every risky option prints a CLI `warning:` at encode time:

| option | what an inspector sees |
|---|---|
| `--lsb-planes 1–2` | near-invisible; normal bit-plane statistics |
| `--lsb-planes 3–4` | cover degraded; low-bit entropy elevated |
| `--lsb-planes 5–8` | heavily degraded cover; skewed bit-plane statistics |
| `--lsb-planes 9–15` | raw renders as degraded noise; flat histogram |
| `--lsb-planes 16` | **no cover at all** — pure payload; trivially exposed by any entropy check (use `--key` so contents stay opaque) |
| `--raw-frames 2–8` | N full-res SubIFDs in `tiffdump`; ~N× file size; no still-DNG camera output looks like this |
| `--bit-depth 8/10/12` | `BitsPerSample` below every GFX 100 II option (14/16) |
| `--auto-size` | dimensions match no camera preset (e.g. 462×348) |
| split shared UUID | links the chunk set (its purpose); `none`/`none` leaves only filenames |

- **Out of scope by design:** video/animation timelines (still DNG has
  none — CinemaDNG is a file sequence), hidden extra-IFD blobs as a
  primary channel (listed by any TIFF tool), single-metadata-tag dumps
  (detectable, size-limited), 32-bit float HDR mantissa hiding, and DNG
  1.7 JPEG XL (lossy modes kill LSBs).

## 6. Background details

Condensed notes on *why* the defaults look the way they do.
Everything above is sufficient to use the tool; this section is for
inspectors and the curious.

- **DNG in one paragraph.** DNG (ISO 12234-4) is a TIFF/EP profile:
  classic TIFF container (`II*\0`, IFD tag directory) plus mandated
  metadata (`DNGVersion`, `ColorMatrix`, `BlackLevel`, …) and EXIF/XMP
  sub-IFDs. TIFF/EP defines `SubIFDs` (330), CFA tags (33421/33422,
  50710/50711), and compression 7 (JPEG) / 8 (Deflate, since DNG 1.4).
- **Reference samples (`images/`, read-only).** GFX RAFs (~70–199 MB,
  `FUJIFILMCCD-RAW` + embedded preview) and Pixel Shift Combiner DNGs
  (1.0–1.6 GB) were inspected with `tiffdump`, `exiv2 -pa`, `tifffile`.
  Every combiner DNG shares one skeleton: IFD0 4000×3000 YCbCr JPEG
  preview + 23296×17472 16-bit × 3ch LinearRaw SubIFD (tiled 128×96,
  lossless JPEG) + EXIF with exposure/focus/Fuji MakerNote + 81–121 MB
  `DNGPrivateData` that embeds the source RAF. The tool mimics the
  skeleton, not the RAF embedding.
- **Why LinearRaw LSB.** Still DNG has no animation timeline, so
  "frames" only offer layout options; an extra hidden IFD is listed by
  any TIFF tool, and single-tag blobs are size-limited and obvious.
  The 16-bit raw headroom is the channel that survives casual viewing.
- **Density knobs considered, not all kept.** Resolution, bit depth,
  channel count, and frame count all scale capacity; lossless Deflate
  does not (measured ~16% on a 2-plane test — random/encrypted bits are
  incompressible), so it stays opt-in. Past ~4 GB the writer switches to
  BigTIFF (DNG 1.6). Deliberately excluded: DNG 1.4 32-bit float HDR
  (mantissa-only hiding = fewer bits per byte), 24/32-bit integer
  (LibRaw rejects it), JPEG XL lossy (destroys LSBs).
- **What viewers show.** Windows Explorer (WIC/Raw Extension codec) and
  Nautilus (`gnome-raw-thumbnailer` and friends) render the embedded
  IFD0 JPEG preview, never the raw mosaic — which is why the thumbnail
  picture matters more than the cover for casual inspection. Viewers
  downscale to 128–512 px regardless, but we keep combiner parity (up to
  4000×3000, same aspect as the raw).
- **Metadata: static vs re-rolled.** Calibration fields are copied
  verbatim (`ColorMatrix1/2`, `CalibrationIlluminant 17/21`,
  `AnalogBalance`, 256-byte `OpcodeList3`, `Make`/`Model`/`Software`, XMP
  skeleton). Every `encode` re-rolls the identifiable fields (seeded by
  `--seed`): `DateTime` (+`DateTimeOriginal/Digitized`, `OffsetTime*`,
  `SubSecTime*`), `ExposureTime`/`ShutterSpeedValue`,
  `FNumber`/`ApertureValue`, `ExposureProgram`, `ISOSpeedRatings`,
  `MeteringMode`, `FocalLength` (+ 35 mm equiv, consistent GF lens pick
  from 8 real lenses), `MaxApertureValue`, `BrightnessValue`,
  `ExposureBiasValue`, `CameraSerialNumber`, `BodySerialNumber`,
  `LensSerialNumber`, `AsShotNeutral`, `BaselineExposure`, plus fresh
  cover and thumbnail pixels. `ImageNumber` is *not* randomized — on
  split chunks it carries the deterministic sequence; plain files omit it.

## 7. Development tasks and PyPI releases

Task runner is [`just`](https://github.com/casey/just) (see `justfile`;
run `just --list`). Dev dependencies first:

```bash
python -m venv .venv
.venv/bin/pip install -r requirements-dev.txt   # pytest, ruff, build, twine, ...
```

| command | what it does |
|---|---|
| `just test` | `pytest tests/ -q` (extra args forwarded, e.g. `just test -k roundtrip`) |
| `just lint` | `ruff check` on the shipped code (`stegodng/`, `stego_dng.py`) |
| `just build` | sdist + wheel into `dist/`, then `twine check` |
| `just publish-test` | rebuild and upload to [TestPyPI](https://test.pypi.org/project/stegodng/) |
| `just publish` | rebuild and upload to [PyPI](https://pypi.org/project/stegodng/) |
| `just clean` | remove `dist/`, `build/`, `*.egg-info/` |

`pip install stegodng` also installs two console commands, `stegodng`
and `stego-dng`, which accept the same `encode`/`decode`/`capacity`/
`gen-tiff` subcommands as `python stego_dng.py`.

Release flow:

1. Bump the version in **both** `pyproject.toml` and
   `stegodng/__init__.py` (`__version__`) — PyPI rejects re-uploading a
   version that already exists.
2. Authenticate with an API token: create one at
   test.pypi.org / pypi.org (Account settings → API tokens), then export
   `TWINE_USERNAME=__token__` and `TWINE_PASSWORD=<token>`
   (or add them to `~/.pypirc`, which is git-ignored).
3. `just publish-test`, check the project page, and install the result
   somewhere clean:
   `pip install --index-url https://test.pypi.org/simple/ stegodng`.
4. `just publish` for the real release.
