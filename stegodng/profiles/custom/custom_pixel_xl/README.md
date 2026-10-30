# Google Pixel XL (custom)

Profile slug: `custom_pixel_xl`  
EXIF Make/Model: `Google` / `Pixel XL`  
Native geometry: 4032x3020 `DefaultCropSize` (raw SubIFD is 4048x3036)  
Suggested bit depth: 16-bit container, 14-bit effective `WhiteLevel`  
CFA: BGGR (`CFAPattern` bytes `02 01 01 00`)  
Crop factor: 5.53  
Calibration source: `harvested-adobe-dng`

Derived from four DNGs taken 2026-10-29 on the author's Pixel XL:

- `images/pixel_xl/IMG_20261029_174518.dng`
- `images/pixel_xl/IMG_20261029_183843.dng`
- `images/pixel_xl/IMG_20261029_183853.dng`
- `images/pixel_xl/IMG_20261029_183905.dng`

These carry Adobe's DNG converter signature (`ProfileName: Adobe Standard`,
`ProfileCalibrationSignature: com.adobe`, DNG 1.3 headers), not the native
Google HDR+ DNGs used by the harvested `google_pixel_xl` profile. That is why
the two profiles carry different color matrices and DNG versions.

## Sample metadata

- Software variants: `HDR+ 1.0.281780091zd` (3 files),
  `HDR+ 1.0.281780091nl` (1 file)
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
- BlackLevel: 1009.49-1017.86 per file (four rational values)
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

- Make `Google`, Model `Pixel XL`, UniqueCameraModel `Google Pixel XL`,
  Software `HDR+ 1.0.281780091zd`
- DNGVersion [1, 3, 0, 0], DNGBackwardVersion [1, 3, 0, 0]
- ColorMatrix1/2 and CalibrationIlluminants 17/21 from the harvest
- BaselineNoise/BaselineSharpness/LinearResponseLimit/ShadowScale 1.0
- BlackLevel ref 4075 (16-bit equivalent; observed per-channel range
  ~4042-4075, ref is file 1's first channel); OpcodeList3 empty
  (`00000000`)

## Randomized per file (seeded)

- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: the harvest's odd 1/24, 1/15, 1/13.33 values plus the
  standard reference pool
- FNumber: always F2 (single-entry pool)
- ISO pool: observed 1225/2035/1250/2900 plus the standard reference pool
- Lens: fixed Pixel XL built-in lens (4.7 mm, f/2.0)
- FocalLength 4.7 mm, 35 mm equivalent 26 mm (crop factor 5.53)
- Camera/body/lens serials (generic prefixes, since the samples carry none)
- AsShotNeutral (writer R 0.50-0.76 / B 0.40-0.56), BaselineExposure
  (writer ±0.006 EV), Brightness, ExposureBias
- Metering [2, 3, 5] and ExposureProgram [1, 2, 3, 4]: not observed in the
  samples, but the writer always emits these tags

## Sub-profiles

- `custom_pixel_xl-native`: pins 4032x3020 (the observed `DefaultCropSize`)

## Fidelity: present in the samples, not reproduced yet

The profile records the full harvest, but the current writer does not emit
all of it. An inspector comparing a generated file against these samples
would still see:

- No Adobe profile block (`ForwardMatrix1/2`, `ProfileHueSatMap`,
  `ProfileLookTable`, `ProfileName`, `ProfileCopyright`, `NoiseProfile`)
- No `OpcodeList2`; the writer emits an empty `OpcodeList3` instead
- Uncompressed raw with 128x96 tiles instead of lossless-JPEG 256x256 tiles
- Raw frame 4032x3020 with crop origin 0,0 instead of storage 4048x3036
  with crop origin 8,8 and `ActiveArea`
- `WhiteLevel 65535` instead of 16368 in a 16-bit container
- RGGB instead of BGGR, no `BlackLevelRepeatDim`, no `BayerGreenSplit`
- A preview up to 4000x3000 instead of 676x506
- An XMP packet (the samples have none)
- Lens model/make/spec, camera/body/lens serials, `OffsetTime*`,
  `ExposureProgram`, `MeteringMode` (the samples omit all of these)
- Orientation 1 instead of 6/3
- No `SubjectDistance`/`SubjectDistanceRange`, no GPS
- `BaselineExposure` is re-rolled within ±0.006 EV, while these samples are
  +0.13 to +0.94 EV
- `AsShotNeutral` is re-rolled as R 0.50-0.76 / B 0.40-0.56, wider than the
  observed R 0.582-0.646 / B 0.378-0.433

`OpcodeList2`, the Google MakerNote and the per-file raw digests cannot be a
single static profile blob: they differ in every sample.

## Plausible-deniability notes

This profile deliberately describes Adobe-converted Pixel XL DNGs. Compared
with other Adobe-converted Pixel XL files it should look consistent; compared
with a native Google HDR+ DNG it will show the Adobe Standard block and DNG
1.3 headers. More samples will be added as they are collected.
