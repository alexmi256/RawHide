# Panasonic DC-G95
Profile slug: `panasonic_dc_g95`  
EXIF Make/Model: `Panasonic` / `DC-G95`
Native geometry: 5200x3904 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Leica DG 10-25mm F1.7/2891878614.rw2`
Files seen: 6 (Panasonic Leica DG 10-25mm F1.7/2891878614.rw2, Panasonic Leica DG 10-25mm F1.7/9078719848.rw2, Panasonic Lumix DC-G95G90/3456701218.rw2, Panasonic Lumix DC-G95G90/9503186366.rw2, ...)
Software strings observed: Ver.0.2, Ver.1.0
Lenses observed: none
ISO observed: 200, 320
Exposure observed: 1/160 s, 1/2000 s, 1/250 s, 1/800 s
F-number observed: F2.2, F2.8, F3.5, F4.5, F5.6
Focal length observed: 20.0 mm, 25.0 mm, 43.0 mm, 55.0 mm, 60.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-G95`, UniqueCameraModel `DC-G95`, Software `Ver.1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [10, 8000], [1, 800], [10, 4000], [1, 250], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DC-G95 built-in lens
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_g95-native`: pins 5200x3904 (native sensor geometry)

Base `--camera-profile=panasonic_dc_g95` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
