# Fujifilm X-T5
Profile slug: `fujifilm_x_t5`  
EXIF Make/Model: `FUJIFILM` / `X-T5`
Native geometry: 7752x5178 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-T5 2/2166675207.raf`
Files seen: 6 (Fujifilm X-T5 2/2166675207.raf, Fujifilm X-T5 2/9396562531.raf, Fujifilm X-T5/2030435045.raf, Fujifilm X-T5/9235934268.raf, ...)
Software strings observed: Digital Camera X-T5 Ver1.00, Digital Camera X-T5 Ver1.03, Digital Camera X-T5 Ver2.10
Lenses observed: XF16-50mmF2.8-4.8 R LM WR; XF23mmF1.4 R LM WR; XF35mmF2 R WR
ISO observed: 125, 12800, 2000
Exposure observed: 1/2000 s, 1/34 s, 1/450 s, 1/75 s, 1/950 s, 10 s
F-number observed: F1.4, F2.8, F5.6, F8
Focal length observed: 16.0 mm, 23.0 mm, 35.0 mm, 50.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-T5`, UniqueCameraModel `X-T5`, Software `Digital Camera X-T5 Ver2.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 950], [10, 8000], [1, 450], [10, 4000], [10, 2000], [10, 1000], [1, 75], [10, 500], [1, 34], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [100000, 10000], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400, 12800]
- Lens pool (3): XF16-50mmF2.8-4.8 R LM WR; XF23mmF1.4 R LM WR; XF35mmF2 R WR
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['2CA']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_t5-native`: pins 7752x5178 (native sensor geometry)

Base `--camera-profile=fujifilm_x_t5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
