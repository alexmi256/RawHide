# Vivo V2114
Profile slug: `vivo_v2114`  
EXIF Make/Model: `vivo` / `V2114`
Native geometry: 4064x3044 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Vivo X70 Pro+/5302803402.dng`
Files seen: 2 (Vivo X70 Pro+/5302803402.dng, Vivo X70 Pro+/7987518740.dng)
Software strings observed: vivo/2114i/2114:11/RP1A.200720.012/compiler0919003023:user/release-keys
Lenses observed: none
ISO observed: 289, 413
Exposure observed: 1/20 s, 1/50 s
F-number observed: F1.6
Focal length observed: 6.5 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "vivo"
- IFD0 Model: "V2114"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "V2114-vivo-vivo"
- IFD0 ColorMatrix1: [[114, 128], [-39, 128], [-16, 128], [-58, 128], [169, 128], [13, 128], [-19, 128], [46, 128], [65, 128]]
- IFD0 ColorMatrix2: [[162, 128], [-83, 128], [-17, 128], [-63, 128], [188, 128], [26, 128], [-3, 128], [22, 128], [109, 128]]
- IFD0 CalibrationIlluminant1: 21
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [678, 1024, 1024, 1024, 570, 1024]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [6400, 100, 6400, 100, 6300, 100, 6300, 100]
- raw WhiteLevel: 1023
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [4064, 3044]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw ActiveArea: [0, 0, 3060, 4080]
- raw OpcodeList3: {"hex": "0000000100000001010300000000000100000044000000013ff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003fe03f6
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 21
- raw CalibrationIlluminant2: 17
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "V2114-vivo-vivo"
- raw _shape: [3060, 4080]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `vivo`, Model `V2114`, UniqueCameraModel `V2114`, Software `vivo/2114i/2114:11/RP1A.200720.012/compiler0919003023:user/release-keys`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 409994 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [1, 50], [10, 250], [1, 20], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[160, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 289, 320, 400, 413, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): V2114 built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `vivo_v2114-native`: pins 4064x3044 (native sensor geometry)

Base `--camera-profile=vivo_v2114` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
