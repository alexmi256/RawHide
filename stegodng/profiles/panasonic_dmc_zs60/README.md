# Panasonic DMC-ZS60
Profile slug: `panasonic_dmc_zs60`  
EXIF Make/Model: `Panasonic` / `DMC-ZS60`
Native geometry: 4912x3688 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.7  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Lumix ZS60 real world/4990447954.rw2`
Files seen: 2 (Panasonic Lumix ZS60 real world/4990447954.rw2, Panasonic Lumix ZS60 real world/6013438424.rw2)
Software strings observed: Ver.1.0
Lenses observed: none
ISO observed: 640, 80
Exposure observed: 1/200 s, 1/500 s
F-number observed: F3.7, F5.6
Focal length observed: 30.9 mm, 6.3 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DMC-ZS60`, UniqueCameraModel `DMC-ZS60`, Software `Ver.1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [370, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DMC-ZS60 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dmc_zs60-native`: pins 4912x3688 (native sensor geometry)

Base `--camera-profile=panasonic_dmc_zs60` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
