# Nikon D5
Profile slug: `nikon_d5`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D5`
Native geometry: 5584x3728 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `AF-S NIKKOR 70-200mm f2.8E FL ED VR/1748866934.nef`
Files seen: 8 (AF-S NIKKOR 70-200mm f2.8E FL ED VR/1748866934.nef, AF-S NIKKOR 70-200mm f2.8E FL ED VR/7165777886.nef, Nikon 180-400mm f4E TC1.4 FL ED VR/7582370504.nef, Nikon 180-400mm f4E TC1.4 FL ED VR/9252152510.nef, ...)
Software strings observed: Ver.1.00
Lenses observed: none
ISO observed: 100, 1600, 200, 32000, 40000, 560, 800
Exposure observed: 1/1000 s, 1/2000 s, 1/800 s
F-number observed: F2.8, F4, F5, F5.6
Focal length observed: 16.0 mm, 200.0 mm, 250.0 mm, 300.0 mm, 320.0 mm, 85.0 mm, 95.0 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D5`, UniqueCameraModel `NIKON D5`, Software `Ver.1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1000], [10, 8000], [1, 800], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 560, 640, 800, 1000, 1250, 1600, 3200, 6400, 32000, 40000]
- Lens pool (1): NIKON D5 built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30', '35']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d5-native`: pins 5584x3728 (native sensor geometry)

Base `--camera-profile=nikon_d5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
