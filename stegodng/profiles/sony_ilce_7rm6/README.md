# Sony a7R VI
Profile slug: `sony_ilce_7rm6`  
EXIF Make/Model: `SONY` / `ILCE-7RM6`
Native geometry: 10240x7168 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony FE 100-400mm F4.5 GM OSS/1553611486.arw`
Files seen: 4 (Sony FE 100-400mm F4.5 GM OSS/1553611486.arw, Sony FE 100-400mm F4.5 GM OSS/5149778168.arw, Sony a7R VI/6420686030.arw, Sony a7R VI/9821823930.arw)
Software strings observed: ILCE-7RM6 v1.01
Lenses observed: FE 100-400mm F4.5 GM OSS; FE 85mm F1.4 GM II
ISO observed: 100, 2000, 250
Exposure observed: 1/2000 s, 1/250 s, 1/320 s, 1/400 s
F-number observed: F2, F4.5, F6.3
Focal length observed: 100.0 mm, 168.0 mm, 400.0 mm, 85.0 mm
EXIF PixelDimensions observed: 9984 x 6656
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-7RM6`, UniqueCameraModel `ILCE-7RM6`, Software `ILCE-7RM6 v1.01`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [10, 8000], [10, 4000], [1, 400], [1, 320], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (2): FE 100-400mm F4.5 GM OSS; FE 85mm F1.4 GM II
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_7rm6-native`: pins 10240x7168 (native sensor geometry)

Base `--camera-profile=sony_ilce_7rm6` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
