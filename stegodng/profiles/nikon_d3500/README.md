# Nikon D3500
Profile slug: `nikon_d3500`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D3500`
Native geometry: 6016x4016 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon D3500 2/5125817913.nef`
Files seen: 4 (Nikon D3500 2/5125817913.nef, Nikon D3500 2/8336615005.nef, Nikon D3500/2514598507.nef, Nikon D3500/3138770550.nef)
Software strings observed: Ver.1.00
Lenses observed: none
ISO observed: 100, 12800, 400
Exposure observed: 1/125 s, 1/200 s, 1/320 s, 1/80 s
F-number observed: F1.8, F5, F7.1
Focal length observed: 20.0 mm, 23.0 mm, 300.0 mm, 35.0 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D3500`, UniqueCameraModel `NIKON D3500`, Software `Ver.1.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 320], [1, 200], [10, 2000], [1, 125], [10, 1000], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 12800]
- Lens pool (1): NIKON D3500 built-in lens
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30', '33']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d3500-native`: pins 6016x4016 (native sensor geometry)

Base `--camera-profile=nikon_d3500` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
