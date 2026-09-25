# Google Pixel 3 XL
Profile slug: `google_pixel_3_xl`  
EXIF Make/Model: `Google` / `Pixel 3 XL`
Native geometry: 4032x3024 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Google Pixel 3/3025304887.dng`
Files seen: 2 (Google Pixel 3/3025304887.dng, Google Pixel 3/8595999464.dng)
Software strings observed: HDR+ 1.0.215421313n, HDR+ 1.0.215421313z
Lenses observed: none
ISO observed: 151, 57
Exposure observed: 0.000724348 s, 0.00916087 s
F-number observed: F1.8
Focal length observed: 4.4 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Google"
- IFD0 Model: "Pixel 3 XL"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "Google Pixel 3 XL"
- IFD0 ColorMatrix1: [[10598, 10000], [-5058, 10000], [-1606, 10000], [-9956, 10000], [19269, 10000], [401, 10000], [642, 10000], [-2328, 10000], [12123, 10000]]
- IFD0 ColorMatrix2: [[16298, 10000], [-7708, 10000], [-2489, 10000], [-9956, 10000], [19269, 10000], [401, 10000], [482, 10000], [-1686, 10000], [8591, 10000]]
- IFD0 CalibrationIlluminant1: 20
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [482422, 1000000, 1000000, 1000000, 688477, 1000000]
- IFD0 BaselineExposure: [44, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 ShadowScale: [1, 1]
- IFD0 MakerNoteSafety: 1
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [261888, 256, 261888, 256, 261632, 256, 261632, 256]
- raw WhiteLevel: 16368
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 1, 8, 1]
- raw DefaultCropSize: [4016, 1, 3008, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "02010100"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3024, 4032]
- raw OpcodeList3: {"hex": "0000000100000001010300000000000100000044000000013fef5d75c00000003fb78c8aa0000000bfc6c4b9400000003fbb757280000000000000000000000000000000000000003fe00f5
- raw NewSubfileType: 0
- raw _shape: [3024, 4032]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Google`, Model `Pixel 3 XL`, UniqueCameraModel `Pixel 3 XL`, Software `HDR+ 1.0.215421313z`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1048560 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[7, 10000], [10, 8000], [10, 4000], [10, 2000], [92, 10000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 57, 64, 100, 125, 151, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Pixel 3 XL built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `google_pixel_3_xl-native`: pins 4032x3024 (native sensor geometry)

Base `--camera-profile=google_pixel_3_xl` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
