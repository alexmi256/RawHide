# Sony a6300
Profile slug: `sony_ilce_6300`  
EXIF Make/Model: `SONY` / `ILCE-6300`
Native geometry: 6024x4024 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma 30mm F1.4 Contemporary (E-mount)/0776453563.arw`
Files seen: 4 (Sigma 30mm F1.4 Contemporary (E-mount)/0776453563.arw, Sigma 30mm F1.4 Contemporary (E-mount)/6604303045.arw, Sony a6300 real world/0484010600.arw, Sony a6300 real world/4824478983.arw)
Software strings observed: ILCE-6300 v1.00
Lenses observed: 30mm F1.4 DC DN | Contemporary 016
ISO observed: 100
Exposure observed: 1/1600 s, 1/60 s
F-number observed: F1.4, F5
Focal length observed: 30.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-6300`, UniqueCameraModel `ILCE-6300`, Software `ILCE-6300 v1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 30mm F1.4 DC DN | Contemporary 016
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_6300-native`: pins 6024x4024 (native sensor geometry)

Base `--camera-profile=sony_ilce_6300` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
