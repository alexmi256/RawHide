# Samsung SM-G965U
Profile slug: `samsung_sm_g965u`  
EXIF Make/Model: `samsung` / `SM-G965U`
Native geometry: 4032x3024 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Samsung Galaxy S9+/6679214842.dng`
Files seen: 2 (Samsung Galaxy S9+/6679214842.dng, Samsung Galaxy S9+/8674951755.dng)
Software strings observed: G965USQU1ARBG
Lenses observed: none
ISO observed: 160, 50
Exposure observed: 0.0003333 s, 1/50 s
F-number observed: F1.5, F2.4
Focal length observed: 4.3 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "samsung"
- IFD0 Model: "SM-G965U"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "SM-G965U"
- IFD0 ColorMatrix1: [[741, 1024], [-158, 1024], [-115, 1024], [-577, 1024], [1488, 1024], [77, 1024], [-159, 1024], [327, 1024], [424, 1024]]
- IFD0 ColorMatrix2: [[1362, 1024], [-631, 1024], [-162, 1024], [-442, 1024], [1483, 1024], [73, 1024], [-55, 1024], [219, 1024], [555, 1024]]
- IFD0 CalibrationIlluminant1: 21
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [249, 512, 1, 1, 317, 512]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [0, 0, 0, 0]
- raw WhiteLevel: 1023
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 0]
- raw DefaultCropSize: [4032, 3024]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01000201"}
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 21
- raw CalibrationIlluminant2: 17
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "SM-G965U"
- raw _shape: [3024, 4032]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `samsung`, Model `SM-G965U`, UniqueCameraModel `SM-G965U`, Software `G965USQU1ARBG`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[3, 10000], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[150, 100], [170, 100], [200, 100], [240, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): SM-G965U built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `samsung_sm_g965u-native`: pins 4032x3024 (native sensor geometry)

Base `--camera-profile=samsung_sm_g965u` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
