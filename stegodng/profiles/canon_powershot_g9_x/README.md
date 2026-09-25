# Canon PowerShot G9 X
Profile slug: `canon_powershot_g9_x`  
EXIF Make/Model: `Canon` / `Canon PowerShot G9 X`
Native geometry: 5536x3692 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.7  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon PowerShot G9 X/0874916787.cr2`
Files seen: 2 (Canon PowerShot G9 X/0874916787.cr2, Canon PowerShot G9 X/6834688062.cr2)
Software strings observed: none
Lenses observed: none
ISO observed: 125
Exposure observed: 1/125 s, 1/800 s
F-number observed: F4, F4.5
Focal length observed: 10.2 mm, 21.6 mm
EXIF PixelDimensions observed: 5472 x 3648
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon PowerShot G9 X`, UniqueCameraModel `Canon PowerShot G9 X`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Canon PowerShot G9 X built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_powershot_g9_x-native`: pins 5536x3692 (native sensor geometry)

Base `--camera-profile=canon_powershot_g9_x` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
