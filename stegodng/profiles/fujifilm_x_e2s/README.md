# Fujifilm X-E2S
Profile slug: `fujifilm_x_e2s`  
EXIF Make/Model: `FUJIFILM` / `X-E2S`
Native geometry: 4934x3296 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-E2S real world/6991779912.raf`
Files seen: 2 (Fujifilm X-E2S real world/6991779912.raf, Fujifilm X-E2S real world/7747856309.raf)
Software strings observed: Digital Camera X-E2S Ver1.00
Lenses observed: XF23mmF1.4 R
ISO observed: 200
Exposure observed: 1/120 s, 1/2200 s
F-number observed: F1.4
Focal length observed: 23.0 mm
EXIF PixelDimensions observed: 1920 x 1280
Serial tags present: Exif.Fujifilm.SerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-E2S`, UniqueCameraModel `X-E2S`, Software `Digital Camera X-E2S Ver1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2200], [10, 8000], [10, 4000], [10, 2000], [1, 120], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): XF23mmF1.4 R
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_e2s-native`: pins 4934x3296 (native sensor geometry)

Base `--camera-profile=fujifilm_x_e2s` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
