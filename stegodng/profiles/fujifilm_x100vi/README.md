# Fujifilm X100VI
Profile slug: `fujifilm_x100vi`  
EXIF Make/Model: `FUJIFILM` / `X100VI`
Native geometry: 7752x5178 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X100VI 2/4630558796.raf`
Files seen: 4 (Fujifilm X100VI 2/4630558796.raf, Fujifilm X100VI 2/8662841254.raf, Fujifilm X100VI/0245336635.raf, Fujifilm X100VI/8420825547.raf)
Software strings observed: Digital Camera X100VI Ver1.00, Digital Camera X100VI Ver1.10
Lenses observed: none
ISO observed: 200, 250
Exposure observed: 1/200 s, 1/60 s, 1/850 s, 1/950 s
F-number observed: F2, F4, F7.1, F8
Focal length observed: 23.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X100VI`, UniqueCameraModel `X100VI`, Software `Digital Camera X100VI Ver1.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 950], [1, 850], [10, 8000], [10, 4000], [1, 200], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): X100VI built-in lens
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['4AA', 'R2B']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x100vi-native`: pins 7752x5178 (native sensor geometry)

Base `--camera-profile=fujifilm_x100vi` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
