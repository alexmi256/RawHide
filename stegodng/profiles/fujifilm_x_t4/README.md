# Fujifilm X-T4
Profile slug: `fujifilm_x_t4`  
EXIF Make/Model: `FUJIFILM` / `X-T4`
Native geometry: 6246x4170 most common decoded dims across 16 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm 23mm F1.4 R LM WR/3770373209.raf`
Files seen: 16 (Fujifilm 23mm F1.4 R LM WR/3770373209.raf, Fujifilm 23mm F1.4 R LM WR/6804098732.raf, Fujifilm X-T4 2/4681201533.raf, Fujifilm X-T4 2/6848379805.raf, ...)
Software strings observed: Digital Camera X-T4 Ver1.00, Digital Camera X-T4 Ver1.01, Digital Camera X-T4 Ver1.10, Digital Camera X-T4 Ver1.20, Digital Camera X-T4 Ver1.22, Digital Camera X-T4 Ver1.39
Lenses observed: XF16-55mmF2.8 R LM WR; XF18mmF1.4 R LM WR; XF23mmF1.4 R LM WR; XF23mmF2 R WR; XF33mmF1.4 R LM WR; XF50mmF1.0 R WR; XF90mmF2 R LM WR
ISO observed: 1000, 1250, 160, 1600, 400, 500, 800
Exposure observed: 1/10 s, 1/125 s, 1/250 s, 1/2900 s, 1/300 s, 1/34 s, 1/4700 s, 1/500 s, 1/60 s, 1/70 s, 1/800 s, 1/85 s, 1/90 s, 1/950 s
F-number observed: F1, F1.4, F1.6, F1.8, F2, F2.8, F3.6, F4, F5.6, F8, F9
Focal length observed: 18.0 mm, 23.0 mm, 33.0 mm, 42.7 mm, 50.0 mm, 90.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-T4`, UniqueCameraModel `X-T4`, Software `Digital Camera X-T4 Ver1.39`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4700], [1, 2900], [1, 950], [10, 8000], [1, 800], [1, 500], [10, 4000], [1, 300], [1, 250], [10, 2000], [1, 125], [10, 1000], [1, 90], [1, 85], [1, 70], [1, 60], [10, 500], [1, 34], [10, 250], [10, 125], [1, 10], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[100, 100], [140, 100], [160, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [360, 100], [400, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (7): XF16-55mmF2.8 R LM WR; XF18mmF1.4 R LM WR; XF23mmF1.4 R LM WR; XF23mmF2 R WR; XF33mmF1.4 R LM WR; XF50mmF1.0 R WR; XF90mmF2 R LM WR
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['0AA']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_t4-native`: pins 6246x4170 (native sensor geometry)

Base `--camera-profile=fujifilm_x_t4` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
