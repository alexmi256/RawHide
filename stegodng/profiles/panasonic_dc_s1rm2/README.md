# Panasonic DC-S1RM2
Profile slug: `panasonic_dc_s1rm2`  
EXIF Make/Model: `Panasonic` / `DC-S1RM2`
Native geometry: 8152x5432 most common decoded dims across 18 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `LK Samyang AF 14-24mm F2.8 L/2957889504.rw2`
Files seen: 18 (LK Samyang AF 14-24mm F2.8 L/2957889504.rw2, LK Samyang AF 14-24mm F2.8 L/9373856473.rw2, Panasonic Lumix DC-S1RII/1406432606.rw2, Panasonic Lumix DC-S1RII/4775461970.rw2, ...)
Software strings observed: Ver.1.0, Ver.1.2, Ver.1.4, Ver.1.5
Lenses observed: 20-60mm F2.8-4 DG | Contemporary 026; 35mm F1.4 DG II | Art 026; 85mm F1.2 DG | Art 026; LK SAMYANG 14-24mm F2.8; LUMIX S 100-500/F5-7.1; LUMIX S 100/F2.8 MACRO; LUMIX S 20-60/F3.5-5.6; LUMIX S 20/F2.5; LUMIX S 24-60/F2.8; LUMIX S 40/F2; VILTROX AF 16mm F1.8 L
ISO observed: 100, 125, 2000, 250, 400, 500, 80
Exposure observed: 1/100 s, 1/125 s, 1/250 s, 1/320 s, 1/400 s, 1/5 s, 1/60 s, 1/6400 s, 1/80 s, 1/800 s
F-number observed: F2, F2.2, F2.5, F2.8, F3.6, F4, F4.5, F7.1, F8, F9
Focal length observed: 100.0 mm, 16.0 mm, 19.0 mm, 198.0 mm, 20.0 mm, 24.0 mm, 33.0 mm, 35.0 mm, 40.0 mm, 42.0 mm, 500.0 mm, 60.0 mm, 85.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-S1RM2`, UniqueCameraModel `DC-S1RM2`, Software `Ver.1.5`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 6400], [1, 800], [10, 8000], [10, 4000], [1, 400], [1, 320], [1, 250], [10, 2000], [1, 125], [10, 1000], [1, 100], [1, 80], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [1, 5], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [360, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (11): 20-60mm F2.8-4 DG | Contemporary 026; 35mm F1.4 DG II | Art 026; 85mm F1.2 DG | Art 026; LK SAMYANG 14-24mm F2.8; LUMIX S 100-500/F5-7.1; LUMIX S 100/F2.8 MACRO; LUMIX S 20-60/F3.5-5.6; LUMIX S 20/F2.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_s1rm2-native`: pins 8152x5432 (native sensor geometry)

Base `--camera-profile=panasonic_dc_s1rm2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
