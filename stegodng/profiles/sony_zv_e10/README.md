# Sony ZV-E10
Profile slug: `sony_zv_e10`  
EXIF Make/Model: `SONY` / `ZV-E10`
Native geometry: 6024x4024 most common decoded dims across 10 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony E 10-20mm F4 PZ G/4413650717.arw`
Files seen: 10 (Sony E 10-20mm F4 PZ G/4413650717.arw, Sony E 10-20mm F4 PZ G/7638747851.arw, Sony E 11m F1.8/5735755936.arw, Sony E 11m F1.8/8368152956.arw, ...)
Software strings observed: ZV-E10 v1.00, ZV-E10 v2.00
Lenses observed: E 10-18mm F4 OSS; E 11mm F1.8; E 15mm F1.4 G; E 50mm F1.8 OSS; E PZ 10-20mm F4 G; E PZ 16-50mm F3.5-5.6 OSS
ISO observed: 100, 200, 3200
Exposure observed: 1/125 s, 1/2000 s, 1/25 s, 1/250 s, 1/30 s, 1/320 s, 1/3200 s, 1/4000 s, 1/640 s, 1/80 s
F-number observed: F1.8, F16, F2.8, F3.5, F4, F5.6, F7.1, F8
Focal length observed: 11.0 mm, 15.0 mm, 16.0 mm, 18.0 mm, 20.0 mm, 50.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ZV-E10`, UniqueCameraModel `ZV-E10`, Software `ZV-E10 v2.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 3200], [1, 2000], [10, 8000], [1, 640], [10, 4000], [1, 320], [1, 250], [10, 2000], [1, 125], [10, 1000], [1, 80], [10, 500], [1, 30], [10, 250], [1, 25], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (6): E 10-18mm F4 OSS; E 11mm F1.8; E 15mm F1.4 G; E 50mm F1.8 OSS; E PZ 10-20mm F4 G; E PZ 16-50mm F3.5-5.6 OSS
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_zv_e10-native`: pins 6024x4024 (native sensor geometry)

Base `--camera-profile=sony_zv_e10` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
