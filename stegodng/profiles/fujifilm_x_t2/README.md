# Fujifilm X-T2
Profile slug: `fujifilm_x_t2`  
EXIF Make/Model: `FUJIFILM` / `X-T2`
Native geometry: 6032x4032 most common decoded dims across 10 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm 23mm F2 R WR/0257086730.raf`
Files seen: 10 (Fujifilm 23mm F2 R WR/0257086730.raf, Fujifilm 23mm F2 R WR/8055926374.raf, Fujifilm X-T2 Beta/1526731315.raf, Fujifilm X-T2 Beta/8748156538.raf, ...)
Software strings observed: Digital Camera X-T2 Ver1.00, Digital Camera X-T2 Ver1.34, Digital Camera X-T2 Ver1.35, Digital Camera X-T2 Ver2.00
Lenses observed: XF23mmF2 R WR; XF35mmF2 R WR; XF50-140mmF2.8 R LM OIS WR; XF50mmF2 R WR; XF55-200mmF3.5-4.8 R LM OIS; XF80mmF2.8 R LM OIS WR Macro
ISO observed: 200, 2000, 400
Exposure observed: 1/125 s, 1/1250 s, 1/2000 s, 1/250 s, 1/400 s, 1/550 s, 1/60 s
F-number observed: F2, F2.8, F3.2, F4, F5.6
Focal length observed: 140.0 mm, 200.0 mm, 23.0 mm, 35.0 mm, 50.0 mm, 80.0 mm
EXIF PixelDimensions observed: 1920 x 1280
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-T2`, UniqueCameraModel `X-T2`, Software `Digital Camera X-T2 Ver2.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1250], [10, 8000], [1, 550], [10, 4000], [1, 400], [1, 250], [10, 2000], [1, 125], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (6): XF23mmF2 R WR; XF35mmF2 R WR; XF50-140mmF2.8 R LM OIS WR; XF50mmF2 R WR; XF55-200mmF3.5-4.8 R LM OIS; XF80mmF2.8 R LM OIS WR Macro
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['63']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_t2-native`: pins 6032x4032 (native sensor geometry)

Base `--camera-profile=fujifilm_x_t2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
