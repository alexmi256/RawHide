# Fujifilm X-T3
Profile slug: `fujifilm_x_t3`  
EXIF Make/Model: `FUJIFILM` / `X-T3`
Native geometry: 6246x4170 most common decoded dims across 20 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm 8-16mm F2.8/0997056950.raf`
Files seen: 20 (Fujifilm 8-16mm F2.8/0997056950.raf, Fujifilm 8-16mm F2.8/2300095429.raf, Fujifilm X-T3/7998472691.raf, Fujifilm X-T3/9547167208.raf, ...)
Software strings observed: Digital Camera X-T3 Ver1.01, Digital Camera X-T3 Ver2.00, Digital Camera X-T3 Ver3.00, Digital Camera X-T3 Ver3.20, Digital Camera X-T3 Ver4.10
Lenses observed: XF10-24mmF4 R OIS WR; XF16-55mmF2.8 R LM WR; XF16-80mmF4 R OIS WR; XF16mmF2.8 R WR; XF18mmF1.4 R LM WR; XF200mmF2 R LM OIS WR; XF200mmF2 R LM OIS WR + 1.4x F2; XF50-140mmF2.8 R LM OIS WR; XF70-300mmF4-5.6 R LM OIS WR; XF8-16mmF2.8 R LM WR
ISO observed: 1250, 160, 2500, 320, 3200, 500, 640, 800
Exposure observed: 1/105 s, 1/110 s, 1/120 s, 1/125 s, 1/170 s, 1/250 s, 1/30 s, 1/300 s, 1/320 s, 1/38 s, 1/500 s, 1/60 s, 1/6400 s, 1/750 s, 1/80 s, 1/800 s, 10 s
F-number observed: F1.4, F11, F2.8, F3.6, F4, F4.5, F5, F5.6, F8
Focal length observed: 13.8 mm, 13.9 mm, 134.4 mm, 14.4 mm, 16.0 mm, 16.6 mm, 18.0 mm, 200.0 mm, 24.7 mm, 280.0 mm, 34.2 mm, 51.6 mm, 70.0 mm, 8.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-T3`, UniqueCameraModel `X-T3`, Software `Digital Camera X-T3 Ver4.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 6400], [10, 8000], [1, 800], [1, 750], [1, 500], [10, 4000], [1, 320], [1, 300], [1, 250], [10, 2000], [1, 170], [1, 125], [1, 120], [1, 110], [1, 105], [10, 1000], [1, 80], [1, 60], [10, 500], [1, 38], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [100000, 10000], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [360, 100], [400, 100], [450, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2500, 3200, 6400]
- Lens pool (10): XF10-24mmF4 R OIS WR; XF16-55mmF2.8 R LM WR; XF16-80mmF4 R OIS WR; XF16mmF2.8 R WR; XF18mmF1.4 R LM WR; XF200mmF2 R LM OIS WR; XF200mmF2 R LM OIS WR + 1.4x F2; XF50-140mmF2.8 R LM OIS WR; XF70-300mmF4
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['8CA']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_t3-native`: pins 6246x4170 (native sensor geometry)

Base `--camera-profile=fujifilm_x_t3` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
