# Fujifilm X-A2
Profile slug: `fujifilm_x_a2`  
EXIF Make/Model: `FUJIFILM` / `X-A2`
Native geometry: 4952x3288 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-A2/5298153373.raf`
Files seen: 2 (Fujifilm X-A2/5298153373.raf, Fujifilm X-A2/7392864124.raf)
Software strings observed: Digital Camera X-A2 Ver1.00
Lenses observed: XC16-50mmF3.5-5.6 OIS II
ISO observed: 200, 320
Exposure observed: 1/60 s, 1/75 s
F-number observed: F4, F5.6
Focal length observed: 21.1 mm, 45.2 mm
EXIF PixelDimensions observed: 1920 x 1280
Serial tags present: Exif.Fujifilm.SerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-A2`, UniqueCameraModel `X-A2`, Software `Digital Camera X-A2 Ver1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 75], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): XC16-50mmF3.5-5.6 OIS II
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_a2-native`: pins 4952x3288 (native sensor geometry)

Base `--camera-profile=fujifilm_x_a2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
