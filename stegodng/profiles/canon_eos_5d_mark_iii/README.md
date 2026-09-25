# Canon EOS 5D Mark III
Profile slug: `canon_eos_5d_mark_iii`  
EXIF Make/Model: `Canon` / `Canon EOS 5D Mark III`
Native geometry: 5796x3870 most common decoded dims across 5 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Canon EF 35mm F1.4L II USM real-world/2819426980.cr2`
Files seen: 5 (Canon EF 35mm F1.4L II USM real-world/2819426980.cr2, Tamron SP 35mm f1.8 Di VC USD/6521622542.cr2, Tamron SP 35mm f1.8 Di VC USD/8346316587.cr2, Tamron SP 45mm f1.8 Di VC USD/4242669246.cr2, ...)
Software strings observed: none
Lenses observed: EF35mm f/1.4L II USM; TAMRON SP 35mm F/1.8 Di VC USD F012; TAMRON SP 45mm F/1.8 Di VC USD F013
ISO observed: 100
Exposure observed: 1/100 s, 1/250 s, 1/3200 s, 1/400 s, 1/8000 s
F-number observed: F1.4, F1.8, F3.2, F6.3, F9
Focal length observed: 35.0 mm, 45.0 mm
EXIF PixelDimensions observed: 5760 x 3840
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `Canon`, Model `Canon EOS 5D Mark III`, UniqueCameraModel `Canon EOS 5D Mark III`, Software ``
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 8000], [1, 3200], [10, 8000], [10, 4000], [1, 400], [1, 250], [10, 2000], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (3): EF35mm f/1.4L II USM; TAMRON SP 35mm F/1.8 Di VC USD F012; TAMRON SP 45mm F/1.8 Di VC USD F013
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['40']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `canon_eos_5d_mark_iii-native`: pins 5796x3870 (native sensor geometry)

Base `--camera-profile=canon_eos_5d_mark_iii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
