# Apple iPhone X
Profile slug: `apple_iphone_x`  
EXIF Make/Model: `Apple` / `iPhone X`
Native geometry: 4032x3024 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `iPhone X/4159813066.dng`
Files seen: 2 (iPhone X/4159813066.dng, iPhone X/8024474106.dng)
Software strings observed: 11.2.2, Adobe Camera 1.1
Lenses observed: iPhone X back camera 4mm f/1.8; iPhone X back camera 6mm f/2.4
ISO observed: 16, 25
Exposure observed: 1/10 s, 1/453 s
F-number observed: F1.8, F2.4
Focal length observed: 4.0 mm, 6.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Apple"
- IFD0 Model: "iPhone X"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "iPhone10,3 back telephoto camera"
- IFD0 ColorMatrix1: [[1675912448, 1073741824], [-962788992, 1073741824], [-149099808, 1073741824], [-518285888, 1073741824], [1591572992, 1073741824], [162835504, 1073741824], [-21
- IFD0 ColorMatrix2: [[917392256, 1073741824], [-279967680, 1073741824], [-103997368, 1073741824], [-579435520, 1073741824], [1423381376, 1073741824], [189191392, 1073741824], [-101
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [517173856, 1073741824, 1073741824, 1073741824, 643271424, 1073741824]
- IFD0 BaselineExposure: [-329820928, 1073741824]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: 528
- raw WhiteLevel: 4095
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw OpcodeList3: {"hex": "00000001000000030103000000000000000000383fc0cfa92f27a4a33ff5256d55fff804c0053437d48cf28840002f565441ee03bfdb23e91aa19c103fdfc804ff6ac5203fdeb4994754cc6
- raw NewSubfileType: 0
- raw _shape: [3024, 4032]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Apple`, Model `iPhone X`, UniqueCameraModel `iPhone X`, Software `Adobe Camera 1.1`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 453], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [1, 10], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [240, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [16, 25, 50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): iPhone X back camera 4mm f/1.8; iPhone X back camera 6mm f/2.4
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `apple_iphone_x-native`: pins 4032x3024 (native sensor geometry)

Base `--camera-profile=apple_iphone_x` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
