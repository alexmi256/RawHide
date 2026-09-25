# DJI FC3682 (drone camera unit)
Profile slug: `dji_fc3682`  
EXIF Make/Model: `DJI` / `FC3682`
Native geometry: 4000x3000 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Mini 3/3052230787.dng`
Files seen: 2 (DJI Mini 3/3052230787.dng, DJI Mini 3/8173390271.dng)
Software strings observed: v01.51.0047
Lenses observed: none
ISO observed: 100
Exposure observed: 1/120 s, 1/60 s
F-number observed: F1.7
Focal length observed: 6.7 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "FC3682"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "FC3682"
- IFD0 ColorMatrix1: [[17412, 10000], [-11581, 10000], [425, 10000], [-2794, 10000], [11486, 10000], [4449, 10000], [216, 10000], [421, 10000], [9532, 10000]]
- IFD0 ColorMatrix2: [[8248, 10000], [-2359, 10000], [-1315, 10000], [-7662, 10000], [15546, 10000], [1595, 10000], [-2199, 10000], [2908, 10000], [5506, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [412196, 1000000, 1000000, 1000000, 708527, 1000000]
- IFD0 BaselineExposure: [0, 10000]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "53HQK9L0M50GS4"
- IFD0 LensInfo: [[207000, 10000], [207000, 10000], [0, 0], [0, 0]]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [256, 1, 256, 1, 256, 1, 256, 1]
- raw WhiteLevel: 16383
- raw DefaultScale: [20000, 10000, 20000, 10000]
- raw DefaultCropOrigin: [1000, 1, 750, 1]
- raw DefaultCropSize: [2000, 1, 1500, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3000, 4000]
- raw OpcodeList3: {"bytes_len": 38388, "sha1_prefix": "587c0b0f7bf68cab", "hex_prefix": "00000002000000030103000000000000000000384004e9752977c88e400df7f9"}
- raw NewSubfileType: 0
- raw _shape: [3000, 4000]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `FC3682`, UniqueCameraModel `FC3682`, Software `v01.51.0047`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1024 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 120], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): FC3682 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['53']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_fc3682-native`: pins 4000x3000 (native sensor geometry)

Base `--camera-profile=dji_fc3682` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
