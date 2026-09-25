# Nikon Z f
Profile slug: `nikon_z_f`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z f`
Native geometry: 6064x4040 most common decoded dims across 1 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon Zf/4337451896.nef`
Files seen: 2 (Nikon Zf/4337451896.nef, Nikon Zf/4870781717.nef)
Software strings observed: Ver.01.00, Ver.01.10
Lenses observed: NIKKOR Z 85mm f/1.8 S
ISO observed: 140, 720
Exposure observed: 1/100 s, 1/160 s
F-number observed: F1.8, F5
Focal length observed: 85.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z f`, UniqueCameraModel `NIKON Z f`, Software `Ver.01.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 160], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 140, 160, 200, 250, 320, 400, 500, 640, 720, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): NIKKOR Z 85mm f/1.8 S
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_f-native`: pins 6064x4040 (native sensor geometry)

Base `--camera-profile=nikon_z_f` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
