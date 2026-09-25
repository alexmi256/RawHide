# Panasonic DC-G9M2
Profile slug: `panasonic_dc_g9m2`  
EXIF Make/Model: `Panasonic` / `DC-G9M2`
Native geometry: 5784x4344 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 2.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Lumix DC-G9 II 2/2662298390.rw2`
Files seen: 4 (Panasonic Lumix DC-G9 II 2/2662298390.rw2, Panasonic Lumix DC-G9 II 2/4118723195.rw2, Panasonic Lumix DC-G9 II/5907621582.rw2, Panasonic Lumix DC-G9 II/9165928236.rw2)
Software strings observed: Ver.0.5, Ver.2.1
Lenses observed: none
ISO observed: 100, 2000
Exposure observed: 1/160 s, 1/1600 s, 1/60 s, 1/800 s
F-number observed: F3.1, F4, F4.5, F7.1
Focal length observed: 12.0 mm, 17.0 mm, 25.0 mm, 35.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-G9M2`, UniqueCameraModel `DC-G9M2`, Software `Ver.2.1`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [10, 8000], [1, 800], [10, 4000], [10, 2000], [1, 160], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [310, 100], [320, 100], [400, 100], [450, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (1): DC-G9M2 built-in lens
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_g9m2-native`: pins 5784x4344 (native sensor geometry)

Base `--camera-profile=panasonic_dc_g9m2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
