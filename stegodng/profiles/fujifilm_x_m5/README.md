# Fujifilm X-M5
Profile slug: `fujifilm_x_m5`  
EXIF Make/Model: `FUJIFILM` / `X-M5`
Native geometry: 6264x4176 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-M5 2/5237679185.raf`
Files seen: 4 (Fujifilm X-M5 2/5237679185.raf, Fujifilm X-M5 2/7040065286.raf, Fujifilm X-M5/4542366053.raf, Fujifilm X-M5/9922913412.raf)
Software strings observed: Digital Camera X-M5 Ver1.00
Lenses observed: XF55-200mmF3.5-4.8 R LM OIS; SIGMA 56mm F1.4 DC DN | Contemporary
ISO observed: 1250, 160, 320, 800
Exposure observed: 1/1250 s, 1/200 s, 1/600 s
F-number observed: F1.4, F14, F2.5, F5
Focal length observed: 56.0 mm, 67.1 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-M5`, UniqueCameraModel `X-M5`, Software `Digital Camera X-M5 Ver1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [10, 8000], [1, 600], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1400, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): XF55-200mmF3.5-4.8 R LM OIS; SIGMA 56mm F1.4 DC DN | Contemporary
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['RWS']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_m5-native`: pins 6264x4176 (native sensor geometry)

Base `--camera-profile=fujifilm_x_m5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
