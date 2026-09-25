# Fujifilm X-A7
Profile slug: `fujifilm_x_a7`  
EXIF Make/Model: `FUJIFILM` / `X-A7`
Native geometry: 6016x4014 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-A7 2/0108816446.raf`
Files seen: 6 (Fujifilm X-A7 2/0108816446.raf, Fujifilm X-A7 2/1309092704.raf, Fujifilm X-A7 3/0549008248.raf, Fujifilm X-A7 3/7294667895.raf, ...)
Software strings observed: Digital Camera X-A7 Ver1.00, Digital Camera X-A7 Ver1.01
Lenses observed: XF14mmF2.8 R; XF18-55mmF2.8-4 R LM OIS; XF23mmF2 R WR; XF35mmF2 R WR; XF90mmF2 R LM WR
ISO observed: 1000, 200, 250, 3200, 400
Exposure observed: 1/1000 s, 1/1250 s, 1/160 s, 1/400 s, 1/450 s, 1/85 s
F-number observed: F11, F2.8, F4, F5, F6.4
Focal length observed: 14.0 mm, 18.0 mm, 23.0 mm, 35.0 mm, 90.0 mm
EXIF PixelDimensions observed: 1920 x 1280
Serial tags present: Exif.Fujifilm.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-A7`, UniqueCameraModel `X-A7`, Software `Digital Camera X-A7 Ver1.01`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [1, 1000], [10, 8000], [1, 450], [10, 4000], [1, 400], [10, 2000], [1, 160], [10, 1000], [1, 85], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [640, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (5): XF14mmF2.8 R; XF18-55mmF2.8-4 R LM OIS; XF23mmF2 R WR; XF35mmF2 R WR; XF90mmF2 R LM WR
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['59']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_a7-native`: pins 6016x4014 (native sensor geometry)

Base `--camera-profile=fujifilm_x_a7` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
