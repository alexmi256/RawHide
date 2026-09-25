# Nikon D500
Profile slug: `nikon_d500`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D500`
Native geometry: 5600x3728 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon 300mm f4E PF ED VR/0939984415.nef`
Files seen: 6 (Nikon 300mm f4E PF ED VR/0939984415.nef, Nikon 300mm f4E PF ED VR/4333560058.nef, Nikon AF-P DX Nikkor 70-300mm F4.5-6.3G ED VR/2978553346.nef, Nikon AF-P DX Nikkor 70-300mm F4.5-6.3G ED VR/9050063027.nef, ...)
Software strings observed: Ver.1.00, Ver.1.11
Lenses observed: none
ISO observed: 100, 140, 360
Exposure observed: 1/1250 s, 1/1600 s, 1/200 s, 1/5000 s, 1/640 s
F-number observed: F3.5, F4, F4.5, F4.8, F5.6, F6.3
Focal length observed: 102.0 mm, 300.0 mm, 350.0 mm, 40.0 mm, 70.0 mm
Serial tags present: Exif.Nikon3.SerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D500`, UniqueCameraModel `NIKON D500`, Software `Ver.1.11`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 5000], [1, 1600], [1, 1250], [10, 8000], [1, 640], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [450, 100], [480, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 140, 160, 200, 250, 320, 360, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): NIKON D500 built-in lens
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d500-native`: pins 5600x3728 (native sensor geometry)

Base `--camera-profile=nikon_d500` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
