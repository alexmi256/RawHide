# Leica TL2
Profile slug: `leica_tl2`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA TL2`
Native geometry: 6000x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica TL2/1643738655.dng`
Files seen: 2 (Leica TL2/1643738655.dng, Leica TL2/7496361913.dng)
Software strings observed: 1.0
Lenses observed: Summicron TL 1:2 23 ASPH.; Super-Vario-Elmar-TL  1:3.5-4.5 / 11-23 ASPH.
ISO observed: 100, 400
Exposure observed: 1/125 s, 1/640 s
F-number observed: F2, F5.6
Focal length observed: 17.7 mm, 23.0 mm
EXIF PixelDimensions observed: 6000 x 4000
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA TL2"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA TL2"
- IFD0 ColorMatrix1: [[7516, 10000], [-2443, 10000], [22, 10000], [-5508, 10000], [14751, 10000], [3673, 10000], [-914, 10000], [1800, 10000], [7771, 10000]]
- IFD0 ColorMatrix2: [[5485, 10000], [-1528, 10000], [-608, 10000], [-5060, 10000], [12524, 10000], [2125, 10000], [-1134, 10000], [2001, 10000], [5508, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 737, 512, 511, 256, 470]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 CameraSerialNumber: "000005224215"
- IFD0 LensInfo: [[11, 1], [23, 1], [36, 10], [45, 10]]
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [8, 7]
- raw DefaultCropSize: [6000, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [1, 1]
- raw RawDataUniqueID: {"hex": "600006260f0607e10717b74f00000000"}
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033fefdc9ce35eaccebf8344fe405b68aa3f95141f072d1e74bf86d058811fb8c2000000000000000000000000000000003fefdca
- raw NewSubfileType: 0
- raw _shape: [4014, 6016]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA TL2`, UniqueCameraModel `LEICA TL2`, Software `1.0`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 640], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): Summicron TL 1:2 23 ASPH.; Super-Vario-Elmar-TL  1:3.5-4.5 / 11-23 ASPH.
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['00']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_tl2-native`: pins 6000x4000 (native sensor geometry)

Base `--camera-profile=leica_tl2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
