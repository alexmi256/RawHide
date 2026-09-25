# Zeiss ZX1
Profile slug: `zeiss_zx1`  
EXIF Make/Model: `ZEISS` / `ZX1`
Native geometry: 7488x4992 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Zeiss ZX1/3385088369.dng`
Files seen: 2 (Zeiss ZX1/3385088369.dng, Zeiss ZX1/6189920865.dng)
Software strings observed: 1.3.1.20201013_1006
Lenses observed: Distagon 2/35 T*
ISO observed: 100, 250
Exposure observed: 0.0026835 s, 0.0166667 s
F-number observed: F2
Focal length observed: 35.0 mm
EXIF PixelDimensions observed: 7792 x 5008
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "ZEISS"
- IFD0 Model: "ZX1"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "ZEISS ZX1"
- IFD0 ColorMatrix1: [[171, 128], [-66, 128], [-17, 128], [-27, 128], [145, 128], [11, 128], [-6, 128], [14, 128], [42, 128]]
- IFD0 ColorMatrix2: [[128, 128], [-61, 128], [-12, 128], [-38, 128], [145, 128], [24, 128], [-4, 128], [14, 128], [95, 128]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [86, 128, 128, 128, 36, 128]
- IFD0 BaselineExposure: [0, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1024, 1024, 1024, 1024]
- raw WhiteLevel: 16383
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [7488, 4992]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [0, 256, 5008, 7760]
- raw OpcodeList3: {"hex": "00000000"}
- raw NewSubfileType: 0
- raw _shape: [5008, 7792]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `ZEISS`, Model `ZX1`, UniqueCameraModel `ZX1`, Software `1.3.1.20201013_1006`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4096 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [27, 10000], [10, 2000], [10, 1000], [167, 10000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Distagon 2/35 T*
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['10']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `zeiss_zx1-native`: pins 7488x4992 (native sensor geometry)

Base `--camera-profile=zeiss_zx1` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
