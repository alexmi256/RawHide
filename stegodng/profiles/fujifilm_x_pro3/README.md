# Fujifilm X-Pro3
Profile slug: `fujifilm_x_pro3`  
EXIF Make/Model: `FUJIFILM` / `X-Pro3`
Native geometry: 6246x4170 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-Pro3 2/6287717420.raf`
Files seen: 6 (Fujifilm X-Pro3 2/6287717420.raf, Fujifilm X-Pro3 2/9499976936.raf, Fujifilm X-Pro3/3888496968.raf, Fujifilm X-Pro3/4565987295.raf, ...)
Software strings observed: Digital Camera X-Pro3 Ver1.00
Lenses observed: XF18-135mmF3.5-5.6R LM OIS WR; XF23mmF1.4 R; XF35mmF2 R WR; XF50mmF2 R WR; XF55-200mmF3.5-4.8 R LM OIS
ISO observed: 160, 250, 320, 500
Exposure observed: 1/110 s, 1/170 s, 1/320 s, 1/350 s, 1/500 s
F-number observed: F4, F4.5, F5.6, F6.4, F9
Focal length observed: 200.0 mm, 23.0 mm, 35.0 mm, 50.0 mm, 70.2 mm, 99.8 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-Pro3`, UniqueCameraModel `X-Pro3`, Software `Digital Camera X-Pro3 Ver1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [1, 350], [1, 320], [10, 2000], [1, 170], [1, 110], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [640, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (5): XF18-135mmF3.5-5.6R LM OIS WR; XF23mmF1.4 R; XF35mmF2 R WR; XF50mmF2 R WR; XF55-200mmF3.5-4.8 R LM OIS
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['94']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_pro3-native`: pins 6246x4170 (native sensor geometry)

Base `--camera-profile=fujifilm_x_pro3` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
