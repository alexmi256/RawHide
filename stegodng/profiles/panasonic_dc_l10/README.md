# Panasonic DC-L10
Profile slug: `panasonic_dc_l10`  
EXIF Make/Model: `Panasonic` / `DC-L10`
Native geometry: 5208x3912 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic DC-L10 2/0045917227.rw2`
Files seen: 4 (Panasonic DC-L10 2/0045917227.rw2, Panasonic DC-L10 2/1217540354.rw2, Panasonic DC-L10/0045917227.rw2, Panasonic DC-L10/1217540354.rw2)
Software strings observed: Ver.0.5
Lenses observed: DC VARIO-SUMMILUX 1:1.7-2.8/10.9-34 ASPH.
ISO observed: 100
Exposure observed: 1/125 s, 1/200 s
F-number observed: F2.2, F2.8
Focal length observed: 14.3 mm, 26.3 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-L10`, UniqueCameraModel `DC-L10`, Software `Ver.0.5`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 200], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DC VARIO-SUMMILUX 1:1.7-2.8/10.9-34 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_l10-native`: pins 5208x3912 (native sensor geometry)

Base `--camera-profile=panasonic_dc_l10` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
