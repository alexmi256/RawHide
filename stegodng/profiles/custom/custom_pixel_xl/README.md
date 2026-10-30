# Google Pixel XL (custom)

Profile slug: `custom_pixel_xl`  
EXIF Make/Model: `Google` / `Pixel XL`  
Native geometry: 4032x3020 `DefaultCropSize` (raw SubIFD is 4048x3036)  
Suggested bit depth: 16-bit container, 14-bit effective `WhiteLevel`  
CFA: BGGR (`CFAPattern` bytes `02 01 01 00`)  
Crop factor: 5.53  
Calibration source: `harvested-adobe-dng`

Derived from six DNGs taken 2026-10-29/30 on the author's Pixel XL:

- `images/pixel_xl/IMG_20261029_174518.dng`
- `images/pixel_xl/IMG_20261029_183843.dng`
- `images/pixel_xl/IMG_20261029_183853.dng`
- `images/pixel_xl/IMG_20261029_183905.dng`
- `images/pixel_xl/IMG_20261030_094221.dng`
- `images/pixel_xl/IMG_20261030_094256.dng`

These carry Adobe's DNG converter signature (`ProfileName: Adobe Standard`,
`ProfileCalibrationSignature: com.adobe`, DNG 1.3 headers), not the native
Google HDR+ DNGs used by the harvested `google_pixel_xl` profile. That is why
the two profiles carry different color matrices and DNG versions.

## Sample metadata

The 2026-10-30 additions contribute ISO 50, Software `nd`, GPS, and
BlackLevel `1020/1016/1016/1020`; they are currently used for the GainMap
base, while the rest of this section is the original four-file harvest.

- Software variants: `HDR+ 1.0.281780091zd` (4 files),
  `HDR+ 1.0.281780091nl` (1 file), `HDR+ 1.0.281780091nd` (1 file)
- Lenses observed: none. The writer synthesizes the fixed
  `Pixel XL built-in lens` (4.7 mm, f/2.0)
- ISO observed: 1225, 2035, 1250, 2900
- Exposure observed: 1/24 s, 1/15 s, 1/13.33 s
- F-number observed: F2 (all files)
- Focal length observed: 4.7 mm, 26 mm equivalent
- Orientation observed: 6, 6, 3, 6
- Serial tags present: none
- GPS present: 1 of 4 files
- AsShotNeutral observed: R 0.5823-0.6457, G 1.0, B 0.3780-0.4326
- BaselineExposure observed: +0.13 to +0.94 EV

## Harvested DNG calibration

- IFD0 Make: "Google"
- IFD0 Model: "Pixel XL"
- IFD0 UniqueCameraModel: "Google Pixel XL"
- IFD0 DNGVersion: `01030000`
- IFD0 DNGBackwardVersion: `01030000`
- IFD0 ColorMatrix1: `9863/-4630/39, -3233/11159/2374, -296/1214/6046` (/10000)
- IFD0 ColorMatrix2: `9293/-3484/-871, -2482/10928/1776, -256/1479/5145` (/10000)
- IFD0 ForwardMatrix1: `4471/3936/1236, 2233/7402/365, 1246/5/7000` (/10000)
- IFD0 ForwardMatrix2: `4110/3917/1617, 1843/7670/487, 848/16/7387` (/10000)
- IFD0 CalibrationIlluminant1: 17 (Standard light A)
- IFD0 CalibrationIlluminant2: 21 (D65)
- IFD0 AnalogBalance: 1, 1, 1
- IFD0 BaselineNoise: 1.0
- IFD0 BaselineSharpness: 1.0
- IFD0 LinearResponseLimit: 1.0
- IFD0 ShadowScale: 1.0
- IFD0 ProfileName: "Adobe Standard"
- IFD0 ProfileHueSatMapDims: 90 x 30 x 1 (data present)
- IFD0 ProfileLookTableDims: 36 x 8 x 16 (data present)
- IFD0 ProfileCopyright: "Copyright 2016 Adobe Systems, Inc."
- IFD0 NoiseProfile: per-file
- IFD0 preview: 676x506 JPEG (YCbCr)
- No XMP packet

Raw SubIFD:

- BitsPerSample: 16
- SamplesPerPixel: 1
- PhotometricInterpretation: 32803 (CFA)
- Compression: 7 (lossless JPEG)
- TileWidth x TileLength: 256 x 256
- CFARepeatPatternDim: 2 x 2
- CFAPattern: `02 01 01 00` (BGGR)
- CFAPlaneColor: `00 01 02`
- BlackLevelRepeatDim: 2 x 2
- BlackLevel: four rationals, 1009.49-1020 per channel per file
- WhiteLevel: 16368
- DefaultCropOrigin: 8, 8
- DefaultCropSize: 4032, 3020
- ActiveArea: 0, 0, 3036, 4048
- BayerGreenSplit: 500
- AntiAliasStrength: 1.0
- BestQualityScale: 1.0
- DefaultUserCrop: 0, 0, 1, 1
- OpcodeList2: ~19572 bytes, content differs per file
- No OpcodeList3

## Static fields (stamped by the current writer)

- Make `Google`, Model `Pixel XL`, UniqueCameraModel `Google Pixel XL`;
  Software is one of the observed variants
- DNGVersion [1, 3, 0, 0], DNGBackwardVersion [1, 3, 0, 0]
- ColorMatrix1/2 and CalibrationIlluminants 17/21 from the harvest
- ForwardMatrix1/2, `Adobe Standard`, `com.adobe`, the Adobe
  copyright/embed-policy tags, `ProfileHueSatMapData1/2` (90x30x1) and
  `ProfileLookTableData` (36x8x16) from the harvest, plus a per-file
  `NoiseProfile`
