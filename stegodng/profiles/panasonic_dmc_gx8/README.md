# Panasonic DMC-GX8
Profile slug: `panasonic_dmc_gx8`  
EXIF Make/Model: `Panasonic` / `DMC-GX8`
Native geometry: 5200x3904 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Leica DG Vario-Elmar 100-400mm F4-6.3 ASPH Real World/8386965466.rw2`
Files seen: 8 (Leica DG Vario-Elmar 100-400mm F4-6.3 ASPH Real World/8386965466.rw2, Leica DG Vario-Elmar 100-400mm F4-6.3 ASPH Real World/8724585670.rw2, Panasonic 12-60mm F2.8-4.0/3793505688.rw2, Panasonic 12-60mm F2.8-4.0/7959435112.rw2, ...)
Software strings observed: Ver.2.1, Ver.2.2
Lenses observed: none
ISO observed: 200, 400
Exposure observed: 1/1300 s, 1/160 s, 1/1600 s, 1/3200 s, 1/400 s, 1/640 s
F-number observed: F2.8, F4, F4.5, F5.6, F6.3, F7.1
Focal length observed: 100.0 mm, 12.0 mm, 15.0 mm, 25.0 mm, 35.0 mm, 400.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DMC-GX8`, UniqueCameraModel `DMC-GX8`, Software `Ver.2.2`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [1, 1600], [1, 1300], [10, 8000], [1, 640], [10, 4000], [1, 400], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DMC-GX8 built-in lens
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dmc_gx8-native`: pins 5200x3904 (native sensor geometry)

Base `--camera-profile=panasonic_dmc_gx8` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
