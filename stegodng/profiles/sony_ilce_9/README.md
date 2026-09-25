# Sony a9
Profile slug: `sony_ilce_9`  
EXIF Make/Model: `SONY` / `ILCE-9`
Native geometry: 6024x4024 most common decoded dims across 18 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony FE 100-400mm F4.5-5.6 GM OSS/1962335798.arw`
Files seen: 18 (Sony FE 100-400mm F4.5-5.6 GM OSS/1962335798.arw, Sony FE 100-400mm F4.5-5.6 GM OSS/5705890476.arw, Sony FE 12-24mm F4 G/0226905831.arw, Sony FE 12-24mm F4 G/4656870189.arw, ...)
Software strings observed: ILCE-9 v0.01, ILCE-9 v1.01, ILCE-9 v2.10, ILCE-9 v4.13, ILCE-9 v4.14, ILCE-9 v5.01
Lenses observed: FE 100-400mm F4.5-5.6 GM OSS; FE 12-24mm F4 G; FE 135mm F1.8 GM; FE 200-600mm F5.6-6.3 G OSS; FE 24-70mm F2.8 GM; FE 400mm F2.8 GM OSS; FE 600mm F4 GM OSS; FE 70-200mm F2.8 GM OSS
ISO observed: 100, 1000, 1250, 160, 200, 2000, 2500, 50, 6400
Exposure observed: 1/1000 s, 1/160 s, 1/1600 s, 1/2000 s, 1/250 s, 1/3200 s, 1/500 s, 1/60 s, 1/640 s, 1/800 s
F-number observed: F1.8, F2.8, F4, F5, F5.6, F6.3, F8
Focal length observed: 100.0 mm, 12.0 mm, 133.0 mm, 135.0 mm, 181.0 mm, 194.0 mm, 200.0 mm, 24.0 mm, 400.0 mm, 41.0 mm, 600.0 mm, 70.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-9`, UniqueCameraModel `ILCE-9`, Software `ILCE-9 v5.01`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [1, 2000], [1, 1600], [1, 1000], [10, 8000], [1, 800], [1, 640], [1, 500], [10, 4000], [1, 250], [10, 2000], [1, 160], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 2500, 3200, 6400]
- Lens pool (8): FE 100-400mm F4.5-5.6 GM OSS; FE 12-24mm F4 G; FE 135mm F1.8 GM; FE 200-600mm F5.6-6.3 G OSS; FE 24-70mm F2.8 GM; FE 400mm F2.8 GM OSS; FE 600mm F4 GM OSS; FE 70-200mm F2.8 GM OSS
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_9-native`: pins 6024x4024 (native sensor geometry)

Base `--camera-profile=sony_ilce_9` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
