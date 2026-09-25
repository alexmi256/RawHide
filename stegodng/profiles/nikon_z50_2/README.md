# Nikon Z50_2
Profile slug: `nikon_z50_2`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z50_2`
Native geometry: 5600x3728 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon Z50II 2/4182090092.nef`
Files seen: 4 (Nikon Z50II 2/4182090092.nef, Nikon Z50II 2/9886478254.nef, Nikon Z50II 3/3339497984.nef, Nikon Z50II 3/6547665832.nef)
Software strings observed: Ver.01.00
Lenses observed: NIKKOR Z 24-120mm f/4 S; NIKKOR Z DX 16-50mm f/3.5-6.3 VR; 56mm F1.4 DC DN | Contemporary 018
ISO observed: 100, 220
Exposure observed: 0.4 s, 1/100 s, 1/2000 s, 1/400 s
F-number observed: F1.8, F11, F4, F6.3
Focal length observed: 16.0 mm, 40.0 mm, 50.0 mm, 56.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z50_2`, UniqueCameraModel `NIKON Z50_2`, Software `Ver.01.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [10, 8000], [10, 4000], [1, 400], [10, 2000], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [4000, 10000], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 220, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (3): NIKKOR Z 24-120mm f/4 S; NIKKOR Z DX 16-50mm f/3.5-6.3 VR; 56mm F1.4 DC DN | Contemporary 018
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['01', '30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z50_2-native`: pins 5600x3728 (native sensor geometry)

Base `--camera-profile=nikon_z50_2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
