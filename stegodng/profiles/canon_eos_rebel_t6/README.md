# Canon EOS Rebel T6
Profile slug: `canon_eos_rebel_t6`  
EXIF Make/Model: `Canon` / `Canon EOS Rebel T6`
Native geometry: 5202x3464 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.6  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS Rebel T6 real-world/0300625962.cr2`
Files seen: 2 (Canon EOS Rebel T6 real-world/0300625962.cr2, Canon EOS Rebel T6 real-world/0615250868.cr2)
Software strings observed: none
Lenses observed: EF-S18-55mm f/3.5-5.6 IS II
ISO observed: 100
Exposure observed: 1/200 s, 1/800 s
F-number observed: F4, F5
Focal length observed: 18.0 mm, 24.0 mm
EXIF PixelDimensions observed: 5184 x 3456
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS Rebel T6`, UniqueCameraModel `Canon EOS Rebel T6`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): EF-S18-55mm f/3.5-5.6 IS II
- FocalLength + 35mm equivalent (x1.6), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_rebel_t6-native`: pins 5202x3464 (native sensor geometry)

Base `--camera-profile=canon_eos_rebel_t6` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
