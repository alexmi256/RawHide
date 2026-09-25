# Canon EOS 6D Mark II
Profile slug: `canon_eos_6d_mark_ii`  
EXIF Make/Model: `Canon` / `Canon EOS 6D Mark II`
Native geometry: 6264x4180 most common decoded dims across 5 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EF 85mm F1.4L IS USM/4144593983.cr2`
Files seen: 5 (Canon EF 85mm F1.4L IS USM/4144593983.cr2, Canon EF 85mm F1.4L IS USM/7018327747.cr2, Canon EOS 6D Mark II/5931293925.cr2, Canon EOS 6D Mark II/8193587075.cr2, ...)
Software strings observed: none
Lenses observed: 14mm F1.8 DG HSM | Art 017; EF100-400mm f/4.5-5.6L IS II USM; EF24-105mm f/4L IS II USM; EF85mm f/1.4L IS USM
ISO observed: 100, 250, 640
Exposure observed: 1/1250 s, 1/400 s, 1/500 s, 1/640 s, 1/800 s
F-number observed: F2, F2.2, F2.5, F5.6
Focal length observed: 105.0 mm, 14.0 mm, 400.0 mm, 85.0 mm
EXIF PixelDimensions observed: 6240 x 4160
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 6D Mark II`, UniqueCameraModel `Canon EOS 6D Mark II`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [10, 8000], [1, 800], [1, 640], [1, 500], [10, 4000], [1, 400], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): 14mm F1.8 DG HSM | Art 017; EF100-400mm f/4.5-5.6L IS II USM; EF24-105mm f/4L IS II USM; EF85mm f/1.4L IS USM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_6d_mark_ii-native`: pins 6264x4180 (native sensor geometry)

Base `--camera-profile=canon_eos_6d_mark_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
