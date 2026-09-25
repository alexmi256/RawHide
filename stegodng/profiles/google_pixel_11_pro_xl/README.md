# Google Pixel 11 Pro XL
Profile slug: `google_pixel_11_pro_xl`  
EXIF Make/Model: `Google` / `Pixel 11 Pro XL`
Native geometry: 8156x6124 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Google Pixel 11 Pro/PXL_20260818_011256107.RAW_.dng`
Files seen: 2 (Google Pixel 11 Pro/PXL_20260818_011256107.RAW_.dng, Google Pixel 11 Pro/PXL_20260818_015544502.RAW_.dng)
Software strings observed: HDR+ 1.0.961838130zd
Lenses observed: Pixel 11 Pro XL back camera 6.9mm f/1.7
ISO observed: 24, 30
Exposure observed: 0.000326816 s, 0.00112343 s
F-number observed: F1.7
Focal length observed: 6.9 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Google"
- IFD0 Model: "Pixel 11 Pro XL"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "Google Pixel 11 Pro XL"
- IFD0 ColorMatrix1: [[10518, 10000], [-4634, 10000], [-592, 10000], [-3576, 10000], [12977, 10000], [571, 10000], [-298, 10000], [1911, 10000], [6563, 10000]]
- IFD0 ColorMatrix2: [[7094, 10000], [-860, 10000], [-1262, 10000], [-5989, 10000], [15710, 10000], [-16, 10000], [-2104, 10000], [4390, 10000], [4099, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [490492, 1000000, 1000000, 1000000, 629884, 1000000]
- IFD0 BaselineExposure: [83, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 ShadowScale: [1, 1]
- IFD0 MakerNoteSafety: 1
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [0, 256, 0, 256, 0, 256, 0, 256]
- raw WhiteLevel: 15344
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 1, 8, 1]
- raw DefaultCropSize: [8140, 1, 6108, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 6124, 8156]
- raw OpcodeList3: {"hex": "0000000100000001010300000000000100000044000000013fef8374000000003fa7013640000000bfb50844200000003fab638ac0000000000000000000000000000000000000003fdf911
- raw NewSubfileType: 0
- raw _shape: [6124, 8156]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Google`, Model `Pixel 11 Pro XL`, UniqueCameraModel `Pixel 11 Pro XL`, Software `HDR+ 1.0.961838130zd`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[3, 10000], [11, 10000], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [24, 30, 50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Pixel 11 Pro XL back camera 6.9mm f/1.7
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `google_pixel_11_pro_xl-native`: pins 8156x6124 (native sensor geometry)

Base `--camera-profile=google_pixel_11_pro_xl` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
