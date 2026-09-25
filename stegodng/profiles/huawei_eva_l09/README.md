# Huawei EVA-L09
Profile slug: `huawei_eva_l09`  
EXIF Make/Model: `HUAWEI` / `EVA-L09`
Native geometry: 3952x2960 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Huawei P9 real-world/2460970096.dng`
Files seen: 2 (Huawei P9 real-world/2460970096.dng, Huawei P9 real-world/6584105446.dng)
Software strings observed: HUAWEI/EVA-L09/HWEVA:6.0/HUAWEIEVA-L09/C900B122:user/release-keys
Lenses observed: none
ISO observed: 50
Exposure observed: 1/2200 s
F-number observed: F2.2
Focal length observed: 4.5 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "HUAWEI"
- IFD0 Model: "EVA-L09"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "EVA-L09-HUAWEI-HUAWEI"
- IFD0 ColorMatrix1: [[1094, 1024], [-306, 1024], [-146, 1024], [-442, 1024], [1388, 1024], [52, 1024], [-104, 1024], [250, 1024], [600, 1024]]
- IFD0 ColorMatrix2: [[2263, 1024], [-1364, 1024], [-145, 1024], [-194, 1024], [1257, 1024], [-56, 1024], [-24, 1024], [187, 1024], [618, 1024]]
- IFD0 CalibrationIlluminant1: 21
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [1092, 2495, 1092, 1092, 1092, 1727]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [0, 0, 0, 0]
- raw WhiteLevel: 1023
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [3952, 2960]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw ActiveArea: [0, 0, 2976, 3968]
- raw OpcodeList3: {"hex": "00000000"}
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 21
- raw CalibrationIlluminant2: 17
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "EVA-L09-HUAWEI-HUAWEI"
- raw _shape: [2976, 3968]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `HUAWEI`, Model `EVA-L09`, UniqueCameraModel `EVA-L09`, Software `HUAWEI/EVA-L09/HWEVA:6.0/HUAWEIEVA-L09/C900B122:user/release-keys`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2200], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): EVA-L09 built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `huawei_eva_l09-native`: pins 3952x2960 (native sensor geometry)

Base `--camera-profile=huawei_eva_l09` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
