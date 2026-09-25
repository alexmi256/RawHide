# Fujifilm X-S10
Profile slug: `fujifilm_x_s10`  
EXIF Make/Model: `FUJIFILM` / `X-S10`
Native geometry: 6246x4170 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-S10 2/4074373265.raf`
Files seen: 8 (Fujifilm X-S10 2/4074373265.raf, Fujifilm X-S10 3/2836581470.raf, Fujifilm X-S10 3/7185191951.raf, Fujifilm XF 18mm F1.4 R LM WR 2/4062857523.raf, ...)
Software strings observed: Digital Camera X-S10 Ver1.00, Digital Camera X-S10 Ver1.02
Lenses observed: XF16-80mmF4 R OIS WR; XF18-135mmF3.5-5.6R LM OIS WR; XF18mmF1.4 R LM WR; XF70-300mmF4-5.6 R LM OIS WR; atx-m 33mm F1.4 X
ISO observed: 160, 1600, 3200, 400, 640, 800
Exposure observed: 1/120 s, 1/12000 s, 1/200 s, 1/3000 s, 1/320 s, 1/4000 s, 1/500 s, 1/60 s
F-number observed: F1.4, F2, F2.2, F4, F5.6
Focal length observed: 135.0 mm, 18.0 mm, 33.0 mm, 70.0 mm, 72.7 mm, 80.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-S10`, UniqueCameraModel `X-S10`, Software `Digital Camera X-S10 Ver1.02`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 12000], [1, 4000], [1, 3000], [10, 8000], [1, 500], [10, 4000], [1, 320], [1, 200], [10, 2000], [1, 120], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (5): XF16-80mmF4 R OIS WR; XF18-135mmF3.5-5.6R LM OIS WR; XF18mmF1.4 R LM WR; XF70-300mmF4-5.6 R LM OIS WR; atx-m 33mm F1.4 X
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['0D0']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_s10-native`: pins 6246x4170 (native sensor geometry)

Base `--camera-profile=fujifilm_x_s10` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
