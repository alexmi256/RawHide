# Olympus PEN-F
Profile slug: `olympus_pen_f`  
EXIF Make/Model: `OLYMPUS CORPORATION` / `PEN-F`
Native geometry: 5200x3904 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Olympus 17mm F1.2/1708954084.orf`
Files seen: 6 (Olympus 17mm F1.2/1708954084.orf, Olympus 17mm F1.2/5319483814.orf, Olympus M.Zuiko Digital ED 30mm F3.5 Macro/0051942060.orf, Olympus M.Zuiko Digital ED 30mm F3.5 Macro/4836570851.orf, ...)
Software strings observed: Version 1.0
Lenses observed: OLYMPUS M.17mm F1.2; OLYMPUS M.30mm F3.5 Macro; OLYMPUS M.75mm F1.8
ISO observed: 200, 2000
Exposure observed: 1/1600 s, 1/2000 s, 1/250 s, 1/50 s, 1/60 s
F-number observed: F1.2, F1.8, F2.2, F3.5, F4
Focal length observed: 17.0 mm, 30.0 mm, 75.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OLYMPUS CORPORATION`, Model `PEN-F`, UniqueCameraModel `PEN-F`, Software `Version 1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1600], [10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [1, 60], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [180, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (3): OLYMPUS M.17mm F1.2; OLYMPUS M.30mm F3.5 Macro; OLYMPUS M.75mm F1.8
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `olympus_pen_f-native`: pins 5200x3904 (native sensor geometry)

Base `--camera-profile=olympus_pen_f` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
