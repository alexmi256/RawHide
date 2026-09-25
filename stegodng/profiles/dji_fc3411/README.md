# DJI FC3411 (drone camera unit)
Profile slug: `dji_fc3411`  
EXIF Make/Model: `DJI` / `FC3411`
Native geometry: 5472x3648 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Air 2S/2400589387.dng`
Files seen: 2 (DJI Air 2S/2400589387.dng, DJI Air 2S/4251598811.dng)
Software strings observed: 10.00.29.10
Lenses observed: none
ISO observed: 100
Exposure observed: 1/100 s, 1/25 s
F-number observed: F2.8
Focal length observed: 8.4 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "FC3411"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "DJI FC3411"
- IFD0 ColorMatrix1: [[14387, 10000], [-8322, 10000], [-1922, 10000], [-3058, 10000], [12714, 10000], [1732, 10000], [141, 10000], [17, 10000], [7174, 10000]]
- IFD0 ColorMatrix2: [[8531, 10000], [-3148, 10000], [-888, 10000], [-4071, 10000], [12492, 10000], [1265, 10000], [-209, 10000], [486, 10000], [5114, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 587, 256, 256, 256, 483]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "42UQJ2L13A00QM"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [4096, 1, 4096, 1, 4096, 1, 4096, 1]
- raw WhiteLevel: 65535
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [4, 1, 4, 1]
- raw DefaultCropSize: [5464, 1, 3640, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 96, 3648, 5568]
- raw OpcodeList3: {"bytes_len": 12564, "sha1_prefix": "21c93ee23013f928", "hex_prefix": "000000020000000901030000000000000000304c000000000000000000000e40"}
- raw NewSubfileType: 0
- raw _shape: [3648, 5568]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `FC3411`, UniqueCameraModel `FC3411`, Software `10.00.29.10`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4096 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 100], [10, 500], [10, 250], [1, 25], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): FC3411 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['42']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_fc3411-native`: pins 5472x3648 (native sensor geometry)

Base `--camera-profile=dji_fc3411` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
