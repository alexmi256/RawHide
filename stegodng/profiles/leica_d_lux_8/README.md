# Leica D-Lux 8
Profile slug: `leica_d_lux_8`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA D-Lux 8`
Native geometry: 4736x3552 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: Bayer (unidentified)  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica D-Lux 8/6949743966.dng`
Files seen: 2 (Leica D-Lux 8/6949743966.dng, Leica D-Lux 8/9824710861.dng)
Software strings observed: 1.00, 1.40
Lenses observed: DC VARIO-SUMMILUX 1:1.7-2.8/10.9-34 ASPH.
ISO observed: 200, 800
Exposure observed: 1/125 s, 1/640 s
F-number observed: F16, F2.8
Focal length observed: 20.4 mm, 34.0 mm
EXIF PixelDimensions observed: 4824 x 3568
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA D-Lux 8"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA D-Lux 8"
- IFD0 ColorMatrix1: [[9994, 10000], [-4900, 10000], [18, 10000], [-4363, 10000], [13152, 10000], [1279, 10000], [-328, 10000], [965, 10000], [5835, 10000]]
- IFD0 ColorMatrix2: [[8585, 10000], [-3127, 10000], [-833, 10000], [-4005, 10000], [12250, 10000], [1953, 10000], [-650, 10000], [1494, 10000], [4862, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1024, 2532, 1024, 1024, 1024, 2013]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "5901687"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [514, 513, 513, 514]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [4736, 3552]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "02010100"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "9203152e161801e907770d5a00000000"}
- raw ActiveArea: [0, 0, 3568, 4752]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033ff0013ea04197f4bf4419c4c84e887f3f2a0d86483d2752bf30647e6db30c40000000000000000000000000000000003ff0000
- raw NewSubfileType: 0
- raw _shape: [3568, 4824]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA D-Lux 8`, UniqueCameraModel `LEICA D-Lux 8`, Software `1.40`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 2056 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 640], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): DC VARIO-SUMMILUX 1:1.7-2.8/10.9-34 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['59']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_d_lux_8-native`: pins 4736x3552 (native sensor geometry)

Base `--camera-profile=leica_d_lux_8` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
