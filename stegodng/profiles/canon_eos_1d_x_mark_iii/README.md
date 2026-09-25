# Canon EOS-1D X Mark III
Profile slug: `canon_eos_1d_x_mark_iii`  
EXIF Make/Model: `Canon` / `Canon EOS-1D X Mark III`
Native geometry: 5496x3670 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS-1D X Mark III 2/4360915901.cr3`
Files seen: 4 (Canon EOS-1D X Mark III 2/4360915901.cr3, Canon EOS-1D X Mark III 2/8689528301.cr3, Canon EOS-1D X Mark III/2510649594.cr3, Canon EOS-1D X Mark III/4147248091.cr3)
Software strings observed: none
Lenses observed: 105mm F1.4 DG HSM | Art 018; EF24-105mm f/4L IS II USM; EF24mm f/2.8 IS USM; EF35mm f/2 IS USM
ISO observed: 100, 1250, 2000
Exposure observed: 1/3200 s, 1/400 s, 1/60 s
F-number observed: F1.4, F2.8, F5.6, F8
Focal length observed: 105.0 mm, 24.0 mm, 30.0 mm, 35.0 mm
EXIF PixelDimensions observed: 5472 x 3648
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS-1D X Mark III`, UniqueCameraModel `Canon EOS-1D X Mark III`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [10, 8000], [10, 4000], [1, 400], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (4): 105mm F1.4 DG HSM | Art 018; EF24-105mm f/4L IS II USM; EF24mm f/2.8 IS USM; EF35mm f/2 IS USM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['01', '03']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_1d_x_mark_iii-native`: pins 5496x3670 (native sensor geometry)

Base `--camera-profile=canon_eos_1d_x_mark_iii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
