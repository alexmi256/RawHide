# Olympus TG-5
Profile slug: `olympus_tg_5`  
EXIF Make/Model: `OLYMPUS CORPORATION` / `TG-5`
Native geometry: 4014x3016 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.7  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Olympus TG-5 in Puerto Rico/2599767878.orf`
Files seen: 6 (Olympus TG-5 in Puerto Rico/2599767878.orf, Olympus TG-5 in Puerto Rico/5497025046.orf, Olympus TG-5/8222319607.orf, Olympus TG-5/8697176108.orf, ...)
Software strings observed: Version 1.0
Lenses observed: none
ISO observed: 100, 640
Exposure observed: 1/125 s, 1/250 s, 1/30 s, 1/320 s, 1/80 s
F-number observed: F2, F2.8, F5, F8
Focal length observed: 11.8 mm, 4.5 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OLYMPUS CORPORATION`, Model `TG-5`, UniqueCameraModel `TG-5`, Software `Version 1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 320], [1, 250], [10, 2000], [1, 125], [10, 1000], [1, 80], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): TG-5 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `olympus_tg_5-native`: pins 4014x3016 (native sensor geometry)

Base `--camera-profile=olympus_tg_5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
