# Fujifilm GFX50S II
Profile slug: `fujifilm_gfx50s_ii`  
EXIF Make/Model: `FUJIFILM` / `GFX50S II`
Native geometry: 8280x6208 most common decoded dims across 5 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `reference-gfx-combiner`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm GFX 50S II 2/2386189818.raf`
Files seen: 5 (Fujifilm GFX 50S II 2/2386189818.raf, Fujifilm GFX 50S II 2/4757769423.raf, Fujifilm GFX 50S II/7172845065.raf, Fujifilm GFX 50S II/9572048405.raf, ...)
Software strings observed: Digital Camera GFX50S II Ver1.00, Digital Camera GFX50S II Ver1.10
Lenses observed: GF110mmF2 R LM WR; GF35-70mmF4.5-5.6 WR; GF45mmF2.8 R WR
ISO observed: 100, 160, 200, 400
Exposure observed: 1/105 s, 1/27 s, 1/34 s, 1/550 s, 1/60 s
F-number observed: (0/0), F10, F2.8, F5.6, F7.1
Focal length observed: 0.0 mm, 110.0 mm, 45.0 mm, 46.5 mm, 64.1 mm
EXIF PixelDimensions observed: 4000 x 3000
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `GFX50S II`, UniqueCameraModel `GFX50S II`, Software `FUJIFILM Pixel Shift Combiner`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 550], [10, 4000], [10, 2000], [1, 105], [10, 1000], [1, 60], [10, 500], [1, 34], [1, 27], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1000, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (3): GF110mmF2 R LM WR; GF35-70mmF4.5-5.6 WR; GF45mmF2.8 R WR
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['12']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_gfx50s_ii-native`: pins 8280x6208 (native sensor geometry)

Base `--camera-profile=fujifilm_gfx50s_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
