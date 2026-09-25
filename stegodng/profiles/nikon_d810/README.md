# Nikon D810
Profile slug: `nikon_d810`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D810`
Native geometry: 7380x4928 most common decoded dims across 15 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Iceland at ISO 64 the Nikon D810 on the Ring Road/3379739213.nef`
Files seen: 15 (Iceland at ISO 64 the Nikon D810 on the Ring Road/3379739213.nef, Iceland at ISO 64 the Nikon D810 on the Ring Road/8898855115.nef, Nikon 105mm F1.4E ED real world/1049143941.nef, Nikon 105mm F1.4E ED real world/5395988719.nef, ...)
Software strings observed: Ver.1.00, Ver.1.01, Ver.1.10, Ver.1.12
Lenses observed: none
ISO observed: 200, 250, 320, 400, 64, 640
Exposure observed: 1.3 s, 1/100 s, 1/160 s, 1/200 s, 1/250 s, 1/320 s, 1/400 s, 1/50 s, 1/60 s, 1/640 s, 1/8000 s
F-number observed: F0, F10, F11, F2, F2.8, F4, F4.5, F5.6, F8
Focal length observed: 0.0 mm, 105.0 mm, 15.0 mm, 19.0 mm, 24.0 mm, 280.0 mm, 300.0 mm, 35.0 mm, 38.0 mm, 40.0 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D810`, UniqueCameraModel `NIKON D810`, Software `Ver.1.12`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 8000], [10, 8000], [1, 640], [10, 4000], [1, 400], [1, 320], [1, 250], [1, 200], [10, 2000], [1, 160], [10, 1000], [1, 100], [1, 60], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [13000, 10000], [15, 10], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [10, 2], [50, 10], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1000, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): NIKON D810 built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d810-native`: pins 7380x4928 (native sensor geometry)

Base `--camera-profile=nikon_d810` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
