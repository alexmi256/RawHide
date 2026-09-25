# Nikon 1 J5
Profile slug: `nikon_1_j5`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON 1 J5`
Native geometry: 5584x3724 most common decoded dims across 2 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon 1 J5 real world/8543426065.nef`
Files seen: 2 (Nikon 1 J5 real world/8543426065.nef, Nikon 1 J5 real world/9223145336.nef)
Software strings observed: Ver.1.00
Lenses observed: 1 NIKKOR VR 10-30mm f/3.5-5.6 PD-ZOOM
ISO observed: 280, 720
Exposure observed: 1/125 s, 1/250 s
F-number observed: F3.5, F4.5
Focal length observed: 10.0 mm, 19.7 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON 1 J5`, UniqueCameraModel `NIKON 1 J5`, Software `Ver.1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 250], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 280, 320, 400, 500, 640, 720, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 1 NIKKOR VR 10-30mm f/3.5-5.6 PD-ZOOM
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['33']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_1_j5-native`: pins 5584x3724 (native sensor geometry)

Base `--camera-profile=nikon_1_j5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
