# Canon EOS R6 Mark III
Profile slug: `canon_eos_r6_mark_iii`  
EXIF Make/Model: `Canon` / `Canon EOS R6 Mark III`
Native geometry: 6959x4639 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS R6 III 2/7109775912.cr3`
Files seen: 4 (Canon EOS R6 III 2/7109775912.cr3, Canon EOS R6 III 2/7558913532.cr3, Canon EOS R6 III/1685854545.cr3, Canon EOS R6 III/9963138474.cr3)
Software strings observed: none
Lenses observed: RF24-70mm F2.8 L IS USM; RF28-70mm F2 L USM; RF70-200mm F2.8 L IS USM
ISO observed: 100, 160, 5000
Exposure observed: 1/160 s, 1/4000 s, 1/80 s
F-number observed: F2, F2.8, F8
Focal length observed: 147.0 mm, 28.0 mm, 70.0 mm
EXIF PixelDimensions observed: 6960 x 4640
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R6 Mark III`, UniqueCameraModel `Canon EOS R6 Mark III`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [10, 8000], [10, 4000], [10, 2000], [1, 160], [10, 1000], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 5000, 6400]
- Lens pool (3): RF24-70mm F2.8 L IS USM; RF28-70mm F2 L USM; RF70-200mm F2.8 L IS USM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['15']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r6_mark_iii-native`: pins 6959x4639 (native sensor geometry)

Base `--camera-profile=canon_eos_r6_mark_iii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
