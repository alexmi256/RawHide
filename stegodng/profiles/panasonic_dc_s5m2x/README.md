# Panasonic DC-S5M2X
Profile slug: `panasonic_dc_s5m2x`  
EXIF Make/Model: `Panasonic` / `DC-S5M2X`
Native geometry: 6008x4008 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Lumix S 28-200mm F4-7.1 Macro OIS/0571196227.rw2`
Files seen: 6 (Panasonic Lumix S 28-200mm F4-7.1 Macro OIS/0571196227.rw2, Panasonic Lumix S 28-200mm F4-7.1 Macro OIS/6657955556.rw2, Panasonic Lumix S5 II X/3652237237.rw2, Panasonic Lumix S5 II X/6765676757.rw2, ...)
Software strings observed: Ver.1.0
Lenses observed: none
ISO observed: 100, 1250, 12800, 1600
Exposure observed: 1/125 s, 1/200 s, 1/250 s, 1/320 s, 1/8000 s
F-number observed: F2, F4, F5.6, F7, F7.1
Focal length observed: 192.0 mm, 200.0 mm, 28.0 mm, 49.0 mm, 65.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-S5M2X`, UniqueCameraModel `DC-S5M2X`, Software `Ver.1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 8000], [10, 8000], [10, 4000], [1, 320], [1, 250], [1, 200], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [700, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 12800]
- Lens pool (1): DC-S5M2X built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_s5m2x-native`: pins 6008x4008 (native sensor geometry)

Base `--camera-profile=panasonic_dc_s5m2x` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
