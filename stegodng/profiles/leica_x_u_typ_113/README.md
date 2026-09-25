# Leica X-U (Typ 113)
Profile slug: `leica_x_u_typ_113`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA X-U (Typ 113)`
Native geometry: 4928x3264 active area (harvested DefaultCropSize)  
Suggested bit depth: 12  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica X-U (Typ 113)/0878636919.dng`
Files seen: 2 (Leica X-U (Typ 113)/0878636919.dng, Leica X-U (Typ 113)/9581779005.dng)
Software strings observed: 1.0
Lenses observed: 23.0 mm f/1.7
ISO observed: 100
Exposure observed: 1/160 s
F-number observed: F3.5, F4
Focal length observed: 23.0 mm
EXIF PixelDimensions observed: 4928 x 3264
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA X-U (Typ 113)"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA X-U (Typ 113)"
- IFD0 ColorMatrix1: [[10702, 10000], [-3867, 10000], [-44, 10000], [-4003, 10000], [12850, 10000], [4350, 10000], [-384, 10000], [962, 10000], [8216, 10000]]
- IFD0 ColorMatrix2: [[7158, 10000], [-1911, 10000], [-606, 10000], [-3603, 10000], [10669, 10000], [2530, 10000], [-659, 10000], [1236, 10000], [5530, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 626, 512, 512, 256, 389]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 CameraSerialNumber: "000004950898"
- IFD0 LensInfo: [[23, 1], [23, 1], [17, 10], [17, 10]]
- IFD0 MakerNoteSafety: 1
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 12
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw WhiteLevel: 4095
- raw DefaultCropOrigin: [8, 7]
- raw DefaultCropSize: [4928, 3264]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [1, 1]
- raw RawDataUniqueID: {"hex": "f7020c2e170602df07728b4b00000000"}
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033ff0000000000000bfad9f7f3b556fbf3f71b323939205363f6c6c88a88882ec000000000000000000000000000000003feff7b
- raw NewSubfileType: 0
- raw _shape: [3278, 4944]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA X-U (Typ 113)`, UniqueCameraModel `LEICA X-U (Typ 113)`, Software `1.0`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [350, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 23.0 mm f/1.7
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['00']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_x_u_typ_113-native`: pins 4928x3264 (native sensor geometry)

Base `--camera-profile=leica_x_u_typ_113` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
