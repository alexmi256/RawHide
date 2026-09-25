# DJI Pocket
Profile slug: `dji_pocket`  
EXIF Make/Model: `DJI` / `DJI Pocket`
Native geometry: 9216x6912 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Pocket 2/0466420889.dng`
Files seen: 2 (DJI Pocket 2/0466420889.dng, DJI Pocket 2/2543294557.dng)
Software strings observed: Adobe Photoshop Lightroom 10.0 Classic (Macintosh)
Lenses observed: 4.4 mm f/1.8
ISO observed: 100
Exposure observed: 1/160 s, 1/400 s
F-number observed: F1.8
Focal length observed: 4.4 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "DJI Pocket"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "DJI Pocket"
- IFD0 ColorMatrix1: [[18075, 10000], [-11133, 10000], [-2191, 10000], [-1176, 10000], [11601, 10000], [-870, 10000], [1013, 10000], [339, 10000], [6282, 10000]]
- IFD0 ColorMatrix2: [[8623, 10000], [-2403, 10000], [-1194, 10000], [-5669, 10000], [14882, 10000], [464, 10000], [-779, 10000], [1876, 10000], [5151, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [484103, 1000000, 1000000, 1000000, 620606, 1000000]
- IFD0 BaselineExposure: [0, 10000]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "3PYCH9N00A0399"
- IFD0 LensInfo: [[44000, 10000], [44000, 10000], [18, 10], [18, 10]]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1024, 1, 1024, 1, 1024, 1, 1024, 1]
- raw WhiteLevel: 16383
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [9216, 1, 6912, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 6912, 9216]
- raw OpcodeList3: {"bytes_len": 38388, "sha1_prefix": "14b01a50da882536", "hex_prefix": "0000000200000003010300000000000000000038400a9ee904e20fa1c02198b3"}
- raw NewSubfileType: 0
- raw _shape: [6912, 9216]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `DJI Pocket`, UniqueCameraModel `DJI Pocket`, Software `Adobe Photoshop Lightroom 10.0 Classic (Macintosh)`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4096 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 400], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 4.4 mm f/1.8
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['3PY']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_pocket-native`: pins 9216x6912 (native sensor geometry)

Base `--camera-profile=dji_pocket` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
