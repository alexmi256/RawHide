# Canon EOS R6
Profile slug: `canon_eos_r6`  
EXIF Make/Model: `Canon` / `Canon EOS R6`
Native geometry: 5496x3670 most common decoded dims across 5 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS R6 2/2665495593.cr3`
Files seen: 5 (Canon EOS R6 2/2665495593.cr3, Canon EOS R6 2/6197608358.cr3, Canon EOS R6/1811705195.cr3, Canon EOS R6/9175463731.cr3, ...)
Software strings observed: none
Lenses observed: RF14-35mm F4 L IS USM; RF24-105mm F4 L IS USM; RF50mm F1.2 L USM
ISO observed: 100, 1600, 200
Exposure observed: 1/125 s, 1/160 s, 1/4000 s, 1/640 s
F-number observed: F1.4, F11, F2, F4.5, F8
Focal length observed: 105.0 mm, 14.0 mm, 50.0 mm, 83.0 mm
EXIF PixelDimensions observed: 5472 x 3648
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R6`, UniqueCameraModel `Canon EOS R6`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [10, 8000], [1, 640], [10, 4000], [10, 2000], [1, 160], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (3): RF14-35mm F4 L IS USM; RF24-105mm F4 L IS USM; RF50mm F1.2 L USM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['03']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r6-native`: pins 5496x3670 (native sensor geometry)

Base `--camera-profile=canon_eos_r6` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
