# DJI FC8284 (drone camera unit)
Profile slug: `dji_fc8284`  
EXIF Make/Model: `DJI` / `FC8284`
Native geometry: 8064x6048 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Air 3/0817483246.dng`
Files seen: 2 (DJI Air 3/0817483246.dng, DJI Air 3/8037620653.dng)
Software strings observed: 10.06.00.11
Lenses observed: none
ISO observed: 110, 180
Exposure observed: 1/500 s, 1/725 s
F-number observed: F2.8
Focal length observed: 19.4 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "FC8284"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "DJI FC8284 Air3"
- IFD0 ColorMatrix1: [[12359, 10000], [-5159, 10000], [-664, 10000], [-6537, 10000], [16586, 10000], [1670, 10000], [111, 10000], [737, 10000], [8550, 10000]]
- IFD0 ColorMatrix2: [[7107, 10000], [-1360, 10000], [-1124, 10000], [-5814, 10000], [13880, 10000], [1512, 10000], [-786, 10000], [1951, 10000], [5170, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [4096, 8464, 4096, 4096, 4096, 6406]
- IFD0 BaselineExposure: [6, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "6GVFL5211102FN"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [4096, 1, 4096, 1, 4096, 1, 4096, 1]
- raw WhiteLevel: 65472
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [8064, 1, 6048, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 6048, 8064]
- raw OpcodeList3: {"bytes_len": 12564, "sha1_prefix": "4ea13c53244cddf8", "hex_prefix": "000000020000000901030000000000000000304c0000000000000000000017a0"}
- raw NewSubfileType: 0
- raw _shape: [6048, 8064]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `FC8284`, UniqueCameraModel `FC8284`, Software `10.06.00.11`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4100 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 725], [1, 500], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 110, 125, 160, 180, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): FC8284 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['6GV']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_fc8284-native`: pins 8064x6048 (native sensor geometry)

Base `--camera-profile=dji_fc8284` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
