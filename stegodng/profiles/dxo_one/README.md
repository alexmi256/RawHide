# DxO ONE
Profile slug: `dxo_one`  
EXIF Make/Model: `DxO` / `DxO ONE`
Native geometry: 5544x3694 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DxO ONE real-world/0968522332.dng`
Files seen: 2 (DxO ONE real-world/0968522332.dng, DxO ONE real-world/5496068530.dng)
Software strings observed: V1.1003.0000 APP:1.1.5
Lenses observed: none
ISO observed: 100
Exposure observed: 1/320 s, 1/8000 s
F-number observed: F1.8
Focal length observed: 11.9 mm
EXIF PixelDimensions observed: 5632 x 3710
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DxO"
- IFD0 Model: "DxO ONE"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "DXO ONE"
- IFD0 ColorMatrix1: [[7366, 10000], [-3213, 10000], [380, 10000], [-3609, 10000], [11127, 10000], [2852, 10000], [-218, 10000], [694, 10000], [5821, 10000]]
- IFD0 ColorMatrix2: [[6596, 10000], [-2079, 10000], [-562, 10000], [-4782, 10000], [13016, 10000], [1933, 10000], [-970, 10000], [1581, 10000], [5181, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [471455, 1000000, 1000000, 1000000, 577878, 1000000]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "C01A1507005029"
- IFD0 ShadowScale: [1, 1]
- IFD0 MakerNoteSafety: 1
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [50944, 256, 50944, 256, 50944, 256, 50944, 256]
- raw WhiteLevel: 4094
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 2, 1]
- raw DefaultCropSize: [5540, 1, 3688, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [16, 88, 3710, 5632]
- raw NewSubfileType: 0
- raw _shape: [3710, 5632]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DxO`, Model `DxO ONE`, UniqueCameraModel `DxO ONE`, Software `V1.1003.0000 APP:1.1.5`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 815490 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 8000], [10, 8000], [10, 4000], [1, 320], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DxO ONE built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['C01']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dxo_one-native`: pins 5544x3694 (native sensor geometry)

Base `--camera-profile=dxo_one` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
