# Canon EOS R
Profile slug: `canon_eos_r`  
EXIF Make/Model: `Canon` / `Canon EOS R`
Native geometry: 6742x4498 most common decoded dims across 34 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon 85mm F1.2L USM DS/6475859252.cr3`
Files seen: 34 (Canon 85mm F1.2L USM DS/6475859252.cr3, Canon 85mm F1.2L USM DS/9150974608.cr3, Canon EOS R/1024065841.cr3, Canon EOS R/4652324415.cr3, ...)
Software strings observed: none
Lenses observed: 60-600mm F4.5-6.3 DG OS HSM | Sports 018; 70-200mm F2.8 DG OS HSM | Sports 018; RF15-35mm F2.8 L IS USM; RF24-105mm F4 L IS USM; RF24-240mm F4-6.3 IS USM; RF24-70mm F2.8 L IS USM; RF28-70mm F2 L USM; RF35mm F1.8 MACRO IS STM; RF50mm F1.2 L USM; RF70-200mm F2.8 L IS USM; RF85mm F1.2 L USM; RF85mm F1.2 L USM DS; TAMRON 35-150mm F/2.8-4.0 Di VC OSD A043
ISO observed: 100, 160, 1600, 200, 250, 320, 400, 500, 800
Exposure observed: 1/100 s, 1/1000 s, 1/125 s, 1/1250 s, 1/160 s, 1/1600 s, 1/200 s, 1/2500 s, 1/320 s, 1/3200 s, 1/400 s, 1/4000 s, 1/50 s, 1/500 s, 1/5000 s, 1/640 s, 1/800 s, 1/8000 s
F-number observed: F0, F1.2, F1.8, F2, F2.5, F2.8, F4, F4.5, F5, F5.6, F6.3
Focal length observed: 0.0 mm, 100.0 mm, 123.0 mm, 15.0 mm, 19.0 mm, 200.0 mm, 240.0 mm, 28.0 mm, 35.0 mm, 44.0 mm, 47.0 mm, 50.0 mm, 52.0 mm, 60.0 mm, 70.0 mm, 80.0 mm, 85.0 mm, 92.0 mm, 93.0 mm
EXIF PixelDimensions observed: 4176/6720 x 2784/4480
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R`, UniqueCameraModel `Canon EOS R`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 8000], [1, 5000], [1, 4000], [1, 3200], [1, 2500], [1, 1600], [1, 1250], [1, 1000], [1, 800], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 100], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (12): 60-600mm F4.5-6.3 DG OS HSM | Sports 018; 70-200mm F2.8 DG OS HSM | Sports 018; RF15-35mm F2.8 L IS USM; RF24-105mm F4 L IS USM; RF24-240mm F4-6.3 IS USM; RF24-70mm F2.8 L IS USM; RF28-70mm F2 L USM; 
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['01']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r-native`: pins 6742x4498 (native sensor geometry)

Base `--camera-profile=canon_eos_r` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
