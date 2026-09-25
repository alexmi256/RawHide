# Camera Intelligence Caira
Profile slug: `caira`  
EXIF Make/Model: `Camera Intelligence` / `Caira`
Native geometry: 4096x2780 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Camera Intelligence Caira/IMG_0253.dng`
Files seen: 2 (Camera Intelligence Caira/IMG_0253.dng, Camera Intelligence Caira/IMG_0475.dng)
Software strings observed: none
Lenses observed: 8.0-25.0 mm f/4.0-22.6; 20.0 mm f/1.4
ISO observed: 400
Exposure observed: 1/159 s, 1/7353 s
F-number observed: F1.4, F4
Focal length observed: 20.1 mm, 23.5 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Camera Intelligence"
- IFD0 Model: "Caira"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "Caira Camera"
- IFD0 ColorMatrix1: [[12006, 10000], [-5066, 10000], [-610, 10000], [-1779, 10000], [10867, 10000], [1028, 10000], [-295, 10000], [1093, 10000], [5098, 10000]]
- IFD0 ColorMatrix2: [[11054, 10000], [-3883, 10000], [-1136, 10000], [-2122, 10000], [11305, 10000], [898, 10000], [-637, 10000], [1452, 10000], [4955, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [527988, 1000000, 1000000, 1000000, 571371, 1000000]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 LensInfo: [[200, 10], [200, 10], [14, 10], [160, 10]]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [51200, 256]
- raw WhiteLevel: 4095
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [0, 0, 0, 0]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01000201"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw NewSubfileType: 0
- raw _shape: [2780, 4096]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Camera Intelligence`, Model `Caira`, UniqueCameraModel `Caira`, Software ``
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 819388 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 7353], [10, 8000], [10, 4000], [10, 2000], [1, 159], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): 8.0-25.0 mm f/4.0-22.6; 20.0 mm f/1.4
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `caira-native`: pins 4096x2780 (native sensor geometry)

Base `--camera-profile=caira` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
