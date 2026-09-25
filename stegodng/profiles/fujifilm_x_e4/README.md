# Fujifilm X-E4
Profile slug: `fujifilm_x_e4`  
EXIF Make/Model: `FUJIFILM` / `X-E4`
Native geometry: 6246x4170 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm X-E4 2/3685037890.raf`
Files seen: 8 (Fujifilm X-E4 2/3685037890.raf, Fujifilm X-E4 2/9822976431.raf, Fujifilm X-E4/0019625941.raf, Fujifilm X-E4/9894855431.raf, ...)
Software strings observed: Digital Camera X-E4 Ver1.00
Lenses observed: XF50mmF2 R WR; atx-m 23mm F1.4 X
ISO observed: 160, 320, 400
Exposure observed: 1/125 s, 1/150 s, 1/1500 s, 1/1700 s, 1/250 s, 1/4000 s, 1/420 s, 1/850 s
F-number observed: (0/0), F16, F2, F2.8, F4.5
Focal length observed: 21.0 mm, 23.0 mm, 50.0 mm
EXIF PixelDimensions observed: 4416 x 2944
Serial tags present: Exif.Fujifilm.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `FUJIFILM`, Model `X-E4`, UniqueCameraModel `X-E4`, Software `Digital Camera X-E4 Ver1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 4000], [1, 1700], [1, 1500], [1, 850], [10, 8000], [1, 420], [10, 4000], [1, 250], [10, 2000], [1, 150], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): XF50mmF2 R WR; atx-m 23mm F1.4 X
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1S0']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `fujifilm_x_e4-native`: pins 6246x4170 (native sensor geometry)

Base `--camera-profile=fujifilm_x_e4` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
