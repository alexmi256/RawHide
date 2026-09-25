# Apple iPhone 18 Pro Max
Profile slug: `apple_iphone_18_pro_max`  
EXIF Make/Model: `Apple` / `iPhone 18 Pro Max`
Native geometry: 8064x6048 max decoded-RAW dims across the model's samples (incl. masked margins)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `iPhone 18 Pro and Pro Max/IMG_4586.DNG`
Files seen: 2 (iPhone 18 Pro and Pro Max/IMG_4586.DNG, iPhone 18 Pro and Pro Max/IMG_4589.DNG)
Software strings observed: 27.0
Lenses observed: iPhone 18 Pro Max back triple camera 6.93mm f/1.48
ISO observed: 64
Exposure observed: 1/2088 s, 1/5587 s
F-number observed: F1.5, F1.8
Focal length observed: 6.9 mm
EXIF PixelDimensions observed: 8064 x 6048
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Apple"
- IFD0 Model: "iPhone 18 Pro Max"
- IFD0 DNGVersion: {"hex": "01070000"}
- IFD0 DNGBackwardVersion: {"hex": "01070000"}
- IFD0 UniqueCameraModel: "iPhone19,3 back camera"
- IFD0 ColorMatrix1: [[27979, 23063], [-15131, 25136], [-5108, 24475], [-56321, 130725], [47051, 31980], [3080, 192667], [-9277, 291031], [34181, 288159], [33555, 50449]]
- IFD0 ColorMatrix2: [[12380, 14047], [-18864, 55505], [-816, 6665], [-8574, 20887], [22439, 17411], [107067, 1100084], [-4150, 44547], [7197, 38183], [125834, 262691]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1, 1, 1, 1, 1, 1]
- IFD0 BaselineExposure: [86777, 22966]
- IFD0 BaselineSharpness: [3, 2]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: [10, 10, 10]
- raw SamplesPerPixel: 3
- raw PhotometricInterpretation: 34892
- raw BlackLevel: [0, 0, 0]
- raw WhiteLevel: [65535, 65535, 65535]
- raw LinearizationTable: [0, 2, 4, 6, 8, 10, 13, 15, 17, 19, 22, 24, 26, 29, 31, 34, 36, 39, 41, 44, 47, 49, 52, 55, 58, 61, 63, 66, 69, 72, 75, 78, 82, 85, 88, 91, 94, 98, 101, 104, 10
- raw NewSubfileType: 0
- raw _shape: [6048, 8064, 3]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `Apple`, Model `iPhone 18 Pro Max`, UniqueCameraModel `iPhone 18 Pro Max`, Software `27.0`
- DNGVersion [1, 7, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 5587], [1, 2088], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[150, 100], [170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): iPhone 18 Pro Max back triple camera 6.93mm f/1.48
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `apple_iphone_18_pro_max-native`: pins 8064x6048 (native sensor geometry)

Base `--camera-profile=apple_iphone_18_pro_max` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
