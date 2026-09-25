# Canon EOS 90D
Profile slug: `canon_eos_90d`  
EXIF Make/Model: `Canon` / `Canon EOS 90D`
Native geometry: 6984x4660 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.6  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS 90D 2/3548374885.cr3`
Files seen: 8 (Canon EOS 90D 2/3548374885.cr3, Canon EOS 90D 2/6976696302.cr3, Canon EOS 90D 3/1371984997.cr3, Canon EOS 90D 3/9739627897.cr3, ...)
Software strings observed: none
Lenses observed: 85mm F1.4 DG HSM | Art 016; EF-S18-135mm f/3.5-5.6 IS USM; EF-S35mm f/2.8 MACRO IS STM; EF70-200mm f/2.8L IS III USM
ISO observed: 100, 160, 200, 500, 640
Exposure observed: 1/1600 s, 1/200 s, 1/50 s, 1/500 s, 1/60 s
F-number observed: F11, F14, F18, F3.2, F4, F5, F6.3
Focal length observed: 113.0 mm, 135.0 mm, 27.0 mm, 35.0 mm, 67.0 mm, 70.0 mm, 85.0 mm, 90.0 mm
EXIF PixelDimensions observed: 6960 x 4640
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 90D`, UniqueCameraModel `Canon EOS 90D`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [10, 8000], [1, 500], [10, 4000], [1, 200], [10, 2000], [10, 1000], [1, 60], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1400, 100], [1600, 100], [1800, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): 85mm F1.4 DG HSM | Art 016; EF-S18-135mm f/3.5-5.6 IS USM; EF-S35mm f/2.8 MACRO IS STM; EF70-200mm f/2.8L IS III USM
- FocalLength + 35mm equivalent (x1.6), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_90d-native`: pins 6984x4660 (native sensor geometry)

Base `--camera-profile=canon_eos_90d` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
