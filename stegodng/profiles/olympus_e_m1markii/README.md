# Olympus E-M1MarkII
Profile slug: `olympus_e_m1markii`  
EXIF Make/Model: `OLYMPUS CORPORATION` / `E-M1MarkII`
Native geometry: 5240x3912 most common decoded dims across 16 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Heliskiing with the Olympus E-M1 Mark II/6112199813.orf`
Files seen: 16 (Heliskiing with the Olympus E-M1 Mark II/6112199813.orf, Heliskiing with the Olympus E-M1 Mark II/9657828628.orf, Olympus 12-200 F3.5-6.3/3796079728.orf, Olympus 12-200 F3.5-6.3/8545109913.orf, ...)
Software strings observed: Version 1.0, Version 1.3, Version 2.0, Version 2.1
Lenses observed: LEICA DG 8-18/F2.8-4.0; OLYMPUS M.12-100mm F4.0; OLYMPUS M.12-200mm F3.5-6.3; OLYMPUS M.12-40mm F2.8; OLYMPUS M.25mm F1.2; OLYMPUS M.45mm F1.2; OLYMPUS M.7-14mm F2.8; OLYMPUS M.8mm F1.8
ISO observed: 1600, 200, 250, 500, 800
Exposure observed: 1/100 s, 1/1000 s, 1/1250 s, 1/1600 s, 1/250 s, 1/2500 s, 1/3200 s, 1/400 s, 1/500 s, 1/60 s, 1/640 s, 1/800 s, 20.94 s
F-number observed: F1.2, F2.8, F4, F4.5, F5, F5.6, F6.3, F7.1
Focal length observed: 100.0 mm, 12.0 mm, 15.0 mm, 18.0 mm, 200.0 mm, 25.0 mm, 45.0 mm, 57.0 mm, 7.0 mm, 8.0 mm, 9.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OLYMPUS CORPORATION`, Model `E-M1MarkII`, UniqueCameraModel `E-M1MarkII`, Software `Version 2.1`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [1, 2500], [1, 1600], [1, 1250], [1, 1000], [10, 8000], [1, 800], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 250], [10, 2000], [10, 1000], [1, 100], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1], [209400, 10000]]
- FNumber pool: [[120, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (8): LEICA DG 8-18/F2.8-4.0; OLYMPUS M.12-100mm F4.0; OLYMPUS M.12-200mm F3.5-6.3; OLYMPUS M.12-40mm F2.8; OLYMPUS M.25mm F1.2; OLYMPUS M.45mm F1.2; OLYMPUS M.7-14mm F2.8; OLYMPUS M.8mm F1.8
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `olympus_e_m1markii-native`: pins 5240x3912 (native sensor geometry)

Base `--camera-profile=olympus_e_m1markii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
