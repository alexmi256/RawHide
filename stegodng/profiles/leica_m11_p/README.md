# Leica M11-P
Profile slug: `leica_m11_p`  
EXIF Make/Model: `Leica Camera AG` / `LEICA M11-P`
Native geometry: 9528x6328 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica 35mm F1.2 Noctilux/1532202451.dng`
Files seen: 2 (Leica 35mm F1.2 Noctilux/1532202451.dng, Leica 35mm F1.2 Noctilux/1648299562.dng)
Software strings observed: 2.6.0
Lenses observed: Summilux-M 1:1.4/35
ISO observed: 2000, 64
Exposure observed: 1/30 s, 1/90 s
F-number observed: none
Focal length observed: 35.0 mm
EXIF PixelDimensions observed: 9536 x 6336
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Leica Camera AG"
- IFD0 Model: "LEICA M11-P"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA M11-P"
- IFD0 ColorMatrix1: [[2358, 4096], [-546, 4096], [-66, 4096], [-2488, 4096], [6300, 4096], [1785, 4096], [-403, 4096], [797, 4096], [3504, 4096]]
- IFD0 ColorMatrix2: [[1700, 4096], [-326, 4096], [-200, 4096], [-2354, 4096], [5409, 4096], [974, 4096], [-612, 4096], [976, 4096], [2276, 4096]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 585, 256, 256, 256, 666]
- IFD0 BaselineExposure: [0, 100]
- IFD0 AntiAliasStrength: [0, 1]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: 1023
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [9528, 6328]
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [0, 1]
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 17
- raw CalibrationIlluminant2: 21
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "LEICA M11-P"
- raw _shape: [6336, 9536]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Leica Camera AG`, Model `LEICA M11-P`, UniqueCameraModel `LEICA M11-P`, Software `2.6.0`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [1, 90], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 3200, 6400]
- Lens pool (1): Summilux-M 1:1.4/35
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['58']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_m11_p-native`: pins 9528x6328 (native sensor geometry)

Base `--camera-profile=leica_m11_p` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
