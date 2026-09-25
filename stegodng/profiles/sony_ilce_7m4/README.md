# Sony a7 IV
Profile slug: `sony_ilce_7m4`  
EXIF Make/Model: `SONY` / `ILCE-7M4`
Native geometry: 7028x4688 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony 16-35mm F4 PZ/0440599973.arw`
Files seen: 4 (Sony 16-35mm F4 PZ/0440599973.arw, Sony 16-35mm F4 PZ/4992673750.arw, Sony a7 IV/3812843300.arw, Sony a7 IV/8128862791.arw)
Software strings observed: ILCE-7M4 v1.00
Lenses observed: E 28-75mm F2.8 A063; FE PZ 16-35mm F4 G
ISO observed: 100, 250
Exposure observed: 1/25 s, 1/250 s, 1/60 s, 2 s
F-number observed: F11, F4, F7.1, F8
Focal length observed: 19.5 mm, 28.0 mm, 35.0 mm, 75.0 mm
EXIF PixelDimensions observed: 7008 x 4672
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-7M4`, UniqueCameraModel `ILCE-7M4`, Software `ILCE-7M4 v1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [1, 25], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20000, 10000], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): E 28-75mm F2.8 A063; FE PZ 16-35mm F4 G
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_7m4-native`: pins 7028x4688 (native sensor geometry)

Base `--camera-profile=sony_ilce_7m4` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
