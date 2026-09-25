# Sony a68
Profile slug: `sony_ilca_68`  
EXIF Make/Model: `SONY` / `ILCA-68`
Native geometry: 6024x4016 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony Alpha SLT-A68 real world/2031888812.arw`
Files seen: 2 (Sony Alpha SLT-A68 real world/2031888812.arw, Sony Alpha SLT-A68 real world/5598142326.arw)
Software strings observed: ILCA-68 v1.00
Lenses observed: 24mm F2 ZA SSM; DT 16-50mm F2.8 SSM
ISO observed: 100
Exposure observed: 1/200 s, 1/800 s
F-number observed: F4, F8
Focal length observed: 24.0 mm, 50.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCA-68`, UniqueCameraModel `ILCA-68`, Software `ILCA-68 v1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): 24mm F2 ZA SSM; DT 16-50mm F2.8 SSM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilca_68-native`: pins 6024x4016 (native sensor geometry)

Base `--camera-profile=sony_ilca_68` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
