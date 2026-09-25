# Fujifilm X-S20
Profile slug: `fujifilm_x_s20`  
EXIF Make/Model: `FUJIFILM` / `X-S20`
Native geometry: 6252x4176 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-S20 2/7582000977.raf`
Files seen: 4 (Fujifilm X-S20 2/7582000977.raf, Fujifilm X-S20 2/8528013571.raf, Fujifilm X-S20/4678220022.raf, Fujifilm X-S20/6287918233.raf)
Software strings observed: Digital Camera X-S20 Ver1.00, Digital Camera X-S20 Ver1.10
Lenses observed: XF27mmF2.8; XF8mmF3.5 R WR
ISO observed: 160, 250, 400, 800
Exposure observed: 1/100 s
F-number observed: F2.8, F22, F3.5
Focal length observed: 27.0 mm, 8.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-S20`, UniqueCameraModel `X-S20`, Software `Digital Camera X-S20 Ver1.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): XF27mmF2.8; XF8mmF3.5 R WR
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['3T1', 'RWB']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_s20-native`: pins 6252x4176 (native sensor geometry)

Base `--camera-profile=fujifilm_x_s20` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
