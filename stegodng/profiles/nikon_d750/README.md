# Nikon D750
Profile slug: `nikon_d750`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON D750`
Native geometry: 6032x4032 most common decoded dims across 9 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Petzval 58/0084608808.dng`
Files seen: 9 (Lensbaby Sol 45/0081968229.nef, Lensbaby Sol 45/5482931407.nef, Nikon 28mm F1.4E ED/2147328785.nef, Nikon 28mm F1.4E ED/3304550251.nef, ...)
Software strings observed: Adobe Photoshop Lightroom 6.6.1 (Macintosh), Ver.1.00, Ver.1.10, Ver.1.12
Lenses observed: 0.0 mm f/0.0
ISO observed: 100, 200, 400, 4500
Exposure observed: 1/1000 s, 1/125 s, 1/200 s, 1/2000 s, 1/320 s, 1/500 s
F-number observed: F0, F1.4, F1.8, F2.8, F5.6
Focal length observed: 0.0 mm, 24.0 mm, 28.0 mm, 85.0 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "NIKON CORPORATION"
- IFD0 Model: "NIKON D750"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "Nikon D750"
- IFD0 ColorMatrix1: [[10019, 10000], [-4200, 10000], [-32, 10000], [-4773, 10000], [12481, 10000], [2572, 10000], [-643, 10000], [1409, 10000], [8486, 10000]]
- IFD0 ColorMatrix2: [[9020, 10000], [-2890, 10000], [-715, 10000], [-4535, 10000], [12436, 10000], [2348, 10000], [-934, 10000], [1919, 10000], [7086, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [454707, 1000000, 1000000, 1000000, 876712, 1000000]
- IFD0 BaselineExposure: [10, 100]
- IFD0 BaselineNoise: [60, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "3054876"
- IFD0 LensInfo: [[0, 10], [0, 10], [0, 10], [0, 10]]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [153600, 256, 153600, 256, 153600, 256, 153600, 256]
- raw WhiteLevel: 15520
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 1, 8, 1]
- raw DefaultCropSize: [6016, 1, 4016, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 4032, 6032]
- raw NewSubfileType: 0
- raw _shape: [4032, 6032]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON D750`, UniqueCameraModel `NIKON D750`, Software `Ver.1.12`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 648594 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [1, 1000], [10, 8000], [1, 500], [10, 4000], [1, 320], [1, 200], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 4500, 6400]
- Lens pool (1): 0.0 mm f/0.0
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_d750-native`: pins 6032x4032 (native sensor geometry)

Base `--camera-profile=nikon_d750` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
