# Canon EOS 80D
Profile slug: `canon_eos_80d`  
EXIF Make/Model: `Canon` / `Canon EOS 80D`
Native geometry: 6024x4020 most common decoded dims across 9 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.6  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EF 70-300mm f4-5.6 IS II USM/4840024914.cr2`
Files seen: 9 (Canon EF 70-300mm f4-5.6 IS II USM/4840024914.cr2, Canon EF 70-300mm f4-5.6 IS II USM/8770892000.cr2, Canon EOS 80D real world/2568349275.cr2, Canon EOS 80D real world/5703715541.cr2, ...)
Software strings observed: none
Lenses observed: EF100-400mm f/4.5-5.6L IS II USM; EF16-35mm f/4L IS USM; EF70-300mm f/4-5.6 IS II USM; TAMRON 10-24mm F/3.5-4.5 Di II VC HLD B023; TAMRON 100-400mm F/4.5-6.3 Di VC USD A035; TAMRON 18-400mm F/3.5-6.3 Di II VC HLD B028
ISO observed: 100, 125, 160, 800, 8000
Exposure observed: 1/1000 s, 1/160 s, 1/200 s, 1/320 s, 1/500 s, 1/640 s
F-number observed: F4, F5, F5.6, F6.3, F8, F9
Focal length observed: 123.0 mm, 16.0 mm, 18.0 mm, 234.0 mm, 24.0 mm, 300.0 mm, 40.0 mm, 70.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 80D`, UniqueCameraModel `Canon EOS 80D`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1000], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 320], [1, 200], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 8000]
- Lens pool (6): EF100-400mm f/4.5-5.6L IS II USM; EF16-35mm f/4L IS USM; EF70-300mm f/4-5.6 IS II USM; TAMRON 10-24mm F/3.5-4.5 Di II VC HLD B023; TAMRON 100-400mm F/4.5-6.3 Di VC USD A035; TAMRON 18-400mm F/3.5-6.3 
- FocalLength + 35mm equivalent (x1.6), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['02']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_80d-native`: pins 6024x4020 (native sensor geometry)

Base `--camera-profile=canon_eos_80d` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
