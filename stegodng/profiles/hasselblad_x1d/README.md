# Hasselblad X1D
Profile slug: `hasselblad_x1d`  
EXIF Make/Model: `Hasselblad` / `Hasselblad X1D`
Native geometry: 8278x6208 most common decoded dims across 6 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Hasselblad X1D/7873666735.3fr`
Files seen: 6 (Hasselblad X1D/7873666735.3fr, Hasselblad X1D/8334146208.3fr, Hasselblad XCD 21mm F4/6170298984.3fr, Hasselblad XCD 21mm F4/8573675060.3fr, ...)
Software strings observed: v1.21.0-28
Lenses observed: XCD 120; XCD 21; XCD 45; XCD 80
ISO observed: 100
Exposure observed: 1 s, 1/1000 s, 1/1250 s, 1/1500 s, 1/2000 s, 1/640 s
F-number observed: F1.9, F11, F3.5, F4.8, F8
Focal length observed: 120.0 mm, 21.0 mm, 45.0 mm, 80.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `Hasselblad`, Model `Hasselblad X1D`, UniqueCameraModel `Hasselblad X1D`, Software `v1.21.0-28`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1500], [1, 1250], [1, 1000], [10, 8000], [1, 640], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10000, 10000], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [190, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [480, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): XCD 120; XCD 21; XCD 45; XCD 80
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `hasselblad_x1d-native`: pins 8278x6208 (native sensor geometry)

Base `--camera-profile=hasselblad_x1d` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
