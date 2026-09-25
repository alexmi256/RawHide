# Olympus E-M1MarkIII
Profile slug: `olympus_e_m1markiii`  
EXIF Make/Model: `OLYMPUS CORPORATION` / `E-M1MarkIII`
Native geometry: 5240x3912 most common decoded dims across 16 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `OM System 20mm F1.4 Pro 2/2389972566.orf`
Files seen: 16 (OM System 20mm F1.4 Pro 2/2389972566.orf, OM System 20mm F1.4 Pro 2/8963411248.orf, Olympus 100-400mm F5-6.3 IS/3818692631.orf, Olympus 100-400mm F5-6.3 IS/9590835874.orf, ...)
Software strings observed: Version 1.0, Version 1.2
Lenses observed: OLYMPUS M.100-400mm F5.0-6.3; OLYMPUS M.12-45mm F4.0; OLYMPUS M.300mm F4.0; OLYMPUS M.8-25mm F4.0; OM 20mm F1.4
ISO observed: 1250, 200, 400, 80, 800
Exposure observed: 1/125 s, 1/1250 s, 1/160 s, 1/1600 s, 1/200 s, 1/2000 s, 1/250 s, 1/320 s, 1/400 s, 1/640 s, 1/800 s
F-number observed: F14, F2.2, F3.2, F4, F4.5, F5, F5.6, F6.3, F8
Focal length observed: 100.0 mm, 17.0 mm, 20.0 mm, 227.0 mm, 25.0 mm, 30.0 mm, 300.0 mm, 33.0 mm, 374.0 mm, 400.0 mm, 45.0 mm, 8.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OLYMPUS CORPORATION`, Model `E-M1MarkIII`, UniqueCameraModel `E-M1MarkIII`, Software `Version 1.2`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1600], [1, 1250], [10, 8000], [1, 800], [1, 640], [10, 4000], [1, 400], [1, 320], [1, 250], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1400, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (5): OLYMPUS M.100-400mm F5.0-6.3; OLYMPUS M.12-45mm F4.0; OLYMPUS M.300mm F4.0; OLYMPUS M.8-25mm F4.0; OM 20mm F1.4
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `olympus_e_m1markiii-native`: pins 5240x3912 (native sensor geometry)

Base `--camera-profile=olympus_e_m1markiii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
