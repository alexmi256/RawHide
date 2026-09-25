# Nikon D780
Profile slug: `nikon_d780`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D780`
Native geometry: 6064x4040 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Fujifilm Acros 100 II film/3593108629.nef`
Files seen: 6 (Fujifilm Acros 100 II film/3593108629.nef, Fujifilm Acros 100 II film/5979041086.nef, Nikon D780 2/3840972526.nef, Nikon D780 2/5249482754.nef, ...)
Software strings observed: Ver.01.00
Lenses observed: 50mm f/1.8D; 60mm f/2.8G; 85mm f/1.8G; VR 24-120mm f/4G; VR 70-200mm f/2.8E
ISO observed: 100, 1250, 5600
Exposure observed: 1/15 s, 1/160 s, 1/2000 s, 1/25 s, 1/640 s, 5 s
F-number observed: F2.8, F4.5, F5.6, F8, F9
Focal length observed: 100.0 mm, 24.0 mm, 50.0 mm, 60.0 mm, 85.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D780`, UniqueCameraModel `NIKON D780`, Software `Ver.01.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [10, 8000], [1, 640], [10, 4000], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [1, 25], [1, 15], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50000, 10000], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 5600, 6400]
- Lens pool (5): 50mm f/1.8D; 60mm f/2.8G; 85mm f/1.8G; VR 24-120mm f/4G; VR 70-200mm f/2.8E
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d780-native`: pins 6064x4040 (native sensor geometry)

Base `--camera-profile=nikon_d780` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
