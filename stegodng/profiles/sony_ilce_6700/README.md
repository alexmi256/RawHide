# Sony a6700
Profile slug: `sony_ilce_6700`  
EXIF Make/Model: `SONY` / `ILCE-6700`
Native geometry: 6240x4168 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony a6700/2625923572.arw`
Files seen: 2 (Sony a6700/2625923572.arw, Sony a6700/3038492132.arw)
Software strings observed: ILCE-6700 v1.00
Lenses observed: E 15mm F1.4 G; E 16-55mm F2.8 G
ISO observed: 100, 2500
Exposure observed: 1/125 s, 1/4000 s
F-number observed: F2.8, F3.5
Focal length observed: 15.0 mm, 55.0 mm
EXIF PixelDimensions observed: 6192 x 4128
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-6700`, UniqueCameraModel `ILCE-6700`, Software `ILCE-6700 v1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [10, 8000], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2500, 3200, 6400]
- Lens pool (2): E 15mm F1.4 G; E 16-55mm F2.8 G
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_6700-native`: pins 6240x4168 (native sensor geometry)

Base `--camera-profile=sony_ilce_6700` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
