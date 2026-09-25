# Fujifilm GFX100RF
Profile slug: `fujifilm_gfx100rf`  
EXIF Make/Model: `FUJIFILM` / `GFX100RF`
Native geometry: 11662x8746 most common decoded dims across 4 sample(s)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 0.79  
Calibration source: `reference-gfx-combiner`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm GFX100RF 2/0580613730.raf`
Files seen: 4 (Fujifilm GFX100RF 2/0580613730.raf, Fujifilm GFX100RF 2/6176168150.raf, Fujifilm GFX100RF/0938253216.raf, Fujifilm GFX100RF/4169961381.raf)
Software strings observed: Digital Camera GFX100RF Ver1.00
Lenses observed: none
ISO observed: 100, 1600, 3200, 80
Exposure observed: 1/125 s, 1/38 s, 1/42 s, 1/450 s
F-number observed: F4, F7.1
Focal length observed: 35.0 mm
EXIF PixelDimensions observed: 4000 x 3000
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `GFX100RF`, UniqueCameraModel `GFX100RF`, Software `FUJIFILM Pixel Shift Combiner`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 450], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [1, 42], [1, 38], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): GFX100RF built-in lens
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['51', 'R2B']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_gfx100rf-native`: pins 11662x8746 (native sensor geometry)

Base `--camera-profile=fujifilm_gfx100rf` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
