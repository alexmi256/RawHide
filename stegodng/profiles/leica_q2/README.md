# Leica Q2
Profile slug: `leica_q2`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA Q2`
Native geometry: 8368x5584 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: Bayer (unidentified)  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica Q2/4972014802.dng`
Files seen: 2 (Leica Q2/4972014802.dng, Leica Q2/8121588862.dng)
Software strings observed: 1.03
Lenses observed: 28.0 mm f/1.7
ISO observed: 100
Exposure observed: 1/160 s, 1/320 s
F-number observed: F6.3, F8
Focal length observed: 28.0 mm
EXIF PixelDimensions observed: 8424 x 5632
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA Q2"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA Q2"
- IFD0 ColorMatrix1: [[12587, 10000], [-5232, 10000], [-1496, 10000], [-3610, 10000], [10841, 10000], [277, 10000], [-911, 10000], [1674, 10000], [2070, 10000]]
- IFD0 ColorMatrix2: [[8389, 10000], [-3198, 10000], [-1019, 10000], [-3834, 10000], [10222, 10000], [661, 10000], [-1122, 10000], [1900, 10000], [3415, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 23
- IFD0 AsShotNeutral: [1024, 2018, 1024, 1024, 1024, 1575]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "5353090"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [512, 512, 512, 512]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [12, 24]
- raw DefaultCropSize: [8368, 5584]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01020001"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "eb001622121504e30782ae5100000000"}
- raw ActiveArea: [0, 0, 5632, 8392]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033feffce45efa4de0bfa8839249a16732bfb925ab63cbe7873fac68072d077e71000000000000000000000000000000003feff9d
- raw NewSubfileType: 0
- raw _shape: [5632, 8424]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA Q2`, UniqueCameraModel `LEICA Q2`, Software `1.03`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 2048 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 320], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 28.0 mm f/1.7
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['53']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_q2-native`: pins 8368x5584 (native sensor geometry)

Base `--camera-profile=leica_q2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
