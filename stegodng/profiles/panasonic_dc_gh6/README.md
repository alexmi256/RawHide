# Panasonic DC-GH6
Profile slug: `panasonic_dc_gh6`  
EXIF Make/Model: `Panasonic` / `DC-GH6`
Native geometry: 5792x4352 most common decoded dims across 5 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic GH6/0555270072.rw2`
Files seen: 5 (Panasonic GH6/0555270072.rw2, Panasonic GH6/8316005059.rw2, Panasonic Leica 9mm F1.7/1311969518.rw2, Panasonic Leica DG Vario-Elmarit 12-35mm F2.8/3258605915.rw2, ...)
Software strings observed: Ver.0.B, Ver.2.0
Lenses observed: none
ISO observed: 100, 400
Exposure observed: 1/1000 s, 1/1600 s, 1/250 s, 1/800 s
F-number observed: F1.2, F2.8, F4, F5.6
Focal length observed: 35.0 mm, 43.0 mm, 60.0 mm, 9.0 mm
EXIF PixelDimensions observed: 1920 x 1440
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-GH6`, UniqueCameraModel `DC-GH6`, Software `Ver.2.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [1, 1000], [10, 8000], [1, 800], [10, 4000], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DC-GH6 built-in lens
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_gh6-native`: pins 5792x4352 (native sensor geometry)

Base `--camera-profile=panasonic_dc_gh6` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
