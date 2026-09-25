# Google Pixel 4 XL
Profile slug: `google_pixel_4_xl`  
EXIF Make/Model: `Google` / `Pixel 4 XL`
Native geometry: 3720x2790 most common decoded dims across 2 sample(s) (also seen 4032x3024)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Google Pixel 4/0070253851.dng`
Files seen: 2 (Google Pixel 4/0070253851.dng, Google Pixel 4/4208260663.dng)
Software strings observed: HDR+ 1.0.264967922nl, HDR+ 1.0.274655470zd
Lenses observed: none
ISO observed: 40, 60
Exposure observed: 0.000468696 s, 1.69742 s
F-number observed: F1.7, F2.4
Focal length observed: 4.4 mm, 5.8 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Google"
- IFD0 Model: "Pixel 4 XL"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "Google Pixel 4 XL"
- IFD0 ColorMatrix1: [[17743, 10000], [-8430, 10000], [-2730, 10000], [-9956, 10000], [19269, 10000], [401, 10000], [401, 10000], [-1525, 10000], [7948, 10000]]
- IFD0 ColorMatrix2: [[24646, 10000], [-17047, 10000], [-4313, 10000], [-9379, 10000], [19101, 10000], [-68, 10000], [479, 10000], [-1232, 10000], [10885, 10000]]
- IFD0 CalibrationIlluminant1: 21
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [682359, 1000000, 1000000, 1000000, 385109, 1000000]
- IFD0 BaselineExposure: [193, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 ShadowScale: [1, 1]
- IFD0 MakerNoteSafety: 1
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [262144, 256, 262144, 256, 262144, 256, 262144, 256]
- raw WhiteLevel: 16383
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 1, 8, 1]
- raw DefaultCropSize: [3704, 1, 2774, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 2790, 3720]
- raw OpcodeList3: {"hex": "0000000100000001010300000000000100000044000000013fef7bdf000000003fa6734a80000000bfa57a4d600000003f8ca92160000000000000000000000000000000000000003fe0089
- raw NewSubfileType: 0
- raw _shape: [2790, 3720]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Google`, Model `Pixel 4 XL`, UniqueCameraModel `Pixel 4 XL`, Software `HDR+ 1.0.274655470zd`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1048624 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[5, 10000], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [16974, 10000], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [240, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [40, 50, 60, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Pixel 4 XL built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `google_pixel_4_xl-native`: pins 3720x2790 (native sensor geometry)

Base `--camera-profile=google_pixel_4_xl` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
