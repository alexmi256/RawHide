# Canon EOS 5D Mark IV
Profile slug: `canon_eos_5d_mark_iv`  
EXIF Make/Model: `Canon` / `Canon EOS 5D Mark IV`
Native geometry: 6744x4502 most common decoded dims across 20 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon 16-35mm F2.8L III USM/2537130705.cr2`
Files seen: 20 (Canon 16-35mm F2.8L III USM/2537130705.cr2, Canon 24-105mm F4 L IS II USM/7671399860.cr2, Canon 24-105mm F4 L IS II USM/8153745849.cr2, Canon 28mm F2.8 IS USM/0946567910.cr2, ...)
Software strings observed: none
Lenses observed: 100-400mm F5-6.3 DG OS HSM | Contemporary 017; 135mm F1.8 DG HSM | Art 017; 24-70mm F2.8 DG OS HSM | Art 017; 85mm F1.4 DG HSM | Art 016; EF16-35mm f/2.8L III USM; EF24-105mm f/4L IS II USM; EF28mm f/2.8 IS USM; EF35mm f/2 IS USM; EF70-200mm f/2.8L IS II USM; EF70-200mm f/4L IS II USM; TAMRON SP 150-600mm F/5-6.3 Di VC USD G2 A022; TAMRON SP 70-200mm F/2.8 Di VC USD G2 A025
ISO observed: 100, 125, 12800, 160, 200, 250, 320, 400, 800
Exposure observed: 1.6 s, 1/1000 s, 1/125 s, 1/160 s, 1/250 s, 1/320 s, 1/400 s, 1/500 s, 1/60 s, 1/640 s, 1/80 s, 1/800 s, 30 s
F-number observed: F1.6, F1.8, F11, F16, F2, F2.5, F2.8, F4, F6.3, F8
Focal length observed: 135.0 mm, 150.0 mm, 16.0 mm, 178.0 mm, 191.0 mm, 234.0 mm, 24.0 mm, 28.0 mm, 35.0 mm, 400.0 mm, 483.0 mm, 70.0 mm, 85.0 mm
EXIF PixelDimensions observed: 6720 x 4480
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 5D Mark IV`, UniqueCameraModel `Canon EOS 5D Mark IV`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1000], [1, 800], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 250], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 80], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [16000, 10000], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1], [300000, 10000]]
- FNumber pool: [[160, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 12800]
- Lens pool (12): 100-400mm F5-6.3 DG OS HSM | Contemporary 017; 135mm F1.8 DG HSM | Art 017; 24-70mm F2.8 DG OS HSM | Art 017; 85mm F1.4 DG HSM | Art 016; EF16-35mm f/2.8L III USM; EF24-105mm f/4L IS II USM; EF28mm f/
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_5d_mark_iv-native`: pins 6744x4502 (native sensor geometry)

Base `--camera-profile=canon_eos_5d_mark_iv` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
