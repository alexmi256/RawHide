# Nikon Z 5
Profile slug: `nikon_z_5`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z 5`
Native geometry: 6040x4032 most common decoded dims across 8 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon Nikkor Z 24-50mm F4-6.3/7385037734.nef`
Files seen: 8 (Nikon Nikkor Z 24-50mm F4-6.3/7385037734.nef, Nikon Nikkor Z 24-50mm F4-6.3/8902569178.nef, Nikon Z5 2/1624858600.nef, Nikon Z5 2/4538016802.nef, ...)
Software strings observed: Ver.01.00
Lenses observed: 50mm f/1.4G; NIKKOR Z 24-50mm f/4-6.3; NIKKOR Z 50mm f/1.8 S
ISO observed: 100, 110, 14400, 900
Exposure observed: 1/125 s, 1/250 s, 1/320 s, 1/3200 s, 1/400 s, 1/500 s, 1/800 s
F-number observed: F2.8, F4, F5.6, F6.3
Focal length observed: 24.0 mm, 35.0 mm, 50.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z 5`, UniqueCameraModel `NIKON Z 5`, Software `Ver.01.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [10, 8000], [1, 800], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 250], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 110, 125, 160, 200, 250, 320, 400, 500, 640, 800, 900, 1000, 1250, 1600, 3200, 6400, 14400]
- Lens pool (3): 50mm f/1.4G; NIKKOR Z 24-50mm f/4-6.3; NIKKOR Z 50mm f/1.8 S
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30', '40']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_5-native`: pins 6040x4032 (native sensor geometry)

Base `--camera-profile=nikon_z_5` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
