# Fujifilm X-H2
Profile slug: `fujifilm_x_h2`  
EXIF Make/Model: `FUJIFILM` / `X-H2`
Native geometry: 7752x5178 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-H2/4350441424.raf`
Files seen: 8 (Fujifilm X-H2/4350441424.raf, Fujifilm X-H2/6341067863.raf, Fujifilm XF 23mm F2.8 R WR/2519524630.raf, Fujifilm XF 23mm F2.8 R WR/4341422024.raf, ...)
Software strings observed: Digital Camera X-H2 Ver1.00, Digital Camera X-H2 Ver1.10, Digital Camera X-H2 Ver5.00
Lenses observed: XF23mmF1.4 R LM WR; XF23mmF2.8 R WR; XF30mmF2.8 R LM WR Macro; XF35mmF2 R WR; XF400mmF4.5 R LM OIS WR
ISO observed: 125, 1250, 2000, 800
Exposure observed: 1/12 s, 1/125 s, 1/15 s, 1/170 s, 1/2700 s, 1/28 s, 1/75 s
F-number observed: F1.4, F2, F2.8, F4.5, F5.6, F6.4
Focal length observed: 23.0 mm, 30.0 mm, 35.0 mm, 400.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-H2`, UniqueCameraModel `X-H2`, Software `Digital Camera X-H2 Ver5.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2700], [10, 8000], [10, 4000], [10, 2000], [1, 170], [1, 125], [10, 1000], [1, 75], [10, 500], [1, 28], [10, 250], [1, 15], [10, 125], [1, 12], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [640, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (5): XF23mmF1.4 R LM WR; XF23mmF2.8 R WR; XF30mmF2.8 R LM WR Macro; XF35mmF2 R WR; XF400mmF4.5 R LM OIS WR
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['2CA']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_h2-native`: pins 7752x5178 (native sensor geometry)

Base `--camera-profile=fujifilm_x_h2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
