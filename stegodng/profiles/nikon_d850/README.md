# Nikon D850
Profile slug: `nikon_d850`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D850`
Native geometry: 8288x5520 most common decoded dims across 10 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Laowa 20mm F4 Shift/0879985865.nef`
Files seen: 10 (Laowa 20mm F4 Shift/0879985865.nef, Laowa 20mm F4 Shift/1889034490.nef, Lensbaby Burnside 35/7467282454.nef, Lensbaby Burnside 35/9248300807.nef, ...)
Software strings observed: Ver.1.00, Ver.1.10
Lenses observed: none
ISO observed: 180, 200, 400, 64, 90
Exposure observed: 1/100 s, 1/1250 s, 1/160 s, 1/200 s, 1/250 s, 1/500 s, 1/800 s
F-number observed: F0, F16, F2, F2.8, F4, F5.6
Focal length observed: 0.0 mm, 105.0 mm, 15.0 mm, 17.0 mm, 18.0 mm, 35.0 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D850`, UniqueCameraModel `NIKON D850`, Software `Ver.1.10`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [10, 8000], [1, 800], [1, 500], [10, 4000], [1, 250], [1, 200], [10, 2000], [1, 160], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 90, 100, 125, 160, 180, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): NIKON D850 built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30', '50']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d850-native`: pins 8288x5520 (native sensor geometry)

Base `--camera-profile=nikon_d850` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
