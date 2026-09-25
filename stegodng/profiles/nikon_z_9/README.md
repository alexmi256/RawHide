# Nikon Z 9
Profile slug: `nikon_z_9`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z 9`
Native geometry: 8280x5520 most common decoded dims across 13 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon 100-400mm F4.5-5.6 VR S/4793464566.nef`
Files seen: 15 (Nikon 100-400mm F4.5-5.6 VR S/4793464566.nef, Nikon 100-400mm F4.5-5.6 VR S/9824960324.nef, Nikon Z 24-120mm F4 S/5648671659.nef, Nikon Z 26mm F2.8/1090122817.nef, ...)
Software strings observed: Ver.01.00, Ver.01.11, Ver.02.00, Ver.03.00
Lenses observed: NIKKOR Z 100-400mm f/4.5-5.6 VR S; NIKKOR Z 24-120mm f/4 S; NIKKOR Z 24-70mm f/2.8 S; NIKKOR Z 26mm f/2.8; NIKKOR Z 400mm f/2.8 TC VR S; NIKKOR Z 400mm f/4.5 VR S; NIKKOR Z 400mm f/4.5 VR S Z TC-1.4x; NIKKOR Z 50mm f/1.2 S; NIKKOR Z 70-200mm f/2.8 VR S
ISO observed: 160, 220, 400, 450, 560, 64, 720
Exposure observed: 1/1000 s, 1/1600 s, 1/200 s, 1/250 s, 1/320 s, 1/500 s, 1/60 s, 1/640 s, 1/80 s
F-number observed: F1.2, F11, F2.8, F5.6, F6.3, F7.1, F8, F9
Focal length observed: 120.0 mm, 145.0 mm, 175.0 mm, 24.0 mm, 26.0 mm, 400.0 mm, 41.0 mm, 50.0 mm, 560.0 mm, 70.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z 9`, UniqueCameraModel `NIKON Z 9`, Software `Ver.03.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [1, 1000], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 320], [1, 250], [1, 200], [10, 2000], [10, 1000], [1, 80], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[120, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 220, 250, 320, 400, 450, 500, 560, 640, 720, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (9): NIKKOR Z 100-400mm f/4.5-5.6 VR S; NIKKOR Z 24-120mm f/4 S; NIKKOR Z 24-70mm f/2.8 S; NIKKOR Z 26mm f/2.8; NIKKOR Z 400mm f/2.8 TC VR S; NIKKOR Z 400mm f/4.5 VR S; NIKKOR Z 400mm f/4.5 VR S Z TC-1.4x;
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_9-native`: pins 8280x5520 (native sensor geometry)

Base `--camera-profile=nikon_z_9` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
