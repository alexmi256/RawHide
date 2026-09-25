# Leica CL
Profile slug: `leica_cl`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA CL`
Native geometry: 6000x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: Bayer (unidentified)  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica CL/1294287973.dng`
Files seen: 2 (Leica CL/1294287973.dng, Leica CL/1800461926.dng)
Software strings observed: 1.00
Lenses observed: ELMARIT-TL 1:2.8/18 ASPH.
ISO observed: 100
Exposure observed: 1/200 s, 1/80 s
F-number observed: F4, F7.1
Focal length observed: 18.0 mm
EXIF PixelDimensions observed: 6120 x 4016
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA CL"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA CL"
- IFD0 ColorMatrix1: [[9760, 10000], [-3850, 10000], [120, 10000], [-5230, 10000], [14540, 10000], [3480, 10000], [-950, 10000], [1860, 10000], [7230, 10000]]
- IFD0 ColorMatrix2: [[6970, 10000], [-2250, 10000], [-790, 10000], [-4820, 10000], [12390, 10000], [2010, 10000], [-1490, 10000], [2320, 10000], [4760, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1024, 2680, 1024, 1024, 1024, 1761]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "5246057"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [511, 511, 511, 511]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [6000, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "be003926170e01e107690c5000000000"}
- raw ActiveArea: [0, 0, 4016, 6016]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033ff003268cbca251bfb52fb93cfc096f3f81b7f7dd570d40bf6324478da81d16000000000000000000000000000000003feffe7
- raw NewSubfileType: 0
- raw _shape: [4016, 6120]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA CL`, UniqueCameraModel `LEICA CL`, Software `1.00`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 2044 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 200], [10, 2000], [10, 1000], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): ELMARIT-TL 1:2.8/18 ASPH.
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['52']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_cl-native`: pins 6000x4000 (native sensor geometry)

Base `--camera-profile=leica_cl` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
