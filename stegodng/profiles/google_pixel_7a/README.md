# Google Pixel 7a
Profile slug: `google_pixel_7a`  
EXIF Make/Model: `Google` / `Pixel 7a`
Native geometry: 4624x3472 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Google Pixel 7a/2209513503.dng`
Files seen: 2 (Google Pixel 7a/2209513503.dng, Google Pixel 7a/5533615701.dng)
Software strings observed: HDR+ 1.0.529852275zd
Lenses observed: none
ISO observed: 45, 47
Exposure observed: 0.00257518 s, 0.0333366 s
F-number observed: F1.9
Focal length observed: 5.4 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Google"
- IFD0 Model: "Pixel 7a"
- IFD0 DNGVersion: {"hex": "01060000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "Google Pixel 7a"
- IFD0 ColorMatrix1: [[18584, 10000], [-12861, 10000], [-3264, 10000], [-9399, 10000], [19119, 10000], [-68, 10000], [550, 10000], [-1294, 10000], [11643, 10000]]
- IFD0 ColorMatrix2: [[14750, 10000], [-6998, 10000], [-2269, 10000], [-9935, 10000], [19229, 10000], [426, 10000], [415, 10000], [-1521, 10000], [7881, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [458783, 1000000, 1000000, 1000000, 591740, 1000000]
- IFD0 BaselineExposure: [173, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 ShadowScale: [1, 1]
- IFD0 MakerNoteSafety: 1
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [262170, 256, 262172, 256, 262156, 256, 262158, 256]
- raw WhiteLevel: 16368
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 1, 8, 1]
- raw DefaultCropSize: [4608, 1, 3456, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3472, 4624]
- raw OpcodeList3: {"hex": "0000000100000001010300000000000100000044000000013fef0f0f200000003fb0b955e0000000bfb81cb7000000003fae922c80000000000000000000000000000000000000003fe080c
- raw NewSubfileType: 0
- raw _shape: [3472, 4624]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Google`, Model `Pixel 7a`, UniqueCameraModel `Pixel 7a`, Software `HDR+ 1.0.529852275zd`
- DNGVersion [1, 6, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1049689 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [26, 10000], [10, 2000], [10, 1000], [10, 500], [333, 10000], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [190, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [45, 47, 50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Pixel 7a built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `google_pixel_7a-native`: pins 4624x3472 (native sensor geometry)

Base `--camera-profile=google_pixel_7a` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
