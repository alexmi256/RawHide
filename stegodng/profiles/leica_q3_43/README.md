# Leica Q3 43
Profile slug: `leica_q3_43`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA Q3 43`
Native geometry: 9520x6336 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica Q3 43/1416153915.dng`
Files seen: 2 (Leica Q3 43/1416153915.dng, Leica Q3 43/4030894411.dng)
Software strings observed: 2.0.4
Lenses observed: APO-SUMMICRON 1:2/43 ASPH.
ISO observed: 100, 160
Exposure observed: 1/60 s, 1/640 s
F-number observed: F2, F5.6
Focal length observed: 43.0 mm
EXIF PixelDimensions observed: 9536 x 6344
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA Q3 43"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA Q3 43"
- IFD0 ColorMatrix1: [[15406, 10000], [-6866, 10000], [-154, 10000], [-3920, 10000], [13782, 10000], [2304, 10000], [-486, 10000], [1393, 10000], [6457, 10000]]
- IFD0 ColorMatrix2: [[10421, 10000], [-3579, 10000], [-991, 10000], [-3517, 10000], [11355, 10000], [1715, 10000], [-888, 10000], [1752, 10000], [4356, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1024, 2475, 1024, 1024, 1024, 1653]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "5971647"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [512, 512, 512, 512]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [9520, 6336]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "cc03320f0e1d08e807bf1e5b00000000"}
- raw ActiveArea: [0, 0, 6344, 9536]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033fefd4bca5e266563f781249b1ccca22bfbabf2dbdf4aab13f992561a997ccdc000000000000000000000000000000003fefd23
- raw NewSubfileType: 0
- raw _shape: [6344, 9536]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA Q3 43`, UniqueCameraModel `LEICA Q3 43`, Software `2.0.4`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 2048 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 640], [10, 4000], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): APO-SUMMICRON 1:2/43 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['59']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_q3_43-native`: pins 9520x6336 (native sensor geometry)

Base `--camera-profile=leica_q3_43` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
