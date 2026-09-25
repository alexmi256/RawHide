# Google Pixel XL
Profile slug: `google_pixel_xl`  
EXIF Make/Model: `Google` / `Pixel XL`
Native geometry: 4032x3020 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: Bayer (unidentified)  
Crop factor: 7.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Google Pixel Real World/5962057809.dng`
Files seen: 2 (Google Pixel Real World/5962057809.dng, Google Pixel Real World/9846071095.dng)
Software strings observed: google/marlin/marlin:7.1/NAE63P/3319494:user/release-keys
Lenses observed: none
ISO observed: 51
Exposure observed: 1/2300 s
F-number observed: F2
Focal length observed: 4.7 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Google"
- IFD0 Model: "Pixel XL"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "Pixel XL-Google-google"
- IFD0 ColorMatrix1: [[92, 128], [-25, 128], [-11, 128], [-72, 128], [173, 128], [21, 128], [-29, 128], [40, 128], [70, 128]]
- IFD0 ColorMatrix2: [[136, 128], [-40, 128], [-35, 128], [-72, 128], [212, 128], [-15, 128], [-7, 128], [25, 128], [77, 128]]
- IFD0 CalibrationIlluminant1: 21
- IFD0 CalibrationIlluminant2: 17
- IFD0 AsShotNeutral: [58, 128, 129, 128, 85, 128]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [6375, 100, 6350, 100, 6350, 100, 6375, 100]
- raw WhiteLevel: 1023
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 8]
- raw DefaultCropSize: [4032, 3020]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "02010100"}
- raw ActiveArea: [8, 0, 3044, 4048]
- raw OpcodeList3: {"hex": "00000000"}
- raw NewSubfileType: 0
- raw CalibrationIlluminant1: 21
- raw CalibrationIlluminant2: 17
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "Pixel XL-Google-google"
- raw _shape: [3044, 4048]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Google`, Model `Pixel XL`, UniqueCameraModel `Pixel XL`, Software `google/marlin/marlin:7.1/NAE63P/3319494:user/release-keys`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 408393 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2300], [10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 51, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Pixel XL built-in lens
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `google_pixel_xl-native`: pins 4032x3020 (native sensor geometry)

Base `--camera-profile=google_pixel_xl` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
