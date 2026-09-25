# Sony a7R II
Profile slug: `sony_ilce_7rm2`  
EXIF Make/Model: `SONY` / `ILCE-7RM2`
Native geometry: 7968x5320 most common decoded dims across 28 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Mitakon Speedmaster 135mm F1.4/2685164070.arw`
Files seen: 28 (Mitakon Speedmaster 135mm F1.4/2685164070.arw, Sigma 30mm F1.4 DC DN C/3757563033.arw, Sigma 30mm F1.4 DC DN C/5049481647.arw, Sony Alpha 7R II/1550334196.arw, ...)
Software strings observed: ILCE-7RM2 v1.00, ILCE-7RM2 v2.00, ILCE-7RM2 v3.00, ILCE-7RM2 v3.05, ILCE-7RM2 v3.10, ILCE-7RM2 v3.20, ILCE-7RM2 v3.30, ILCE-7RM2 v4.00
Lenses observed: ----; 30mm F1.4 DC DN | Contemporary 016; FE 100mm F2.8 STF GM OSS; FE 16-35mm F2.8 GM; FE 24-70mm F2.8 GM; FE 35mm F1.4 ZA; FE 50mm F1.4 ZA; FE 50mm F1.8; FE 50mm F2.8 Macro; FE 70-200mm F2.8 GM OSS; FE 85mm F1.4 GM; FE 85mm F1.8; Voigtlander MACRO APO-LANTHAR 65mm F2 Aspherical; Voigtlander SUPER WIDE-HELIAR 15mm F4.5 III
ISO observed: 100, 125, 160, 1600, 200, 400, 4000, 50, 500, 8000
Exposure observed: 0.4 s, 1/1000 s, 1/125 s, 1/1250 s, 1/160 s, 1/1600 s, 1/200 s, 1/250 s, 1/3 s, 1/3200 s, 1/50 s, 1/500 s, 1/800 s
F-number observed: F0, F1.4, F1.8, F11, F16, F2, F2.5, F2.8, F5.6, F8
Focal length observed: 0.0 mm, 100.0 mm, 105.0 mm, 15.0 mm, 16.0 mm, 198.0 mm, 30.0 mm, 35.0 mm, 37.0 mm, 50.0 mm, 65.0 mm, 70.0 mm, 85.0 mm
EXIF PixelDimensions observed: 5168/7952 x 3448/5304
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-7RM2`, UniqueCameraModel `ILCE-7RM2`, Software `ILCE-7RM2 v4.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [1, 1600], [1, 1250], [1, 1000], [10, 8000], [1, 800], [1, 500], [10, 4000], [1, 250], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [1, 3], [10, 30], [4000, 10000], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 4000, 6400, 8000]
- Lens pool (12): ----; 30mm F1.4 DC DN | Contemporary 016; FE 100mm F2.8 STF GM OSS; FE 16-35mm F2.8 GM; FE 24-70mm F2.8 GM; FE 35mm F1.4 ZA; FE 50mm F1.4 ZA; FE 50mm F1.8; FE 50mm F2.8 Macro; FE 70-200mm F2.8 GM OSS;
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_7rm2-native`: pins 7968x5320 (native sensor geometry)

Base `--camera-profile=sony_ilce_7rm2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