- BaselineNoise/BaselineSharpness/LinearResponseLimit/ShadowScale 1.0
- BlackLevel per channel `1020/1016/1016/1020` with
  `BlackLevelRepeatDim 2x2` (scaled to the 16-bit range under the default
  capacity policy)
- Default capacity policy: WhiteLevel 65535 and up to 16 planes.
  `--level-policy strict` switches to WhiteLevel 16368 and a safe
  13-plane cap so no sample exceeds it (other profiles keep their own
  policy, or 16 planes when they have no fidelity block)
- `--auto-size` tries native 4048x3036 with 16 planes first and only
  grows the frame after that configuration is exhausted; the same
  descending plane search applies when the native subprofile pins the
  geometry
- OpcodeList2 is generated per file (four GainMaps, see below), so no
  OpcodeList3 is written
- Preview 676x506, `CFAPattern` BYTE BGGR, `BayerGreenSplit` 500,
  `ActiveArea` and an 8 px crop margin around `4032x3020`, 256x256 tiles

## GainMap / OpcodeList2

`profile.json` carries a compact `"gainmap"` block: a 4 x 8 x 10 base
grid (one grid per CFA phase, averaged from the six samples' 30 x 40
maps), plus `jitter` and `clip`. CFA encodes interpolate the base to
30 x 40, add a seeded low-frequency jitter, and write four `GainMap`
opcodes (ID 9) in `OpcodeList2` (tag 51009) with phases
`1,1 / 1,0 / 0,1 / 0,0`, 2x2 pitch, and one map plane. The blob is
19,572 bytes, matching the samples; no `OpcodeList3` is written.

Edit `jitter` to change file-to-file variation, or remove the block
(`"gainmap": null`) to fall back to the GFX-style empty `OpcodeList3`.
The generator is `stegodng.opcodes.build_opcode_list2`; the parser and
validator are `parse_opcode_list2` / `validate_opcode_list2`.

## Randomized per file (seeded)

- DateTime* and SubSecTime* inside the last 365 days; Orientation 6 or 3
- Software `…zd`, `…nl` or `…nd`
- ExposureTime: the five observed exact rationals (≈1/160–1/13.3 s)
- FNumber: always F2 (single-entry pool)
- ISO: 50–2900, including the observed 1225/1250/2035/2900 values
- Lens: fixed Pixel XL built-in lens (4.7 mm, f/2.0); focal length 4.7 mm,
  35 mm equivalent 26 mm (crop factor 5.53)
- AsShotNeutral R 0.4453–0.6460 / B 0.3780–0.6410; BaselineExposure
  +0.13…+0.94 EV; ExposureBias 0; Flash “No, compulsory”
- SubjectDistance/SubjectDistanceRange chosen as a consistent pair
- GPS: seeded plausible coordinates, altitude, DOP, timestamp and date
- No OffsetTime*, no MeteringMode/ExposureProgram, no camera/body/lens
  serials, no lens tags, no XMP packet
- The CLI defaults this profile to `--mode cfa` via
  `fidelity.suggested_mode`; pass `--mode linear` to override. The Python
  API still defaults to `linear` unless the caller passes `mode="cfa"`.

## Sub-profiles

- `custom_pixel_xl-native`: pins raw storage 4048x3036; the writer trims
  8 px per side to the observed `DefaultCropSize` 4032x3020

## Fidelity status

Reproduced by the current writer:

- Make/Model/UniqueCameraModel, DNG 1.3 headers, ColorMatrix1/2,
  CalibrationIlluminants, and the full Adobe profile block
  (`ForwardMatrix1/2`, `ProfileName`, signature, copyright, embed policy,
  `ProfileHueSatMapData1/2`, `ProfileLookTableData`, `NoiseProfile`)
- 4048x3036 raw storage, 8 px crop margin to 4032x3020, `ActiveArea`,
  `DefaultUserCrop`, 256x256 tiles, BGGR `CFAPattern` (BYTE),
  `BayerGreenSplit`, per-channel BlackLevel; default capacity WhiteLevel
  65535 / 16 planes, strict WhiteLevel 16368 / 13 planes
- 676x506 preview, Orientation 6/3, software variant, last-365-days dates,
  AsShotNeutral/BaselineExposure ranges, SubjectDistance/Range, GPS
- No XMP, lens tags, serials, `OffsetTime*`, `ExposureProgram`, or
  `MeteringMode`, matching the samples
- Generated `OpcodeList2` (four GainMaps) from the compact base grid

Still different:

- Raw compression is uncompressed, not lossless-JPEG (Compression 7)
- The Google MakerNote and the raw digests are not emitted
- The preview is a thumbnail source, not a development of the raw scene
- The raw pixels are a synthetic cover, not a real Pixel XL scene
- `OpcodeList2` is generated, not copied byte-for-byte; its structure and
  gain range match, but the four 30 x 40 tables differ from any sample
- `NewRawImageDigest`/`RawDataUniqueID` are absent
- The default capacity policy claims WhiteLevel 65535 / 16-bit data,
  unlike the real 14-bit files; use `--level-policy strict` for 16368
  and at most 13 planes

The Google MakerNote and the per-file raw digests cannot be a single
static profile blob because they differ in every sample. `OpcodeList2` is
the exception: its header is static and only the gain tables vary, so a
base grid plus per-file jitter reproduces it.

## Plausible-deniability notes

This profile deliberately describes Adobe-converted Pixel XL DNGs. Compared
with other Adobe-converted Pixel XL files it should look consistent; compared
with a native Google HDR+ DNG it will show the Adobe Standard block and DNG
1.3 headers. More samples will be added as they are collected.
