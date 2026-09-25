# Skydio 2+
Profile slug: `skydio_2`  
EXIF Make/Model: `Skydio` / `2+`
Native geometry: 4056x3040 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Skydio 2+/0801020952.dng`
Files seen: 2 (Skydio 2+/0801020952.dng, Skydio 2+/6405207617.dng)
Software strings observed: 4fcf055b88714bb0b4f07a7bdfefd41f
Lenses observed: none
ISO observed: 100, 101
Exposure observed: 0.00092433 s, 0.0104167 s
F-number observed: F2.2
Focal length observed: 4.7 mm
Serial tags present: Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Harvested DNG calibration
- IFD0 Make: "Skydio"
- IFD0 Model: "2+"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "Skydio 2+"
- IFD0 ColorMatrix1: [[11078, 10000], [-5920, 10000], [782, 10000], [-1475, 10000], [8694, 10000], [3306, 10000], [153, 10000], [764, 10000], [5594, 10000]]
- IFD0 ColorMatrix2: [[9817, 10000], [-3638, 10000], [-750, 10000], [-2882, 10000], [10852, 10000], [2335, 10000], [-507, 10000], [1617, 10000], [5254, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 23
- IFD0 AsShotNeutral: [488550, 1000000, 1000000, 1000000, 604843, 1000000]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [65536, 256, 65536, 256, 65536, 256, 65536, 256]
- raw WhiteLevel: 4095
- raw DefaultScale: [4056, 4056, 3040, 3040]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [4056, 1, 3040, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3040, 4056]
- raw NewSubfileType: 0
- raw _shape: [3040, 4056]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Skydio`, Model `2+`, UniqueCameraModel `2+`, Software `4fcf055b88714bb0b4f07a7bdfefd41f`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1048816 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[9, 10000], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [104, 10000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 101, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 2+ built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `skydio_2-native`: pins 4056x3040 (native sensor geometry)

Base `--camera-profile=skydio_2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
