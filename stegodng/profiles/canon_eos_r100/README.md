# Canon EOS R100
Profile slug: `canon_eos_r100`  
EXIF Make/Model: `Canon` / `Canon EOS R100`
Native geometry: 6024x4020 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS R100/2975843588.cr3`
Files seen: 2 (Canon EOS R100/2975843588.cr3, Canon EOS R100/7052035421.cr3)
Software strings observed: none
Lenses observed: RF-S18-150mm F3.5-6.3 IS STM; RF-S18-45mm F4.5-6.3 IS STM
ISO observed: 100, 1250
Exposure observed: 1/100 s, 1/125 s
F-number observed: F5, F7.1
Focal length observed: 24.0 mm, 39.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R100`, UniqueCameraModel `Canon EOS R100`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 125], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): RF-S18-150mm F3.5-6.3 IS STM; RF-S18-45mm F4.5-6.3 IS STM
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r100-native`: pins 6024x4020 (native sensor geometry)

Base `--camera-profile=canon_eos_r100` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
