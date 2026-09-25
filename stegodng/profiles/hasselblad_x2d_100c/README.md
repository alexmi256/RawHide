# Hasselblad X2D 100C
Profile slug: `hasselblad_x2d_100c`  
EXIF Make/Model: `Hasselblad` / `X2D 100C`
Native geometry: 11664x8750 most common decoded dims across 6 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Hasselblad X2D 100C 2/1613830905.3fr`
Files seen: 6 (Hasselblad X2D 100C 2/1613830905.3fr, Hasselblad X2D 100C 2/5805005626.3fr, Hasselblad X2D 100C/4236625428.3fr, Hasselblad X2D 100C/8742913299.3fr, ...)
Software strings observed: 1.0.0, 2.0.1
Lenses observed: XCD 120; XCD 20-35E@20; XCD 55V
ISO observed: 400, 64
Exposure observed: 1/121 s, 1/15 s, 1/250 s, 1/27 s, 1/45 s, 1/800 s
F-number observed: F16, F2.5, F20, F7.1, F8
Focal length observed: 120.0 mm, 20.0 mm, 55.0 mm
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Hasselblad`, Model `X2D 100C`, UniqueCameraModel `X2D 100C`, Software `2.0.1`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [10, 4000], [1, 250], [10, 2000], [1, 121], [10, 1000], [10, 500], [1, 45], [1, 27], [10, 250], [1, 15], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2000, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (3): XCD 120; XCD 20-35E@20; XCD 55V
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['XT2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `hasselblad_x2d_100c-native`: pins 11664x8750 (native sensor geometry)

Base `--camera-profile=hasselblad_x2d_100c` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
