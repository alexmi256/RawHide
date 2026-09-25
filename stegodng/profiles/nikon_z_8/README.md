# Nikon Z 8
Profile slug: `nikon_z_8`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z 8`
Native geometry: 8280x5520 max decoded-RAW dims across the model's samples (incl. masked margins)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon 24-105mm F4-7.1/3791560995.nef`
Files seen: 20 (Nikon 24-105mm F4-7.1/3791560995.nef, Nikon 24-105mm F4-7.1/5082882996.nef, Nikon 24-70mm F2.8 S II/4627224320.nef, Nikon 24-70mm F2.8 S II/4968891060.nef, ...)
Software strings observed: Ver.01.00, Ver.02.00, Ver.03.01, Ver.03.10
Lenses observed: TAMRON 12-20mm F2.8 A084 Z; TAMRON 70-180mm F2.8 A065 Z; VR 70-200mm f/2.8G; Viltrox AF 35mm f/1.2 LAB Z; Viltrox AF 55mm f/1.8 Z; NIKKOR Z 100-400mm f/4.5-5.6 VR S; NIKKOR Z 24-105mm f/4-7.1; NIKKOR Z 24-70mm f/2.8 S II; NIKKOR Z 24-70mm f/4 S; NIKKOR Z 400mm f/4.5 VR S; NIKKOR Z 50mm f/1.4; NIKKOR Z 70-200mm f/2.8 VR S II
ISO observed: 110, 2000, 2800, 320, 3200, 450, 64, 90
Exposure observed: 1/100 s, 1/15 s, 1/200 s, 1/2000 s, 1/320 s, 1/40 s, 1/400 s, 1/50 s, 1/500 s, 1/80 s, 1/800 s
F-number observed: F1.2, F1.4, F1.8, F2.8, F4, F4.5, F5, F5.6, F8
Focal length observed: 110.0 mm, 150.0 mm, 155.0 mm, 180.0 mm, 20.0 mm, 24.0 mm, 32.5 mm, 35.0 mm, 36.0 mm, 400.0 mm, 41.0 mm, 45.0 mm, 50.0 mm, 55.0 mm, 71.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z 8`, UniqueCameraModel `NIKON Z 8`, Software `Ver.03.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 800], [10, 8000], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 200], [10, 2000], [10, 1000], [1, 100], [1, 80], [10, 500], [1, 50], [1, 40], [10, 250], [1, 15], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 90, 100, 110, 125, 160, 200, 250, 320, 400, 450, 500, 640, 800, 1000, 1250, 1600, 2000, 2800, 3200, 6400]
- Lens pool (12): TAMRON 12-20mm F2.8 A084 Z; TAMRON 70-180mm F2.8 A065 Z; VR 70-200mm f/2.8G; Viltrox AF 35mm f/1.2 LAB Z; Viltrox AF 55mm f/1.8 Z; NIKKOR Z 100-400mm f/4.5-5.6 VR S; NIKKOR Z 24-105mm f/4-7.1; NIKKOR 
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_8-native`: pins 8280x5520 (native sensor geometry)

Base `--camera-profile=nikon_z_8` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
