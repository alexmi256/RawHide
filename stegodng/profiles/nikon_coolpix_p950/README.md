# Nikon COOLPIX P950
Profile slug: `nikon_coolpix_p950`  
EXIF Make/Model: `NIKON CORPORATION` / `COOLPIX P950`
Native geometry: 4624x3470 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon Coolpix P950/3050494385.nrw`
Files seen: 4 (Nikon Coolpix P950/3050494385.nrw, Nikon Coolpix P950/4357092002.nrw, Nikon P950/5938369482.nrw, Nikon P950/7147064260.nrw)
Software strings observed: COOLPIX P950   V1.0
Lenses observed: none
ISO observed: 100, 200, 320
Exposure observed: 1/2000 s, 1/250 s, 1/500 s
F-number observed: F5.6, F6.3, F6.5, F8
Focal length observed: 116.0 mm, 357.0 mm, 42.8 mm, 9.8 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `COOLPIX P950`, UniqueCameraModel `COOLPIX P950`, Software `COOLPIX P950   V1.0`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [10, 8000], [1, 500], [10, 4000], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [650, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): COOLPIX P950 built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30', '50']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_coolpix_p950-native`: pins 4624x3470 (native sensor geometry)

Base `--camera-profile=nikon_coolpix_p950` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
