# Panasonic DC-S1R
Profile slug: `panasonic_dc_s1r`  
EXIF Make/Model: `Panasonic` / `DC-S1R`
Native geometry: 8392x5620 most common decoded dims across 61 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Laowa 15mm F4.5 Zero-D Shift/0025043063.rw2`
Files seen: 61 (Laowa 15mm F4.5 Zero-D Shift/0025043063.rw2, Laowa 15mm F4.5 Zero-D Shift/5265025760.rw2, Panasonic LUMIX S 18mm F1.8/2965034422.rw2, Panasonic LUMIX S 18mm F1.8/4574268687.rw2, ...)
Software strings observed: Ver.0.7, Ver.1.0, Ver.1.1, Ver.1.2, Ver.1.3, Ver.1.7, Ver.1.9
Lenses observed: none
ISO observed: 100, 125, 1600, 200, 250, 320, 3200, 400, 500, 5000, 640
Exposure observed: 1.6 s, 1/100 s, 1/1000 s, 1/10000 s, 1/125 s, 1/1300 s, 1/160 s, 1/1600 s, 1/200 s, 1/2000 s, 1/25 s, 1/250 s, 1/30 s, 1/320 s, 1/40 s, 1/400 s, 1/50 s, 1/500 s, 1/60 s, 1/640 s, 1/80 s, 1/800 s, 4 s, 5 s, 8 s
F-number observed: F0, F1.4, F1.8, F10, F11, F2, F2.5, F2.8, F3.5, F4, F4.5, F5, F5.6, F6.3, F7.1, F8, F9
Focal length observed: 0.0 mm, 102.0 mm, 104.0 mm, 105.0 mm, 129.0 mm, 14.0 mm, 147.0 mm, 149.0 mm, 15.0 mm, 16.0 mm, 18.0 mm, 188.0 mm, 20.0 mm, 23.0 mm, 24.0 mm, 25.0 mm, 250.0 mm, 261.0 mm, 28.0 mm, 35.0 mm, 36.0 mm, 42.0 mm, 45.0 mm, 48.0 mm, 50.0 mm, 56.0 mm, 58.0 mm, 60.0 mm, 600.0 mm, 65.0 mm, 70.0 mm, 81.0 mm, 85.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-S1R`, UniqueCameraModel `DC-S1R`, Software `Ver.1.9`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 10000], [1, 2000], [1, 1600], [1, 1300], [1, 1000], [1, 800], [10, 8000], [1, 640], [1, 500], [10, 4000], [1, 400], [1, 320], [1, 250], [1, 200], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 100], [1, 80], [1, 60], [10, 500], [1, 50], [1, 40], [1, 30], [10, 250], [1, 25], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [16000, 10000], [20, 10], [10, 5], [10, 4], [30, 10], [10, 3], [40000, 10000], [50000, 10000], [10, 2], [50, 10], [60, 10], [80000, 10000], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [450, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [900, 100], [1000, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 5000, 6400]
- Lens pool (1): DC-S1R built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['SAM']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_s1r-native`: pins 8392x5620 (native sensor geometry)

Base `--camera-profile=panasonic_dc_s1r` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
