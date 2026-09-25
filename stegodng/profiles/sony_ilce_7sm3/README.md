# Sony a7S III
Profile slug: `sony_ilce_7sm3`  
EXIF Make/Model: `SONY` / `ILCE-7SM3`
Native geometry: 4256x2848 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony a7S III/0192026916.arw`
Files seen: 2 (Sony a7S III/0192026916.arw, Sony a7S III/7666791020.arw)
Software strings observed: ILCE-7SM3 v1.01
Lenses observed: E 28-200mm F2.8-5.6 A071; FE 16-35mm F2.8 GM
ISO observed: 32000, 80
Exposure observed: 1/200 s, 2 s
F-number observed: F5.6, F9
Focal length observed: 160.0 mm, 23.0 mm
EXIF PixelDimensions observed: 4240 x 2832
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-7SM3`, UniqueCameraModel `ILCE-7SM3`, Software `ILCE-7SM3 v1.01`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20000, 10000], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 32000]
- Lens pool (2): E 28-200mm F2.8-5.6 A071; FE 16-35mm F2.8 GM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_7sm3-native`: pins 4256x2848 (native sensor geometry)

Base `--camera-profile=sony_ilce_7sm3` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
