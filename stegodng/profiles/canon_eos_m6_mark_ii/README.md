# Canon EOS M6 Mark II
Profile slug: `canon_eos_m6_mark_ii`  
EXIF Make/Model: `Canon` / `Canon EOS M6 Mark II`
Native geometry: 6984x4660 most common decoded dims across 9 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EF-M 32mm F1.4 STM/3846718505.cr3`
Files seen: 9 (Canon EF-M 32mm F1.4 STM/3846718505.cr3, Canon EF-M 32mm F1.4 STM/9840869374.cr3, Canon EOS M6 Mark II 2/2129414177.cr3, Canon EOS M6 Mark II 2/8455864785.cr3, ...)
Software strings observed: none
Lenses observed: 56mm F1.4 DC DN | Contemporary 018; EF-M15-45mm f/3.5-6.3 IS STM; EF-M32mm f/1.4 STM; EF-S17-55mm f/2.8 IS USM
ISO observed: 100, 125, 200, 400, 500, 5000
Exposure observed: 1/100 s, 1/1000 s, 1/125 s, 1/2000 s, 1/2500 s, 1/4000 s, 1/500 s, 1/80 s
F-number observed: F1.4, F2, F2.5, F2.8, F4, F5, F8
Focal length observed: 17.0 mm, 24.0 mm, 32.0 mm, 55.0 mm, 56.0 mm
EXIF PixelDimensions observed: 6960 x 4640
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS M6 Mark II`, UniqueCameraModel `Canon EOS M6 Mark II`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 2500], [1, 2000], [1, 1000], [10, 8000], [1, 500], [10, 4000], [10, 2000], [1, 125], [10, 1000], [1, 100], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 5000, 6400]
- Lens pool (4): 56mm F1.4 DC DN | Contemporary 018; EF-M15-45mm f/3.5-6.3 IS STM; EF-M32mm f/1.4 STM; EF-S17-55mm f/2.8 IS USM
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['87']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_m6_mark_ii-native`: pins 6984x4660 (native sensor geometry)

Base `--camera-profile=canon_eos_m6_mark_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
