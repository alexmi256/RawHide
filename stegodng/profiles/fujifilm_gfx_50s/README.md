# Fujifilm GFX 50S
Profile slug: `fujifilm_gfx_50s`  
EXIF Make/Model: `FUJIFILM` / `GFX 50S`
Native geometry: 8280x6208 most common decoded dims across 16 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `reference-gfx-combiner`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm GF 100-200mm F5.6/3095277039.raf`
Files seen: 16 (Fujifilm GF 100-200mm F5.6/3095277039.raf, Fujifilm GF 100-200mm F5.6/9882524430.raf, Fujifilm GF 110mm F2/4685367629.raf, Fujifilm GF 110mm F2/8610467773.raf, ...)
Software strings observed: Digital Camera GFX 50S Ver1.00, Digital Camera GFX 50S Ver1.11
Lenses observed: GF100-200mmF5.6 R LM OIS WR; GF110mmF2 R LM WR; GF23mmF4 R LM WR; GF250mmF4 R LM OIS WR; GF32-64mmF4 R LM WR; GF63mmF2.8 R WR
ISO observed: 100, 1250, 1600, 200, 3200, 400, 500, 640, 800
Exposure observed: 1/125 s, 1/1600 s, 1/200 s, 1/2000 s, 1/250 s, 1/280 s, 1/300 s, 1/480 s, 1/500 s, 1/60 s, 1/640 s, 1/680 s, 1/800 s
F-number observed: F11, F2, F2.5, F2.8, F4, F5.6
Focal length observed: 109.3 mm, 110.0 mm, 153.2 mm, 23.0 mm, 250.0 mm, 60.7 mm, 63.0 mm, 64.0 mm
EXIF PixelDimensions observed: 4000 x 3000
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `GFX 50S`, UniqueCameraModel `GFX 50S`, Software `FUJIFILM Pixel Shift Combiner`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1600], [10, 8000], [1, 800], [1, 680], [1, 640], [1, 500], [1, 480], [10, 4000], [1, 300], [1, 280], [1, 250], [1, 200], [10, 2000], [1, 125], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (6): GF100-200mmF5.6 R LM OIS WR; GF110mmF2 R LM WR; GF23mmF4 R LM WR; GF250mmF4 R LM OIS WR; GF32-64mmF4 R LM WR; GF63mmF2.8 R WR
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['71']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_gfx_50s-native`: pins 8280x6208 (native sensor geometry)

Base `--camera-profile=fujifilm_gfx_50s` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
