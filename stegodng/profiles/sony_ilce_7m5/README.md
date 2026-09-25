# Sony a7 V
Profile slug: `sony_ilce_7m5`  
EXIF Make/Model: `SONY` / `ILCE-7M5`
Native geometry: 7168x5120 most common decoded dims across 10 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony FE 400mm F4.5 GM OSS/DSC01120.ARW`
Files seen: 10 (Sony FE 400mm F4.5 GM OSS/DSC01120.ARW, Sony FE 400mm F4.5 GM OSS/DSC01971.ARW, Sony FE 600mm F6.3 GM OSS/DSC00142.ARW, Sony FE 600mm F6.3 GM OSS/DSC00422.ARW, ...)
Software strings observed: ILCE-7M5 v1.00, ILCE-7M5 v2.00
Lenses observed: FE 35mm F1.4 GM; FE 400mm F4.5 GM OSS; FE 600mm F6.3 GM OSS; FE 8-14mm F3.5 Fisheye G; FE 85mm F1.4 GM II
ISO observed: 100, 125, 1600, 200, 3200, 400, 500, 640
Exposure observed: 1/100 s, 1/1250 s, 1/200 s, 1/250 s, 1/2500 s, 1/320 s, 1/40 s, 1/5000 s, 1/800 s
F-number observed: F1.4, F2, F2.2, F22, F4.5, F5, F6.3, F8
Focal length observed: 14.0 mm, 35.0 mm, 400.0 mm, 600.0 mm, 8.0 mm, 85.0 mm
EXIF PixelDimensions observed: 7008 x 4672
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-7M5`, UniqueCameraModel `ILCE-7M5`, Software `ILCE-7M5 v2.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 5000], [1, 2500], [1, 1250], [10, 8000], [1, 800], [10, 4000], [1, 320], [1, 250], [1, 200], [10, 2000], [10, 1000], [1, 100], [10, 500], [1, 40], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (5): FE 35mm F1.4 GM; FE 400mm F4.5 GM OSS; FE 600mm F6.3 GM OSS; FE 8-14mm F3.5 Fisheye G; FE 85mm F1.4 GM II
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_7m5-native`: pins 7168x5120 (native sensor geometry)

Base `--camera-profile=sony_ilce_7m5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
