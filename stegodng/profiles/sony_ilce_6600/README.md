# Sony a6600
Profile slug: `sony_ilce_6600`  
EXIF Make/Model: `SONY` / `ILCE-6600`
Native geometry: 6024x4024 most common decoded dims across 12 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma 18-50mm F2.8 DC DN 2/0741481541.arw`
Files seen: 12 (Sigma 18-50mm F2.8 DC DN 2/0741481541.arw, Sigma 18-50mm F2.8 DC DN 2/3717465192.arw, Sigma 18-50mm F2.8 DC DN/1732132975.arw, Sigma 18-50mm F2.8 DC DN/8901878200.arw, ...)
Software strings observed: ILCE-6600 v1.00
Lenses observed: 18-50mm F2.8 DC DN | Contemporary 021; E 16-55mm F2.8 G; E 17-70mm F2.8 B070; E 70-350mm F4.5-6.3 G OSS
ISO observed: 100, 125, 320, 400, 640, 800
Exposure observed: 1/125 s, 1/1600 s, 1/200 s, 1/250 s, 1/400 s, 1/50 s, 1/500 s, 1/640 s
F-number observed: F2.8, F4, F4.5, F5, F6.3, F7.1
Focal length observed: 16.0 mm, 160.0 mm, 18.0 mm, 21.7 mm, 25.0 mm, 28.8 mm, 50.0 mm, 54.0 mm, 55.0 mm, 65.0 mm, 70.0 mm, 91.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: none (generic fallback (no serial tags observed))

## Static fields (identical in every output file)
- Make `SONY`, Model `ILCE-6600`, UniqueCameraModel `ILCE-6600`, Software `ILCE-6600 v1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 250], [1, 200], [10, 2000], [1, 125], [10, 1000], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): 18-50mm F2.8 DC DN | Contemporary 021; E 16-55mm F2.8 G; E 17-70mm F2.8 B070; E 70-350mm F4.5-6.3 G OSS
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sony_ilce_6600-native`: pins 6024x4024 (native sensor geometry)

Base `--camera-profile=sony_ilce_6600` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
