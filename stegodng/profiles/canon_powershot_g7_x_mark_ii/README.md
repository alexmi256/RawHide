# Canon PowerShot G7 X Mark II
Profile slug: `canon_powershot_g7_x_mark_ii`  
EXIF Make/Model: `Canon` / `Canon PowerShot G7 X Mark II`
Native geometry: 5536x3692 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.7  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon G7 X Mark II at Sasquatch/0330637416.cr2`
Files seen: 4 (Canon G7 X Mark II at Sasquatch/0330637416.cr2, Canon G7 X Mark II at Sasquatch/6493627523.cr2, Canon PowerShot G7 X Mark II/1239183976.cr2, Canon PowerShot G7 X Mark II/4735809311.cr2)
Software strings observed: none
Lenses observed: none
ISO observed: 125, 800
Exposure observed: 1/200 s, 1/400 s, 1/800 s
F-number observed: F2.8, F4
Focal length observed: 10.3 mm, 36.8 mm, 8.8 mm
EXIF PixelDimensions observed: 5472 x 3648
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon PowerShot G7 X Mark II`, UniqueCameraModel `Canon PowerShot G7 X Mark II`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [10, 4000], [1, 400], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Canon PowerShot G7 X Mark II built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['24']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_powershot_g7_x_mark_ii-native`: pins 5536x3692 (native sensor geometry)

Base `--camera-profile=canon_powershot_g7_x_mark_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
