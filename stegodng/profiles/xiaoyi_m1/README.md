# Xiaomi M1
Profile slug: `xiaoyi_m1`  
EXIF Make/Model: `XIAOYI` / `M1`
Native geometry: 5200x3902 active area (harvested DefaultCropSize)  
Suggested bit depth: 12  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `YI M1/2529203744.dng`
Files seen: 2 (YI M1/2529203744.dng, YI M1/4460018946.dng)
Software strings observed: Adobe Photoshop Lightroom 6.7 (Macintosh)
Lenses observed: XIAOYI 42.5mm F1.8
ISO observed: 200
Exposure observed: 1/250 s, 1/320 s
F-number observed: F1.8
Focal length observed: 43.0 mm
EXIF PixelDimensions observed: 5184 x 3888
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "XIAOYI"
- IFD0 Model: "M1"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01040000"}
- IFD0 UniqueCameraModel: "M1"
- IFD0 ColorMatrix1: [[10702, 10000], [-3867, 10000], [-44, 10000], [-4003, 10000], [12850, 10000], [4350, 10000], [-384, 10000], [962, 10000], [8216, 10000]]
- IFD0 ColorMatrix2: [[7158, 10000], [-1911, 10000], [-606, 10000], [-3603, 10000], [10669, 10000], [2530, 10000], [-659, 10000], [1236, 10000], [5530, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 592, 512, 510, 256, 435]
- IFD0 BaselineExposure: [0, 0]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 CameraSerialNumber: "00B607280043"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 12
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [256, 1, 256, 1, 256, 1, 256, 1]
- raw WhiteLevel: 4095
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 0]
- raw DefaultCropSize: [5200, 3902]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [0, 0]
- raw BestQualityScale: [1, 1]
- raw OpcodeList3: {"hex": "00000001000000010104000000000000000000a4000000033ff00000000000003f8c3acc6271ee4dbf900814be00cb683f783b3d458de893000000000000000000000000000000003ff0000
- raw NewSubfileType: 0
- raw _shape: [3902, 5200]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `XIAOYI`, Model `M1`, UniqueCameraModel `M1`, Software `Adobe Photoshop Lightroom 6.7 (Macintosh)`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4097 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 320], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): XIAOYI 42.5mm F1.8
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['00']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `xiaoyi_m1-native`: pins 5200x3902 (native sensor geometry)

Base `--camera-profile=xiaoyi_m1` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
