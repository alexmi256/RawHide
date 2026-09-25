# Panasonic DC-S1M2
Profile slug: `panasonic_dc_s1m2`  
EXIF Make/Model: `Panasonic` / `DC-S1M2`
Native geometry: 6008x4008 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic Lumix DC-S1II/0682256433.rw2`
Files seen: 4 (Panasonic Lumix DC-S1II/0682256433.rw2, Panasonic Lumix DC-S1II/4386670752.rw2, Panasonic S1II/1738147982.rw2, Panasonic S1II/9815045774.rw2)
Software strings observed: Ver.1.0, Ver.1.2
Lenses observed: 24mm F1.4 DG DN | Art 022; LUMIX S 100/F2.8 MACRO; LUMIX S 16-35/F4; LUMIX S 24-60/F2.8
ISO observed: 100, 125, 320
Exposure observed: 1/125 s, 1/160 s, 1/60 s, 1/640 s
F-number observed: F1.4, F2.8, F4
Focal length observed: 100.0 mm, 24.0 mm, 35.0 mm, 59.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-S1M2`, UniqueCameraModel `DC-S1M2`, Software `Ver.1.2`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 640], [10, 4000], [10, 2000], [1, 160], [1, 125], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): 24mm F1.4 DG DN | Art 022; LUMIX S 100/F2.8 MACRO; LUMIX S 16-35/F4; LUMIX S 24-60/F2.8
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_s1m2-native`: pins 6008x4008 (native sensor geometry)

Base `--camera-profile=panasonic_dc_s1m2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
