# Sony a1
Profile slug: `sony_ilce_1`  
EXIF Make/Model: `SONY` / `ILCE-1`
Native geometry: 8660x5784 most common decoded dims across 17 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `NiSi 15mm F4 ‘Sunstar’/4481586183.arw`
Files seen: 17 (NiSi 15mm F4 ‘Sunstar’/4481586183.arw, NiSi 15mm F4 ‘Sunstar’/8059766977.arw, Sony 24-70mm F2.8 GM II/5344816037.arw, Sony 24-70mm F2.8 GM II/8675301367.arw, ...)
Software strings observed: ILCE-1 v1.00, ILCE-1 v1.10, ILCE-1 v1.20, ILCE-1 v1.30
Lenses observed: ----; E 50-400mm F4.5-6.3 A067; FE 135mm F1.8 GM; FE 14mm F1.8 GM; FE 24-70mm F2.8 GM II; FE 35mm F1.4 GM; FE 50mm F1.2 GM; FE 70-200mm F2.8 GM OSS II; FE 70-200mm F4 Macro G OSS II
ISO observed: 100, 125, 160, 200, 400, 640
Exposure observed: 1/100 s, 1/1000 s, 1/1600 s, 1/2000 s, 1/250 s, 1/400 s, 1/4000 s, 1/500 s, 1/60 s, 1/640 s
F-number observed: F0, F1.2, F11, F2.8, F3.2, F4, F5.6, F6.3, F8
Focal length observed: 0.0 mm, 135.0 mm, 14.0 mm, 200.0 mm, 277.0 mm, 35.0 mm, 50.0 mm, 70.0 mm, 83.0 mm
EXIF PixelDimensions observed: 8640 x 5760
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-1`, UniqueCameraModel `ILCE-1`, Software `ILCE-1 v1.30`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 2000], [1, 1600], [1, 1000], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 250], [10, 2000], [10, 1000], [1, 100], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (9): ----; E 50-400mm F4.5-6.3 A067; FE 135mm F1.8 GM; FE 14mm F1.8 GM; FE 24-70mm F2.8 GM II; FE 35mm F1.4 GM; FE 50mm F1.2 GM; FE 70-200mm F2.8 GM OSS II; FE 70-200mm F4 Macro G OSS II
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_1-native`: pins 8660x5784 (native sensor geometry)

Base `--camera-profile=sony_ilce_1` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
