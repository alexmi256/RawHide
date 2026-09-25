# Canon EOS M6
Profile slug: `canon_eos_m6`  
EXIF Make/Model: `Canon` / `Canon EOS M6`
Native geometry: 6024x4020 most common decoded dims across 7 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EF-M 22mm F2 STM/7964079236.cr2`
Files seen: 7 (Canon EF-M 22mm F2 STM/7964079236.cr2, Canon EF-S 35mm F2.8 Macro/1670621169.cr2, Canon EF-S 35mm F2.8 Macro/6283987547.cr2, Canon EOS M6 w EF-M 22mm F2/0176508290.cr2, ...)
Software strings observed: none
Lenses observed: EF-M22mm f/2 STM; EF-S35mm f/2.8 MACRO IS STM
ISO observed: 100, 320, 800
Exposure observed: 1/125 s, 1/200 s, 1/250 s, 1/60 s, 1/640 s, 1/800 s
F-number observed: F2, F2.8, F4.5, F5.6, F8
Focal length observed: 22.0 mm, 35.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS M6`, UniqueCameraModel `Canon EOS M6`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [1, 640], [10, 4000], [1, 250], [1, 200], [10, 2000], [1, 125], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): EF-M22mm f/2 STM; EF-S35mm f/2.8 MACRO IS STM
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['42']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_m6-native`: pins 6024x4020 (native sensor geometry)

Base `--camera-profile=canon_eos_m6` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
