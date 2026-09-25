# Sony a7CR
Profile slug: `sony_ilce_7cr`  
EXIF Make/Model: `SONY` / `ILCE-7CR`
Native geometry: 9566x6374 most common decoded dims across 14 sample(s) (also seen 9564x6376)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma 135mm F1.4 Art/1221197953.arw`
Files seen: 14 (Sigma 135mm F1.4 Art/1221197953.arw, Sigma 135mm F1.4 Art/6747838301.arw, Sigma 20-200mm F3.5-6.3 DG Contemporary/5848504920.arw, Sigma 20-200mm F3.5-6.3 DG Contemporary/8677831377.arw, ...)
Software strings observed: ILCE-7CR v1.00, ILCE-7CR v1.02, ILCE-7CR v2.00
Lenses observed: 135mm F1.4 DG | Art 025; 20-200mm F3.5-6.3 DG | Contemporary 025; 35mm F1.2 DG II | Art 025; FE 16-25mm F2.8 G; FE 16mm F1.8 G; FE 20-70mm F4 G; FE 24-50mm F2.8 G
ISO observed: 100, 1250, 160, 200, 2500, 4000, 500, 640
Exposure observed: 1/1000 s, 1/125 s, 1/15 s, 1/160 s, 1/2000 s, 1/250 s, 1/40 s, 1/60 s, 1/640 s, 1/80 s, 1/800 s
F-number observed: F1.2, F1.4, F1.8, F2.2, F2.8, F5, F6.3, F7.1, F8
Focal length observed: 108.6 mm, 135.0 mm, 16.0 mm, 17.0 mm, 24.0 mm, 35.0 mm, 37.0 mm, 38.0 mm, 47.0 mm, 76.2 mm
EXIF PixelDimensions observed: 9504 x 6336
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-7CR`, UniqueCameraModel `ILCE-7CR`, Software `ILCE-7CR v2.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1000], [1, 800], [10, 8000], [1, 640], [10, 4000], [1, 250], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 80], [1, 60], [10, 500], [1, 40], [10, 250], [1, 15], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [140, 100], [170, 100], [180, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2500, 3200, 4000, 6400]
- Lens pool (7): 135mm F1.4 DG | Art 025; 20-200mm F3.5-6.3 DG | Contemporary 025; 35mm F1.2 DG II | Art 025; FE 16-25mm F2.8 G; FE 16mm F1.8 G; FE 20-70mm F4 G; FE 24-50mm F2.8 G
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_7cr-native`: pins 9566x6374 (native sensor geometry)

Base `--camera-profile=sony_ilce_7cr` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
