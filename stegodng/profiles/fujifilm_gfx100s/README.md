# Fujifilm GFX100S
Profile slug: `fujifilm_gfx100s`  
EXIF Make/Model: `FUJIFILM` / `GFX100S`
Native geometry: 11662x8746 most common decoded dims across 7 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `reference-gfx-combiner`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm GF 35-70mm F4.5-5.6 WR/6767529456.raf`
Files seen: 7 (Fujifilm GF 35-70mm F4.5-5.6 WR/6767529456.raf, Fujifilm GF 35-70mm F4.5-5.6 WR/7604679754.raf, Fujifilm GFX 100S 2/3095995619.raf, Fujifilm GFX 100S 2/8694672048.raf, ...)
Software strings observed: Digital Camera GFX100S Ver1.00, Digital Camera GFX100S Ver1.31
Lenses observed: GF110mmF2 R LM WR; GF30mmF3.5 R WR; GF35-70mmF4.5-5.6 WR; GF80mmF1.7 R WR
ISO observed: 100, 200, 2000, 3200
Exposure observed: 1/125 s, 1/200 s, 1/45 s, 1/480 s, 1/60 s, 1/600 s, 1/90 s
F-number observed: (0/0), F10, F16, F4, F4.5, F8
Focal length observed: 110.0 mm, 19.0 mm, 30.0 mm, 35.0 mm, 70.0 mm, 80.0 mm
EXIF PixelDimensions observed: 4000 x 3000
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `GFX100S`, UniqueCameraModel `GFX100S`, Software `FUJIFILM Pixel Shift Combiner`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 600], [1, 480], [10, 4000], [1, 200], [10, 2000], [1, 125], [10, 1000], [1, 90], [1, 60], [10, 500], [1, 45], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1000, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (4): GF110mmF2 R LM WR; GF30mmF3.5 R WR; GF35-70mmF4.5-5.6 WR; GF80mmF1.7 R WR
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['11']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_gfx100s-native`: pins 11662x8746 (native sensor geometry)

Base `--camera-profile=fujifilm_gfx100s` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
