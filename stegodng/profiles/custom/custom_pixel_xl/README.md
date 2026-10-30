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
- `NewRawImageDigest` + `RawDataUniqueID`, the `HDRP` MakerNote with
  `MakerNoteSafety 1`, and the Adobe tag set (see below)
- Preview 676x506, `CFAPattern` BYTE BGGR, `BayerGreenSplit` 500,
  `ActiveArea` and an 8 px crop margin around `4032x3020`, 256x256 tiles

The IFD0 inventory is now exactly the sample set: `254 256 257 258 259
262 271 272 273 274 277 278 279 284 305 306 330 529 530 531 532 34665
34853 50706 50707 50708 50721 50722 50727 50728 50730 50731 50732 50734
50739 50741 50778 50779 50781 50932 50936 50937 50938 50939 50941 50942
50964 50965 50981 50982 51041 51111`, and the raw SubIFD matches too.

## Adobe tag conventions (`fidelity.tag_conventions: "adobe"`)

The TIFF writer used below tifffile's defaults, which differ from what
Adobe software emits.  The profile now switches them off or on:

- `XResolution` (282), `YResolution` (283) and `ResolutionUnit` (296) are
  removed from IFD0 and the raw SubIFD after writing (the reference
  files carry none of them)
- `YCbCrCoefficients` (529, 299/1000 587/1000 114/1000) and
  `YCbCrPositioning` (531, centered) are added to the preview IFD
- the raw SubIFD gains `PlanarConfiguration` (284, chunky), which
  tifffile only writes for multi-sample pages
- `CFAPlaneColor` (50710) is written as BYTE, like the samples
- `SubIFDs` (330) is retyped from TIFF IFD (13) to LONG (4)
- `RowsPerStrip` (278) is the full preview height (`506`), not the TIFF
  writer's MCU-rounded 512
- `SubSecTime*` carry the full six-digit EXIF fraction (`153489`), not
  the two-digit legacy value
- `AnalogBalance` (1000000/1000000), `AsShotNeutral` (/1000000),
  `BaselineExposure` (hundredths of a stop) and `ShadowScale` (1/1) use
  Adobe's denominators instead of the writer's 1e4/100 defaults

The entry block is compacted in place (`DngContainer.drop_ifd_tags` /
`rewrite_ifd_entries`), so no offsets move and the raw tiles are
untouched.

## Raw image digests (`fidelity.raw_digests: true`)

Both tags reproduce the sample values byte-for-byte (verified with
`tools/digests.py verify` against all six files):

- `NewRawImageDigest` (51111) is the DNG SDK "fast" digest: MD5 over the
  concatenated MD5s of 256x256 tiles (row-major, edge tiles truncated,
  little-endian 16-bit samples).  It is *not* MD5 of the whole raster.
- `RawDataUniqueID` (50781) follows `dng_negative::FindRawDataUniqueID`:
  MD5 over the new digest, `UniqueCameraModel` (`Google Pixel XL`, not
  the IFD0 Model), `DefaultCropSize`/`DefaultCropOrigin`/`DefaultUserCrop`
  rationals, and `FingerprintToStream` of OpcodeList2 (header fields plus
  the gain table, host/little-endian).  The gain-map fingerprint is what
  the SDK re-serializes, not the raw tag bytes.

Both values are computed from the finished raw frame, so they stay valid
after LSB embedding.  Multi-frame encodes (`--raw-frames 2+`) omit them:
one digest describes one raw image.

## MakerNote (`fidelity.makernote`)

Every sample carries `Exif.Photo.MakerNote` (2640-2757 bytes) starting
with `HDRP` + `02 ef` + nine constant bytes.  The tail is per-file
high-entropy data (7.94 bits/byte, all 256 byte values, no strings, and
two files XOR to noise), i.e. Google's HDR+ processing metadata; it is
not derivable from anything else in the file and no public parser decodes
it.

The writer therefore reproduces the envelope only: the constant 15-byte
prefix (`48 44 52 50 02 ef 64 35 6d 5e 70 1e 2c ea e3`) followed by
seeded pseudo-random bytes, at a length drawn from 2640-2757 bytes.  The
same seed reproduces the same blob; different seeds differ in length and
content.  `MakerNoteSafety` (50741, "Safe") marks it copyable, as in the
samples.  The profile must also list `37500` in
`fidelity.tags.exif_allow`, otherwise the EXIF builder filters it out.

What an inspector would see: a correctly sized, correctly prefixed
MakerNote on every file.  What they would not see: a decodable HDR+
payload.  An ExifTool dump only shows the opaque blob, but a byte-level
comparison with a genuine Pixel file would expose the difference.

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
- MakerNote length (2640-2757) and payload bytes
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
- The complete IFD0/SubIFD tag inventory of the samples (no
  X/YResolution, no ResolutionUnit, Adobe's YCbCr pair, SubIFD
  `PlanarConfiguration`, BYTE `CFAPlaneColor`, LONG `SubIFDs`)
- `NewRawImageDigest` and `RawDataUniqueID` identical to the values a
  DNG SDK-based writer produces for the same pixels and metadata
- `HDRP` MakerNote at a realistic length plus `MakerNoteSafety`, and
  six-digit `SubSecTime*`
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
- The MakerNote payload is an opaque pseudo-random blob, not a real
  HDR+ record (prefix, length and entropy match; content does not)
- The preview is a thumbnail source, not a development of the raw scene
- The raw pixels are a synthetic cover, not a real Pixel XL scene
- `OpcodeList2` is generated, not copied byte-for-byte; its structure and
  gain range match, but the four 30 x 40 tables differ from any sample
- The default capacity policy claims WhiteLevel 65535 / 16-bit data,
  unlike the real 14-bit files; use `--level-policy strict` for 16368
  and at most 13 planes

The MakerNote cannot be a static profile blob because it differs in
every sample; the writer reproduces its envelope instead (see above).
`OpcodeList2` is the exception: its header is static and only the gain
tables vary, so a base grid plus per-file jitter reproduces it.

## Plausible-deniability notes

This profile deliberately describes Adobe-converted Pixel XL DNGs. Compared
with other Adobe-converted Pixel XL files it should look consistent; compared
with a native Google HDR+ DNG it will show the Adobe Standard block and DNG
1.3 headers. More samples will be added as they are collected.
