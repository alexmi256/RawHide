# Samsung SM-G975U1
Profile slug: `samsung_sm_g975u1`  
EXIF Make/Model: `samsung` / `SM-G975U1`
Native geometry: 4016x3008 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Samsung Galaxy S10+/0726557120.dng`
Files seen: 2 (Samsung Galaxy S10+/0726557120.dng, Samsung Galaxy S10+/1624969965.dng)
Software strings observed: G975U1UEU1ASD3
Lenses observed: none
ISO observed: 160, 50
Exposure observed: 0.00115207 s, 0.0166667 s
F-number observed: F1.5
Focal length observed: 4.3 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "samsung"
- IFD0 Model: "SM-G975U1"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "SM-G975U1"
- IFD0 ColorMatrix1: [[698, 1024], [-90, 1024], [-120, 1024], [-603, 1024], [1517, 1024], [73, 1024], [-206, 1024], [441, 1024], [482, 1024]]
- IFD0 ColorMatrix2: [[1395, 1024], [-636, 1024], [-181, 1024], [-462, 1024], [1542, 1024], [-29, 1024], [-61, 1024], [314, 1024], [572, 1024]]
- IFD0 CalibrationIlluminant1: 20
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [545, 1024, 1, 1, 691, 1024]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [0, 0, 0, 0]
- raw WhiteLevel: 1023
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [4016, 3008]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "01000201"}
- raw ActiveArea: [0, 0, 3024, 4032]
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 20
- raw CalibrationIlluminant2: 17
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "SM-G975U1"
- raw _shape: [3024, 4032]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `samsung`, Model `SM-G975U1`, UniqueCameraModel `SM-G975U1`, Software `G975U1UEU1ASD3`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[12, 10000], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [167, 10000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[150, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): SM-G975U1 built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `samsung_sm_g975u1-native`: pins 4016x3008 (native sensor geometry)

Base `--camera-profile=samsung_sm_g975u1` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
