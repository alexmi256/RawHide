# DJI FC4280 (drone camera unit)
Profile slug: `dji_fc4280`  
EXIF Make/Model: `DJI` / `FC4280`
Native geometry: 8192x5456 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Inspire 3/2301547988.dng`
Files seen: 2 (DJI Inspire 3/2301547988.dng, DJI Inspire 3/4717480184.dng)
Software strings observed: 10.00.15.01
Lenses observed: none
ISO observed: 100, 370
Exposure observed: 1/50 s, 1/800 s
F-number observed: F2.8, F3.5
Focal length observed: 18.0 mm, 35.0 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "FC4280"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "DJI FC4280 Inspire 3"
- IFD0 ColorMatrix1: [[14514, 10000], [-10043, 10000], [-1144, 10000], [-4312, 10000], [14834, 10000], [-274, 10000], [164, 10000], [-106, 10000], [8874, 10000]]
- IFD0 ColorMatrix2: [[7090, 10000], [-2655, 10000], [-556, 10000], [-6261, 10000], [14087, 10000], [1712, 10000], [224, 10000], [-991, 10000], [6572, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [4096, 10587, 4096, 4096, 4096, 7764]
- IFD0 BaselineExposure: [0, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "564BKBM1020GAY"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [4096, 1, 4096, 1, 4096, 1, 4096, 1]
- raw WhiteLevel: 65472
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [8192, 1, 5456, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 5456, 8192]
- raw OpcodeList3: {"bytes_len": 12564, "sha1_prefix": "875051c99caa4fb5", "hex_prefix": "000000020000000901030000000000000000304c000000000000000000001550"}
- raw NewSubfileType: 0
- raw _shape: [5456, 8192]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `FC4280`, UniqueCameraModel `FC4280`, Software `10.00.15.01`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4100 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 800], [10, 4000], [10, 2000], [10, 1000], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 370, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): FC4280 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['56']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_fc4280-native`: pins 8192x5456 (native sensor geometry)

Base `--camera-profile=dji_fc4280` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
