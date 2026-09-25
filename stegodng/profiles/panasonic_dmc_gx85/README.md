# Panasonic DMC-GX85
Profile slug: `panasonic_dmc_gx85`  
EXIF Make/Model: `Panasonic` / `DMC-GX85`
Native geometry: 4608x3464 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Lumix DMC-GX85/2024631751.rw2`
Files seen: 2 (Panasonic Lumix DMC-GX85/2024631751.rw2, Panasonic Lumix DMC-GX85/8717559306.rw2)
Software strings observed: Ver.0.2
Lenses observed: none
ISO observed: 200
Exposure observed: 1/500 s, 1/80 s
F-number observed: F4.6, F9
Focal length observed: 12.0 mm, 17.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DMC-GX85`, UniqueCameraModel `DMC-GX85`, Software `Ver.0.2`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [10, 2000], [10, 1000], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [460, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DMC-GX85 built-in lens
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dmc_gx85-native`: pins 4608x3464 (native sensor geometry)

Base `--camera-profile=panasonic_dmc_gx85` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
