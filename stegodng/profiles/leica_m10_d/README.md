# Leica M10-D
Profile slug: `leica_m10_d`  
EXIF Make/Model: `Leica Camera AG` / `LEICA M10-D`
Native geometry: 5976x3984 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica M10-D/3753140315.dng`
Files seen: 2 (Leica M10-D/3753140315.dng, Leica M10-D/4614334053.dng)
Software strings observed: 2.6.5.1
Lenses observed: Summilux-M 1:1.4/28 ASPH.
ISO observed: 200, 500
Exposure observed: 1/250 s
F-number observed: F1.7, F3.4
Focal length observed: 28.0 mm
EXIF PixelDimensions observed: 5984 x 3992
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Leica Camera AG"
- IFD0 Model: "LEICA M10-D"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA M10-D"
- IFD0 ColorMatrix1: [[3666, 4096], [-1313, 4096], [202, 4096], [-2388, 4096], [6594, 4096], [-9, 4096], [-343, 4096], [1134, 4096], [3251, 4096]]
- IFD0 ColorMatrix2: [[3301, 4096], [-1140, 4096], [-248, 4096], [-2167, 4096], [5905, 4096], [226, 4096], [-383, 4096], [1230, 4096], [2608, 4096]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 537, 256, 256, 256, 329]
- IFD0 BaselineExposure: [0, 100]
- IFD0 AntiAliasStrength: [0, 1]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: 0
- raw WhiteLevel: 15000
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [5976, 3984]
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [0, 1]
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 17
- raw CalibrationIlluminant2: 21
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "LEICA M10-D"
- raw _shape: [3992, 5984]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Leica Camera AG`, Model `LEICA M10-D`, UniqueCameraModel `LEICA M10-D`, Software `2.6.5.1`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [340, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Summilux-M 1:1.4/28 ASPH.
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['53']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_m10_d-native`: pins 5976x3984 (native sensor geometry)

Base `--camera-profile=leica_m10_d` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
