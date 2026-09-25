# Canon EOS 5DS R
Profile slug: `canon_eos_5ds_r`  
EXIF Make/Model: `Canon` / `Canon EOS 5DS R`
Native geometry: 8736x5856 most common decoded dims across 26 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon 100-400mm F4.5-5.6L IS II/5388979576.cr2`
Files seen: 26 (Canon 100-400mm F4.5-5.6L IS II/5388979576.cr2, Canon 100-400mm F4.5-5.6L IS II/9376721232.cr2, Canon 16-35mm F2.8L III USM/3379623732.cr2, Canon EOS 5DS R Real-World/5464364265.cr2, ...)
Software strings observed: none
Lenses observed: 12-24mm F4 DG HSM | Art 016; 14-24mm F2.8 DG HSM | Art 018; 14mm; 14mm F1.8 DG HSM | Art 017; 20mm F1.4 DG HSM | Art 015; 24-70mm F2.8 DG OS HSM | Art 017; 28mm F1.4 DG HSM | Art 019; 40mm F1.4 DG HSM | Art 018; 60-600mm F4.5-6.3 DG OS HSM | Sports 018; 70-200mm F2.8 DG OS HSM | Sports 018; EF100-400mm f/4.5-5.6L IS II USM; EF16-35mm f/2.8L III USM; EF35mm f/1.4L II USM; TAMRON 100-400mm F/4.5-6.3 Di VC USD A035; TAMRON SP 24-70mm F/2.8 Di VC USD G2 A032; TAMRON SP 90mm F/2.8 Di VC USD MACRO1:1 F017
ISO observed: 100, 160, 200, 2000, 3200, 400, 500, 800
Exposure observed: 1/100 s, 1/1000 s, 1/125 s, 1/1250 s, 1/160 s, 1/20 s, 1/200 s, 1/320 s, 1/3200 s, 1/400 s, 1/4000 s, 1/500 s, 1/60 s, 1/640 s, 1/80 s, 1/800 s
F-number observed: F1.4, F1.8, F11, F20, F4, F4.5, F5, F5.6, F6.3, F8
Focal length observed: 12.0 mm, 14.0 mm, 15.0 mm, 16.0 mm, 170.0 mm, 20.0 mm, 208.0 mm, 28.0 mm, 35.0 mm, 40.0 mm, 400.0 mm, 49.0 mm, 57.0 mm, 600.0 mm, 64.0 mm, 70.0 mm, 90.0 mm
EXIF PixelDimensions observed: 8688 x 5792
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 5DS R`, UniqueCameraModel `Canon EOS 5DS R`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 3200], [1, 1250], [1, 1000], [10, 8000], [1, 800], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 100], [1, 80], [1, 60], [10, 500], [10, 250], [1, 20], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2000, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (12): 12-24mm F4 DG HSM | Art 016; 14-24mm F2.8 DG HSM | Art 018; 14mm; 14mm F1.8 DG HSM | Art 017; 20mm F1.4 DG HSM | Art 015; 24-70mm F2.8 DG OS HSM | Art 017; 28mm F1.4 DG HSM | Art 019; 40mm F1.4 DG HSM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_5ds_r-native`: pins 8736x5856 (native sensor geometry)

Base `--camera-profile=canon_eos_5ds_r` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
