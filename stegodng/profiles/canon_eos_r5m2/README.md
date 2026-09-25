# Canon EOS R5m2
Profile slug: `canon_eos_r5m2`  
EXIF Make/Model: `Canon` / `Canon EOS R5m2`
Native geometry: 8222x5488 most common decoded dims across 18 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS R5 II/0347041779.cr3`
Files seen: 18 (Canon EOS R5 II/0347041779.cr3, Canon EOS R5 II/4911384018.cr3, Canon EOS R5 Mark II/3973651114.cr3, Canon EOS R5 Mark II/6575079090.cr3, ...)
Software strings observed: none
Lenses observed: RF14mm F1.4 L VCM; RF15-35mm F2.8 L IS USM; RF20-50mm F4 L IS USM PZ; RF20mm F1.4 L VCM; RF24-70mm F2.8 L IS USM; RF24mm F1.4 L VCM; RF45mm F1.2 STM; RF7-14mm F2.8-3.5 L FISHEYE STM; RF70-200mm F2.8 L IS USM; RF85mm F1.4 L VCM
ISO observed: 100, 1250, 160, 200, 2500, 4000, 500
Exposure observed: 1/1000 s, 1/125 s, 1/1250 s, 1/160 s, 1/250 s, 1/320 s, 1/400 s, 1/500 s, 1/80 s, 1/800 s
F-number observed: F1.2, F1.4, F1.8, F2.5, F2.8, F3.5, F5.6, F8
Focal length observed: 14.0 mm, 15.0 mm, 20.0 mm, 24.0 mm, 43.0 mm, 45.0 mm, 50.0 mm, 7.0 mm, 70.0 mm, 85.0 mm
EXIF PixelDimensions observed: 8192 x 5464
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R5m2`, UniqueCameraModel `Canon EOS R5m2`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [1, 1000], [1, 800], [10, 8000], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 250], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2500, 3200, 4000, 6400]
- Lens pool (10): RF14mm F1.4 L VCM; RF15-35mm F2.8 L IS USM; RF20-50mm F4 L IS USM PZ; RF20mm F1.4 L VCM; RF24-70mm F2.8 L IS USM; RF24mm F1.4 L VCM; RF45mm F1.2 STM; RF7-14mm F2.8-3.5 L FISHEYE STM; RF70-200mm F2.8 L
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['00', '14']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r5m2-native`: pins 8222x5488 (native sensor geometry)

Base `--camera-profile=canon_eos_r5m2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
