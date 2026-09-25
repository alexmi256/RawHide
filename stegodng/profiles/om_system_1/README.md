# OM System OM-1
Profile slug: `om_system_1`  
EXIF Make/Model: `OM Digital Solutions` / `OM-1`
Native geometry: 5220x3912 most common decoded dims across 16 sample(s) (largest seen 10388x7792 hi-res composite excluded)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `OM System 12-40mm F2.8 PRO II/0343035219.orf`
Files seen: 16 (OM System 12-40mm F2.8 PRO II/0343035219.orf, OM System 12-40mm F2.8 PRO II/6880123238.orf, OM System 40-150mm F4 Pro/6056103892.orf, OM System 40-150mm F4 Pro/9706352168.orf, ...)
Software strings observed: Version 1.0, Version 1.3
Lenses observed: OLYMPUS M.12-100mm F4.0; OLYMPUS M.40-150mm F2.8; OM 12-40mm F2.8 II; OM 40-150mm F4.0; OM 90mm F3.5; OM 90mm F3.5 + MC-20
ISO observed: 1000, 10000, 1600, 200, 2500, 3200, 400, 500, 640, 800
Exposure observed: 0.00308833 s, 1/100 s, 1/1000 s, 1/125 s, 1/160 s, 1/200 s, 1/2000 s, 1/320 s, 1/4 s, 1/50 s, 1/60 s, 1/640 s, 1/80 s, 1/800 s
F-number observed: F2.8, F22, F3.5, F4, F5, F6.3, F8
Focal length observed: 100.0 mm, 130.0 mm, 14.0 mm, 140.0 mm, 150.0 mm, 180.0 mm, 40.0 mm, 44.0 mm, 60.0 mm, 61.0 mm, 90.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OM Digital Solutions`, Model `OM-1`, UniqueCameraModel `OM-1`, Software `Version 1.3`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1000], [1, 800], [10, 8000], [1, 640], [10, 4000], [31, 10000], [1, 320], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 100], [1, 80], [1, 60], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [1, 4], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2500, 3200, 6400, 10000]
- Lens pool (6): OLYMPUS M.12-100mm F4.0; OLYMPUS M.40-150mm F2.8; OM 12-40mm F2.8 II; OM 40-150mm F4.0; OM 90mm F3.5; OM 90mm F3.5 + MC-20
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `om_system_1-native`: pins 5220x3912 (native sensor geometry)

Base `--camera-profile=om_system_1` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
