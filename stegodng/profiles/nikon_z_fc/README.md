# Nikon Z fc
Profile slug: `nikon_z_fc`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z fc`
Native geometry: 5600x3728 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon Z fc 2/5099579699.nef`
Files seen: 4 (Nikon Z fc 2/5099579699.nef, Nikon Z fc 2/6140729138.nef, Nikon Z fc/2563536465.nef, Nikon Z fc/9947345223.nef)
Software strings observed: Ver.01.00
Lenses observed: NIKKOR Z DX 16-50mm f/3.5-6.3 VR; NIKKOR Z MC 50mm f/2.8
ISO observed: 100, 560
Exposure observed: 1/100 s, 1/200 s, 1/25 s, 1/400 s
F-number observed: F3.3, F5.6, F7.1
Focal length observed: 17.0 mm, 38.0 mm, 50.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z fc`, UniqueCameraModel `NIKON Z fc`, Software `Ver.01.00`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 400], [1, 200], [10, 2000], [10, 1000], [1, 100], [10, 500], [10, 250], [1, 25], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [330, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 560, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): NIKKOR Z DX 16-50mm f/3.5-6.3 VR; NIKKOR Z MC 50mm f/2.8
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30', '40']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_fc-native`: pins 5600x3728 (native sensor geometry)

Base `--camera-profile=nikon_z_fc` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
