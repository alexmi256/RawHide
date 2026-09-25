# Panasonic DC-S5
Profile slug: `panasonic_dc_s5`  
EXIF Make/Model: `Panasonic` / `DC-S5`
Native geometry: 6024x4016 most common decoded dims across 22 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Lumix DC-S5 2/3248267580.rw2`
Files seen: 22 (Panasonic Lumix DC-S5 2/3248267580.rw2, Panasonic Lumix DC-S5 2/7620035737.rw2, Panasonic Lumix DC-S5/3460952296.rw2, Panasonic Lumix DC-S5/9655491043.rw2, ...)
Software strings observed: Ver.0.4, Ver.1.0, Ver.2.0, Ver.2.1, Ver.2.3
Lenses observed: none
ISO observed: 100, 1000, 125, 1600, 200, 2000, 250, 800
Exposure observed: 1/125 s, 1/13 s, 1/160 s, 1/200 s, 1/25 s, 1/250 s, 1/320 s, 1/400 s, 1/500 s, 1/60 s, 1/80 s, 4 s
F-number observed: F0, F1.4, F1.8, F11, F2, F2.8, F4, F5.6, F5.8, F7.1, F8
Focal length observed: 0.0 mm, 127.0 mm, 150.0 mm, 20.0 mm, 200.0 mm, 24.0 mm, 28.0 mm, 300.0 mm, 305.0 mm, 35.0 mm, 43.0 mm, 60.0 mm, 65.0 mm, 90.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-S5`, UniqueCameraModel `DC-S5`, Software `Ver.2.3`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 250], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 80], [1, 60], [10, 500], [10, 250], [1, 25], [1, 13], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [40000, 10000], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [580, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (1): DC-S5 built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_s5-native`: pins 6024x4016 (native sensor geometry)

Base `--camera-profile=panasonic_dc_s5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
