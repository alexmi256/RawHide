# Sony a6500
Profile slug: `sony_ilce_6500`  
EXIF Make/Model: `SONY` / `ILCE-6500`
Native geometry: 6024x4024 most common decoded dims across 15 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Kamlan 28mm F1.4 for APS-C/8411109374.arw`
Files seen: 15 (Kamlan 28mm F1.4 for APS-C/8411109374.arw, Kamlan 50mm F1.1 II/6236260297.arw, Kamlan 50mm F1.1 II/9446642593.arw, Laowa 9mm F2.8 Zero-D/1276555652.arw, ...)
Software strings observed: ILCE-6500 v1.00, ILCE-6500 v1.04
Lenses observed: ----; 16mm F1.4 DC DN | Contemporary 017; E 10-18mm F4 OSS; E 11-20mm F2.8 B060; E 16-55mm F2.8 G; E 18-135mm F3.5-5.6 OSS; FE 70-200mm F2.8 GM OSS
ISO observed: 100, 160, 200, 400, 640
Exposure observed: 1/1250 s, 1/160 s, 1/1600 s, 1/2000 s, 1/250 s, 1/30 s, 1/320 s, 1/400 s, 1/4000 s, 1/60 s, 1/80 s, 1/800 s
F-number observed: F0, F2.8, F3.5, F5, F5.6, F8
Focal length observed: 0.0 mm, 10.0 mm, 135.0 mm, 16.0 mm, 18.0 mm, 191.0 mm, 20.0 mm, 30.0 mm, 41.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-6500`, UniqueCameraModel `ILCE-6500`, Software `ILCE-6500 v1.04`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 2000], [1, 1600], [1, 1250], [1, 800], [10, 8000], [10, 4000], [1, 400], [1, 320], [1, 250], [10, 2000], [1, 160], [10, 1000], [1, 80], [1, 60], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (7): ----; 16mm F1.4 DC DN | Contemporary 017; E 10-18mm F4 OSS; E 11-20mm F2.8 B060; E 16-55mm F2.8 G; E 18-135mm F3.5-5.6 OSS; FE 70-200mm F2.8 GM OSS
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_6500-native`: pins 6024x4024 (native sensor geometry)

Base `--camera-profile=sony_ilce_6500` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
