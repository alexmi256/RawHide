# Leica M10-R
Profile slug: `leica_m10_r`  
EXIF Make/Model: `Leica Camera AG` / `LEICA M10-R`
Native geometry: 7864x5200 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica APO-Summicron-M 35mm F2 ASPH/1973166827.dng`
Files seen: 6 (Leica APO-Summicron-M 35mm F2 ASPH/1973166827.dng, Leica APO-Summicron-M 35mm F2 ASPH/9856493160.dng, Leica M10-R 2/7233386414.dng, Leica M10-R 2/7316945536.dng, ...)
Software strings observed: 1.20.11.8, 10.20.23.49, 20.20.47.37
Lenses observed: Apo-Summicron-M 1:2/35 ASPH.; Apo-Summicron-M 1:2/50 ASPH.; Summilux-M 1:1.4/35 ASPH.
ISO observed: 100, 125, 12500
Exposure observed: 1/125 s, 1/1500 s, 1/360 s, 1/45 s, 1/90 s
F-number observed: F1.4, F2.4, F4
Focal length observed: 35.0 mm, 50.0 mm
EXIF PixelDimensions observed: 7872 x 5208
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Leica Camera AG"
- IFD0 Model: "LEICA M10-R"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA M10-R"
- IFD0 ColorMatrix1: [[2918, 4096], [-1024, 4096], [-178, 4096], [-2350, 4096], [6358, 4096], [1473, 4096], [-449, 4096], [1197, 4096], [3172, 4096]]
- IFD0 ColorMatrix2: [[1998, 4096], [-527, 4096], [-199, 4096], [-2392, 4096], [5612, 4096], [904, 4096], [-739, 4096], [1380, 4096], [2151, 4096]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 873, 256, 256, 256, 381]
- IFD0 BaselineExposure: [0, 100]
- IFD0 AntiAliasStrength: [0, 1]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: 0
- raw WhiteLevel: 15000
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [7864, 5200]
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw AntiAliasStrength: [0, 1]
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 17
- raw CalibrationIlluminant2: 21
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "LEICA M10-R"
- raw _shape: [5208, 7872]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Leica Camera AG`, Model `LEICA M10-R`, UniqueCameraModel `LEICA M10-R`, Software `20.20.47.37`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1500], [10, 8000], [10, 4000], [1, 360], [10, 2000], [1, 125], [10, 1000], [1, 90], [10, 500], [1, 45], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [240, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 12500]
- Lens pool (3): Apo-Summicron-M 1:2/35 ASPH.; Apo-Summicron-M 1:2/50 ASPH.; Summilux-M 1:1.4/35 ASPH.
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['55']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_m10_r-native`: pins 7864x5200 (native sensor geometry)

Base `--camera-profile=leica_m10_r` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
