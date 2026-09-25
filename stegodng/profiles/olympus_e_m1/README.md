# Olympus E-M1
Profile slug: `olympus_e_m1`  
EXIF Make/Model: `OLYMPUS IMAGING CORP.` / `E-M1`
Native geometry: 4640x3472 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Olympus ED 25mm F1.2 Pro/3594675282.orf`
Files seen: 4 (Olympus ED 25mm F1.2 Pro/3594675282.orf, Olympus ED 25mm F1.2 Pro/4253870426.orf, Olympus M.ZUIKO DIGITAL ED 300mm F4 IS Pro/2011225894.orf, Olympus M.ZUIKO DIGITAL ED 300mm F4 IS Pro/5040510109.orf)
Software strings observed: Version 4.0
Lenses observed: OLYMPUS M.25mm F1.2; OLYMPUS M.300mm F4.0
ISO observed: 200
Exposure observed: 1/1250 s, 1/250 s, 1/800 s
F-number observed: F1.2, F4, F8
Focal length observed: 25.0 mm, 300.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `OLYMPUS IMAGING CORP.`, Model `E-M1`, UniqueCameraModel `E-M1`, Software `Version 4.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [1, 800], [10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): OLYMPUS M.25mm F1.2; OLYMPUS M.300mm F4.0
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `olympus_e_m1-native`: pins 4640x3472 (native sensor geometry)

Base `--camera-profile=olympus_e_m1` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
