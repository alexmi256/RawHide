# Sony a1 II
Profile slug: `sony_ilce_1m2`  
EXIF Make/Model: `SONY` / `ILCE-1M2`
Native geometry: 8704x6144 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sony FE 28-70mm F2 GM/5532763809.arw`
Files seen: 4 (Sony FE 28-70mm F2 GM/5532763809.arw, Sony FE 28-70mm F2 GM/9451869735.arw, Sony a1 II/0146371903.arw, Sony a1 II/4509809713.arw)
Software strings observed: ILCE-1M2 v0.70, ILCE-1M2 v1.00
Lenses observed: FE 24-70mm F2.8 GM II; FE 28-70mm F2 GM; FE 400mm F2.8 GM OSS
ISO observed: 100, 1000, 320, 640
Exposure observed: 1/3200 s, 1/4000 s, 1/50 s, 1/80 s
F-number observed: F2, F2.8, F4
Focal length observed: 400.0 mm, 50.0 mm, 70.0 mm
EXIF PixelDimensions observed: 8640 x 5760
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-1M2`, UniqueCameraModel `ILCE-1M2`, Software `ILCE-1M2 v1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 3200], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 80], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (3): FE 24-70mm F2.8 GM II; FE 28-70mm F2 GM; FE 400mm F2.8 GM OSS
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_1m2-native`: pins 8704x6144 (native sensor geometry)

Base `--camera-profile=sony_ilce_1m2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
