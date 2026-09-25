# DJI FC3170 (drone camera unit)
Profile slug: `dji_fc3170`  
EXIF Make/Model: `DJI` / `FC3170`
Native geometry: 4000x3000 most common decoded dims across 2 sample(s) (also seen 8000x6000)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Mavic Air 2/0641717700.dng`
Files seen: 2 (DJI Mavic Air 2/0641717700.dng, DJI Mavic Air 2/3184801385.dng)
Software strings observed: 10.00.12.16
Lenses observed: none
ISO observed: 100
Exposure observed: 1/1250 s, 1/180 s
F-number observed: F2.8
Focal length observed: 4.5 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "FC3170"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "DJI FC3170"
- IFD0 ColorMatrix1: [[12400, 10000], [-8024, 10000], [2902, 10000], [-1185, 10000], [7988, 10000], [3824, 10000], [381, 10000], [416, 10000], [5642, 10000]]
- IFD0 ColorMatrix2: [[8157, 10000], [-2211, 10000], [-505, 10000], [-4010, 10000], [12314, 10000], [1881, 10000], [-492, 10000], [1794, 10000], [5008, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 475, 256, 256, 256, 434]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "1TCLH1403BJBJ6"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [4096, 1, 4096, 1, 4096, 1, 4096, 1]
- raw WhiteLevel: 65472
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [4000, 1, 3000, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3000, 4000]
- raw OpcodeList3: {"bytes_len": 12564, "sha1_prefix": "f42054d25de77300", "hex_prefix": "000000020000000901030000000000000000304c000000000000000000000bb8"}
- raw NewSubfileType: 0
- raw _shape: [3000, 4000]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `FC3170`, UniqueCameraModel `FC3170`, Software `10.00.12.16`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4100 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [10, 8000], [10, 4000], [10, 2000], [1, 180], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): FC3170 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1TC']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_fc3170-native`: pins 4000x3000 (native sensor geometry)

Base `--camera-profile=dji_fc3170` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
