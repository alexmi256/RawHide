# Hasselblad CFV 100C/907X
Profile slug: `hasselblad_cfv_100c_907x`  
EXIF Make/Model: `Hasselblad` / `CFV 100C/907X`
Native geometry: 11664x8750 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Hasselblad 907X  CFV 100C/1147485111.3fr`
Files seen: 2 (Hasselblad 907X  CFV 100C/1147485111.3fr, Hasselblad 907X  CFV 100C/8581844385.3fr)
Software strings observed: 3.0.0
Lenses observed: XCD 90V
ISO observed: 64
Exposure observed: 1/125 s, 4 s
F-number observed: F16, F5.6
Focal length observed: 90.0 mm
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Hasselblad`, Model `CFV 100C/907X`, UniqueCameraModel `CFV 100C/907X`, Software `3.0.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [40000, 10000], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): XCD 90V
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['JT6']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `hasselblad_cfv_100c_907x-native`: pins 11664x8750 (native sensor geometry)

Base `--camera-profile=hasselblad_cfv_100c_907x` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
