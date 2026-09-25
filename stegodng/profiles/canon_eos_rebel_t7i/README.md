# Canon EOS Rebel T7i
Profile slug: `canon_eos_rebel_t7i`  
EXIF Make/Model: `Canon` / `Canon EOS Rebel T7i`
Native geometry: 6024x4020 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.6  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EOS Rebel T7i  EOS 800D/2934375791.cr2`
Files seen: 2 (Canon EOS Rebel T7i  EOS 800D/2934375791.cr2, Canon EOS Rebel T7i  EOS 800D/6619166577.cr2)
Software strings observed: none
Lenses observed: EF-S18-135mm f/3.5-5.6 IS USM; EF28mm f/2.8 IS USM
ISO observed: 100, 125
Exposure observed: 1/160 s, 1/200 s
F-number observed: F5.6, F7.1
Focal length observed: 135.0 mm, 28.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS Rebel T7i`, UniqueCameraModel `Canon EOS Rebel T7i`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 200], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): EF-S18-135mm f/3.5-5.6 IS USM; EF28mm f/2.8 IS USM
- FocalLength + 35mm equivalent (x1.6), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['03']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_rebel_t7i-native`: pins 6024x4020 (native sensor geometry)

Base `--camera-profile=canon_eos_rebel_t7i` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
