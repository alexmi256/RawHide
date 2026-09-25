# Canon EOS R5
Profile slug: `canon_eos_r5`  
EXIF Make/Model: `Canon` / `Canon EOS R5`
Native geometry: 8191x5463 most common decoded dims across 31 sample(s) (also seen 8352x5586)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EF 200mm F1.8 L/8760502743.cr3`
Files seen: 31 (Canon EF 200mm F1.8 L/8760502743.cr3, Canon EF 200mm F1.8 L/9300111519.cr3, Canon EOS R5 2/0895017892.cr3, Canon EOS R5 2/8153583620.cr3, ...)
Software strings observed: none
Lenses observed: EF200mm f/1.8L USM; RF100mm F2.8 L MACRO IS USM; RF14-35mm F4 L IS USM; RF16mm F2.8 STM; RF24-105mm F4 L IS USM; RF28-70mm F2 L USM; RF35mm F1.8 MACRO IS STM; RF50mm F1.8 STM; RF600mm F11 IS STM; RF70-200mm F4 L IS USM; RF800mm F11 IS STM; RF85mm F2 MACRO IS STM
ISO observed: 100, 125, 1600, 200, 250, 2500, 320, 3200, 4000, 500, 640, 800
Exposure observed: 1/100 s, 1/1000 s, 1/125 s, 1/1250 s, 1/13 s, 1/1600 s, 1/200 s, 1/2000 s, 1/25 s, 1/250 s, 1/40 s, 1/400 s, 1/5 s, 1/50 s, 1/500 s, 1/640 s, 1/80 s, 1/800 s, 15 s, 2 s
F-number observed: F0, F1.8, F11, F2, F2.8, F4, F4.5, F5, F5.6, F8
Focal length observed: 0.0 mm, 100.0 mm, 105.0 mm, 16.0 mm, 186.0 mm, 200.0 mm, 35.0 mm, 44.0 mm, 50.0 mm, 600.0 mm, 70.0 mm, 800.0 mm, 81.0 mm, 85.0 mm
EXIF PixelDimensions observed: 8192 x 5464
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R5`, UniqueCameraModel `Canon EOS R5`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1600], [1, 1250], [1, 1000], [1, 800], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 250], [1, 200], [10, 2000], [1, 125], [10, 1000], [1, 100], [1, 80], [10, 500], [1, 50], [1, 40], [10, 250], [1, 25], [1, 13], [10, 125], [10, 60], [1, 5], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [20000, 10000], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1], [150000, 10000]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2500, 3200, 4000, 6400]
- Lens pool (12): EF200mm f/1.8L USM; RF100mm F2.8 L MACRO IS USM; RF14-35mm F4 L IS USM; RF16mm F2.8 STM; RF24-105mm F4 L IS USM; RF28-70mm F2 L USM; RF35mm F1.8 MACRO IS STM; RF50mm F1.8 STM; RF600mm F11 IS STM; RF70
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['00', '01']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r5-native`: pins 8191x5463 (native sensor geometry)

Base `--camera-profile=canon_eos_r5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
