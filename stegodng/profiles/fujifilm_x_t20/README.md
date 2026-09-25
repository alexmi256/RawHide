# Fujifilm X-T20
Profile slug: `fujifilm_x_t20`  
EXIF Make/Model: `FUJIFILM` / `X-T20`
Native geometry: 6032x4028 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-T20/0959001480.raf`
Files seen: 4 (Fujifilm X-T20/0959001480.raf, Fujifilm X-T20/3308671605.jpg, Fujifilm XF 18-55mm F2.8-4 R LM OIS/2778805461.raf, Fujifilm XF 18-55mm F2.8-4 R LM OIS/3785484568.raf)
Software strings observed: Digital Camera X-T20 Ver1.00
Lenses observed: XF18-55mmF2.8-4 R LM OIS; XF18mmF2 R
ISO observed: 200, 3200, 4000, 500
Exposure observed: 1/125 s, 1/1400 s, 1/42 s, 1/60 s
F-number observed: F2, F3.6, F4
Focal length observed: 18.0 mm, 32.9 mm, 35.8 mm, 55.0 mm
EXIF PixelDimensions observed: 1920/6000 x 1280/4000
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-T20`, UniqueCameraModel `X-T20`, Software `Digital Camera X-T20 Ver1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1400], [10, 8000], [10, 4000], [10, 2000], [1, 125], [10, 1000], [1, 60], [10, 500], [1, 42], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [360, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 4000, 6400]
- Lens pool (2): XF18-55mmF2.8-4 R LM OIS; XF18mmF2 R
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['7AQ']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_t20-native`: pins 6032x4028 (native sensor geometry)

Base `--camera-profile=fujifilm_x_t20` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
