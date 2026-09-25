# Sigma fp
Profile slug: `sigma_fp`  
EXIF Make/Model: `SIGMA` / `SIGMA fp`
Native geometry: 6000x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma fp/5299184666.dng`
Files seen: 2 (Sigma fp/5299184666.dng, Sigma fp/8677332215.dng)
Software strings observed: SIGMA fp Ver.1.00.0.V77
Lenses observed: 45mm F2.8 DG DN | Contemporary 019
ISO observed: 100, 1250
Exposure observed: 1/100 s, 1/160 s
F-number observed: F11, F3.5
Focal length observed: 45.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber, Exif.Sigma.SerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "SIGMA"
- IFD0 Model: "SIGMA fp"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01040000"}
- IFD0 UniqueCameraModel: "SIGMA fp"
- IFD0 ColorMatrix1: [[14262, 10000], [-7315, 10000], [-4969, 10000], [-3330, 10000], [11711, 10000], [-604, 10000], [-750, 10000], [1639, 10000], [5884, 10000]]
- IFD0 ColorMatrix2: [[8038, 10000], [-1991, 10000], [-1698, 10000], [-4961, 10000], [11648, 10000], [631, 10000], [-1140, 10000], [1585, 10000], [3560, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 533, 512, 512, 256, 450]
- IFD0 BaselineExposure: [1024, 1024]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 CameraSerialNumber: "91405968"
- IFD0 LensInfo: [[450, 10], [450, 10], [28, 10], [28, 10]]
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1024, 1024, 1024, 1024]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [32, 21]
- raw DefaultCropSize: [6000, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw ActiveArea: [0, 0, 4042, 6064]
- raw OpcodeList3: {"hex": "00000001000000010104000000000000000000a4000000033fef184a44cdd4503f8768ffe7f364fd3f7bc5967ac7e4fd3f8490071a7cdc65000000000000000000000000000000003fef188
- raw NewSubfileType: 0
- raw _shape: [4042, 6064]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `SIGMA`, Model `SIGMA fp`, UniqueCameraModel `SIGMA fp`, Software `SIGMA fp Ver.1.00.0.V77`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4096 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 160], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 45mm F2.8 DG DN | Contemporary 019
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['91']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sigma_fp-native`: pins 6000x4000 (native sensor geometry)

Base `--camera-profile=sigma_fp` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
