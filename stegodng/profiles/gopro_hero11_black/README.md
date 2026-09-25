# GoPro HERO11 Black
Profile slug: `gopro_hero11_black`  
EXIF Make/Model: `GoPro` / `HERO11 Black`
Native geometry: 5568x4872 max decoded-RAW dims across the model's samples (incl. masked margins)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `GoPro Hero 11 Black/6250773970.gpr`
Files seen: 2 (GoPro Hero 11 Black/6250773970.gpr, GoPro Hero 11 Black/9241827675.gpr)
Software strings observed: H22.01.01.09.23
Lenses observed: none
ISO observed: 120, 141
Exposure observed: 1/240 s, 1/877 s
F-number observed: F2.5
Focal length observed: 2.7 mm
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "GoPro"
- IFD0 Model: "HERO11 Black"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "GoPro HERO11 Black"
- IFD0 ColorMatrix1: [[18331, 10000], [-8166, 10000], [-2478, 10000], [1391, 10000], [8961, 10000], [-367, 10000], [822, 10000], [662, 10000], [2597, 10000]]
- IFD0 ColorMatrix2: [[10344, 10000], [-4210, 10000], [-620, 10000], [-2315, 10000], [10625, 10000], [1948, 10000], [93, 10000], [1058, 10000], [5541, 10000]]
- IFD0 CalibrationIlluminant1: 3
- IFD0 CalibrationIlluminant2: 23
- IFD0 AsShotNeutral: [518219, 1000000, 1000000, 1000000, 530021, 1000000]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "C3471325008935"
- IFD0 ShadowScale: [1, 1]
- IFD0 BestQualityScale: [1, 1]
- IFD0 AntiAliasStrength: [100, 100]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [3072, 256, 3072, 256, 3072, 256, 3072, 256]
- raw WhiteLevel: 4095
- raw DefaultScale: [5568, 5568, 4872, 4872]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [5568, 1, 4872, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 4872, 5568]
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 3
- raw CalibrationIlluminant2: 23
- raw DNGVersion: {"hex": "01030000"}
- raw UniqueCameraModel: "GoPro HERO11 Black"
- raw _shape: [4872, 5568]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `GoPro`, Model `HERO11 Black`, UniqueCameraModel `HERO11 Black`, Software `H22.01.01.09.23`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 49163 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 877], [10, 8000], [10, 4000], [1, 240], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 120, 125, 141, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): HERO11 Black built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['C34']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `gopro_hero11_black-native`: pins 5568x4872 (native sensor geometry)

Base `--camera-profile=gopro_hero11_black` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
