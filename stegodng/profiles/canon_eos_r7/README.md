# Canon EOS R7
Profile slug: `canon_eos_r7`  
EXIF Make/Model: `Canon` / `Canon EOS R7`
Native geometry: 6984x4660 most common decoded dims across 18 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS R7 2/1361826471.cr3`
Files seen: 18 (Canon EOS R7 2/1361826471.cr3, Canon EOS R7 2/6687894371.cr3, Canon EOS R7/0663385178.cr3, Canon EOS R7/6591493461.cr3, ...)
Software strings observed: none
Lenses observed: 12mm F1.4 DC | Contemporary 025; 15mm F1.4 DC | Contemporary 026; 18-50mm F2.8 DC DN | Contemporary 021; RF-S18-150mm F3.5-6.3 IS STM; RF24-50mm F4.5-6.3 IS STM; RF50mm F1.2 L USM; TAMRON 11-20mm F2.8 B060 RF; TAMRON 17-70mm F2.8 B070 RF; TAMRON 18-300mm F3.5-6.3 B061 RF
ISO observed: 100, 160, 200, 250, 320, 500, 6400
Exposure observed: 1/100 s, 1/1000 s, 1/1250 s, 1/200 s, 1/2000 s, 1/250 s, 1/2500 s, 1/320 s, 1/3200 s, 1/400 s, 1/5000 s, 1/640 s, 1/80 s, 1/800 s
F-number observed: F1.4, F2.2, F2.8, F3.5, F4.5, F5, F5.6, F6.3, F8
Focal length observed: 11.0 mm, 12.0 mm, 15.0 mm, 150.0 mm, 18.0 mm, 20.0 mm, 24.0 mm, 25.0 mm, 42.0 mm, 45.0 mm, 50.0 mm, 64.0 mm, 66.0 mm
EXIF PixelDimensions observed: 6960 x 4640
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS R7`, UniqueCameraModel `Canon EOS R7`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 5000], [1, 3200], [1, 2500], [1, 2000], [1, 1250], [1, 1000], [1, 800], [10, 8000], [1, 640], [10, 4000], [1, 400], [1, 320], [1, 250], [1, 200], [10, 2000], [10, 1000], [1, 100], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (9): 12mm F1.4 DC | Contemporary 025; 15mm F1.4 DC | Contemporary 026; 18-50mm F2.8 DC DN | Contemporary 021; RF-S18-150mm F3.5-6.3 IS STM; RF24-50mm F4.5-6.3 IS STM; RF50mm F1.2 L USM; TAMRON 11-20mm F2.8
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['01', '02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_r7-native`: pins 6984x4660 (native sensor geometry)

Base `--camera-profile=canon_eos_r7` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
