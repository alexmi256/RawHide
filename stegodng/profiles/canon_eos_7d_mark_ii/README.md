# Canon EOS 7D Mark II
Profile slug: `canon_eos_7d_mark_ii`  
EXIF Make/Model: `Canon` / `Canon EOS 7D Mark II`
Native geometry: 5496x3670 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma 50-100 F1.8 HSM Art real-world/1072275688.cr2`
Files seen: 4 (Sigma 50-100 F1.8 HSM Art real-world/1072275688.cr2, Sigma 50-100 F1.8 HSM Art real-world/2567160513.cr2, Sigma 50-100mm F1.8 DC HSM Art/1018763825.cr2, Sigma 50-100mm F1.8 DC HSM Art/3526280282.cr2)
Software strings observed: none
Lenses observed: 50-100mm F1.8 DC HSM | Art 016
ISO observed: 100, 200
Exposure observed: 1/160 s, 1/2500 s, 1/800 s, 1/8000 s
F-number observed: F1.8, F2.8, F4, F5.6
Focal length observed: 50.0 mm, 57.0 mm, 91.0 mm
EXIF PixelDimensions observed: 5472 x 3648
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 7D Mark II`, UniqueCameraModel `Canon EOS 7D Mark II`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 8000], [1, 2500], [1, 800], [10, 8000], [10, 4000], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 50-100mm F1.8 DC HSM | Art 016
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_7d_mark_ii-native`: pins 5496x3670 (native sensor geometry)

Base `--camera-profile=canon_eos_7d_mark_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
