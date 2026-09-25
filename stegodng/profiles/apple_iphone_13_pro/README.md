# Apple iPhone 13 Pro
Profile slug: `apple_iphone_13_pro`  
EXIF Make/Model: `Apple` / `iPhone 13 Pro`
Native geometry: 4032x3024 most common decoded dims across 4 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Apple iPhone 13 Pro/3522260501.dng`
Files seen: 4 (Apple iPhone 13 Pro/3043154948.heic, Apple iPhone 13 Pro/3522260501.dng, iPhone 13 Pro/5499349486.dng, iPhone 13 Pro/6728302480.dng)
Software strings observed: 15.0
Lenses observed: iPhone 13 Pro back dual wide camera 5.7mm f/1.5; iPhone 13 Pro back triple camera 1.57mm f/1.8; iPhone 13 Pro back triple camera 5.7mm f/1.5; iPhone 13 Pro front camera 2.71mm f/2.2
ISO observed: 25, 50, 64, 80
Exposure observed: 1/121 s, 1/128 s, 1/161 s, 1/808 s
F-number observed: F1.5, F1.8, F2.2
Focal length observed: 1.6 mm, 2.7 mm, 5.7 mm
EXIF PixelDimensions observed: 4032 x 3024
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Apple"
- IFD0 Model: "iPhone 13 Pro"
- IFD0 DNGVersion: {"hex": "01060000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "iPhone14,2 back ultra wide camera"
- IFD0 ColorMatrix1: [[1284057856, 1073741824], [-553015872, 1073741824], [-247781632, 1073741824], [-483649472, 1073741824], [1598455936, 1073741824], [30281436, 1073741824], [-422
- IFD0 ColorMatrix2: [[935831936, 1073741824], [-303002688, 1073741824], [-127982208, 1073741824], [-456371712, 1073741824], [1384590080, 1073741824], [117217984, 1073741824], [-109
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1073741824, 1073741824, 1073741824, 1073741824, 1073741824, 1073741824]
- IFD0 BaselineExposure: [1073868288, 268435456]
- IFD0 BaselineSharpness: [1610612736, 1073741824]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: [12, 12, 12]
- raw SamplesPerPixel: 3
- raw PhotometricInterpretation: 34892
- raw BlackLevel: [0, 0, 0]
- raw WhiteLevel: [65535, 65535, 65535]
- raw LinearizationTable: {"len": 4096, "sha1_prefix": "fa7456e234716170"}
- raw NewSubfileType: 0
- raw _shape: [3024, 4032, 3]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `Apple`, Model `iPhone 13 Pro`, UniqueCameraModel `iPhone 13 Pro`, Software `15.0`
- DNGVersion [1, 6, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 808], [10, 8000], [10, 4000], [10, 2000], [1, 161], [1, 128], [1, 121], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[150, 100], [170, 100], [180, 100], [200, 100], [220, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [25, 50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): iPhone 13 Pro back dual wide camera 5.7mm f/1.5; iPhone 13 Pro back triple camera 1.57mm f/1.8; iPhone 13 Pro back triple camera 5.7mm f/1.5; iPhone 13 Pro front camera 2.71mm f/2.2
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `apple_iphone_13_pro-native`: pins 4032x3024 (native sensor geometry)

Base `--camera-profile=apple_iphone_13_pro` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
