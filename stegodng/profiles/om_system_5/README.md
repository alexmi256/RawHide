# OM System OM-5
Profile slug: `om_system_5`  
EXIF Make/Model: `OM Digital Solutions` / `OM-5`
Native geometry: 5240x3912 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `OM System OM-5 2/2754003229.orf`
Files seen: 4 (OM System OM-5 2/2754003229.orf, OM System OM-5 2/5220803230.orf, OM System OM-5/3467955717.orf, OM System OM-5/5970811778.orf)
Software strings observed: Version 1.0
Lenses observed: M.40-150mm F2.8 + MC-14; OLYMPUS M.12-45mm F4.0; OLYMPUS M.25mm F1.2; OM 20mm F1.4
ISO observed: 200, 250, 320
Exposure observed: 1.3 s, 1/1000 s, 1/1250 s, 1/60 s
F-number observed: F1.2, F1.8, F4, F4.5
Focal length observed: 20.0 mm, 210.0 mm, 22.0 mm, 25.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OM Digital Solutions`, Model `OM-5`, UniqueCameraModel `OM-5`, Software `Version 1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [1, 1000], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [13000, 10000], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): M.40-150mm F2.8 + MC-14; OLYMPUS M.12-45mm F4.0; OLYMPUS M.25mm F1.2; OM 20mm F1.4
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `om_system_5-native`: pins 5240x3912 (native sensor geometry)

Base `--camera-profile=om_system_5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
