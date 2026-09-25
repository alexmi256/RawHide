# Apple iPhone 7
Profile slug: `apple_iphone_7`  
EXIF Make/Model: `Apple` / `iPhone 7`
Native geometry: 4032x3024 most common decoded dims across 1 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `iPhone 7/6171790209.dng`
Files seen: 1 (iPhone 7/6171790209.dng)
Software strings observed: ProCam 8.0
Lenses observed: iPhone 7 back camera 3.99mm f/1.8
ISO observed: 320
Exposure observed: 1/15 s
F-number observed: F1.8
Focal length observed: 4.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Apple"
- IFD0 Model: "iPhone 7"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "iPhone9,3 back camera"
- IFD0 ColorMatrix1: [[1071463104, 1073741824], [-406720480, 1073741824], [-165394560, 1073741824], [-497395424, 1073741824], [1525636864, 1073741824], [286942400, 1073741824], [-48
- IFD0 ColorMatrix2: [[748492544, 1073741824], [-241942400, 1073741824], [-61580424, 1073741824], [-505051872, 1073741824], [1308884864, 1073741824], [226785424, 1073741824], [-1083
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [589076672, 1073741824, 1073741824, 1073741824, 492999264, 1073741824]
- IFD0 BaselineExposure: [-257883712, 1073741824]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: 528
- raw WhiteLevel: 4095
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw OpcodeList3: {"hex": "0000000100000003010300000000000000000038400001cd7dd7034dc015b7d346a4da334034a493773e837cc03b8f5346bf0d3940290156acfd271c3fe00000000000003fe000000000000
- raw NewSubfileType: 0
- raw _shape: [3024, 4032]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Apple`, Model `iPhone 7`, UniqueCameraModel `iPhone 7`, Software `ProCam 8.0`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [1, 15], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): iPhone 7 back camera 3.99mm f/1.8
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `apple_iphone_7-native`: pins 4032x3024 (native sensor geometry)

Base `--camera-profile=apple_iphone_7` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
