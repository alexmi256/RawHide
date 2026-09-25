# Nikon Z 7_2
Profile slug: `nikon_z_7_2`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z 7_2`
Native geometry: 8288x5520 most common decoded dims across 13 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikkor 58mm F0.95 Noct/5825695530.nef`
Files seen: 13 (Nikkor 58mm F0.95 Noct/5825695530.nef, Nikkor 58mm F0.95 Noct/7557545260.nef, Nikon 17-28mm F2.8/6825976733.nef, Nikon 17-28mm F2.8/9691432863.nef, ...)
Software strings observed: Ver.01.00, Ver.01.10, Ver.01.21, Ver.01.50
Lenses observed: VR 70-200mm f/2.8E; NIKKOR Z 14-24mm f/2.8 S; NIKKOR Z 17-28mm f/2.8; NIKKOR Z 28-75mm f/2.8; NIKKOR Z 50mm f/1.2 S; NIKKOR Z 50mm f/1.8 S; NIKKOR Z 58mm f/0.95 S Noct; NIKKOR Z 85mm f/1.8 S
ISO observed: 125, 1250, 1600, 3200, 400, 64, 800
Exposure observed: 0.625 s, 1/125 s, 1/160 s, 1/1600 s, 1/3200 s, 1/400 s, 1/50 s, 1/500 s, 1/5000 s, 30 s, 4 s
F-number observed: F0.95, F1.2, F1.8, F11, F2.5, F2.8, F3.2, F4, F4.5, F5.6
Focal length observed: 20.0 mm, 200.0 mm, 24.0 mm, 28.0 mm, 35.0 mm, 37.0 mm, 50.0 mm, 58.0 mm, 85.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z 7_2`, UniqueCameraModel `NIKON Z 7_2`, Software `Ver.01.50`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 5000], [1, 3200], [1, 1600], [10, 8000], [1, 500], [10, 4000], [1, 400], [10, 2000], [1, 160], [1, 125], [10, 1000], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [6250, 10000], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [40000, 10000], [10, 2], [50, 10], [60, 10], [10, 1], [300000, 10000]]
- FNumber pool: [[95, 100], [120, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (8): VR 70-200mm f/2.8E; NIKKOR Z 14-24mm f/2.8 S; NIKKOR Z 17-28mm f/2.8; NIKKOR Z 28-75mm f/2.8; NIKKOR Z 50mm f/1.2 S; NIKKOR Z 50mm f/1.8 S; NIKKOR Z 58mm f/0.95 S Noct; NIKKOR Z 85mm f/1.8 S
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_7_2-native`: pins 8288x5520 (native sensor geometry)

Base `--camera-profile=nikon_z_7_2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
