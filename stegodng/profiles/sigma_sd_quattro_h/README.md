# Sigma sd Quattro H
Profile slug: `sigma_sd_quattro_h`  
EXIF Make/Model: `SIGMA` / `sd Quattro H`
Native geometry: 6192x4128 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma sd Quattro H/1255722523.dng`
Files seen: 2 (Sigma sd Quattro H/1255722523.dng, Sigma sd Quattro H/4291410509.dng)
Software strings observed: SIGMA sd Quattro H ver1.1.0.0512
Lenses observed: 35mm F1.4 DG HSM | Art 012
ISO observed: 100
Exposure observed: 1/250 s, 1/320 s
F-number observed: F8
Focal length observed: 35.0 mm
EXIF PixelDimensions observed: 6192 x 4128
Serial tags present: Exif.Photo.BodySerialNumber, Exif.Sigma.SerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "SIGMA"
- IFD0 Model: "sd Quattro H"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "sd Quattro H"
- IFD0 ColorMatrix1: [[84159, 65536], [2806, 65536], [-22293, 65536], [31640, 65536], [43719, 65536], [-10506, 65536], [18966, 65536], [38470, 65536], [10660, 65536]]
- IFD0 ColorMatrix2: [[85018, 65536], [3005, 65536], [-23530, 65536], [19634, 65536], [51469, 65536], [-5867, 65536], [1893, 65536], [46059, 65536], [21413, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 15
- IFD0 AsShotNeutral: [65536, 67260, 65536, 68812, 65536, 68597]
- IFD0 BaselineExposure: [0, 1]
- IFD0 BaselineNoise: [18, 1]
- IFD0 BaselineSharpness: [22, 10]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 ShadowScale: [100, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: [12, 12, 12]
- raw SamplesPerPixel: 3
- raw PhotometricInterpretation: 34892
- raw BlackLevel: [0, 1, 0, 1, 0, 1]
- raw WhiteLevel: [4095, 4095, 4095]
- raw DefaultCropOrigin: [12, 20]
- raw DefaultCropSize: [6192, 4128]
- raw AntiAliasStrength: [1, 1]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [156, 220, 4324, 6436]
- raw NewSubfileType: 0
- raw _shape: [4480, 6656, 3]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `SIGMA`, Model `sd Quattro H`, UniqueCameraModel `sd Quattro H`, Software `SIGMA sd Quattro H ver1.1.0.0512`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 320], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 35mm F1.4 DG HSM | Art 012
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['91']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sigma_sd_quattro_h-native`: pins 6192x4128 (native sensor geometry)

Base `--camera-profile=sigma_sd_quattro_h` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
