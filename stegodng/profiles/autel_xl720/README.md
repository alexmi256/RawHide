# Autel XL720
Profile slug: `autel_xl720`  
EXIF Make/Model: `Autel Robotics` / `XL720`
Native geometry: 5472x3648 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Autel EVO Lite+/2203151315.dng`
Files seen: 2 (Autel EVO Lite+/2203151315.dng, Autel EVO Lite+/7296763790.dng)
Software strings observed: V2.1.6.7, V2.1.7.29
Lenses observed: none
ISO observed: 100
Exposure observed: 1/1400 s, 1/150 s
F-number observed: F2.8
Focal length observed: 10.6 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "Autel Robotics"
- IFD0 Model: "XL720"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "XL720"
- IFD0 ColorMatrix1: [[13007, 10000], [-7710, 10000], [920, 10000], [-1262, 10000], [8047, 10000], [3842, 10000], [122, 10000], [834, 10000], [5144, 10000]]
- IFD0 ColorMatrix2: [[9945, 10000], [-3550, 10000], [-868, 10000], [-2576, 10000], [10944, 10000], [1866, 10000], [-426, 10000], [1697, 10000], [5299, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [497087, 1000000, 1000000, 1000000, 585812, 1000000]
- IFD0 BaselineExposure: [0, 100]
- IFD0 BaselineNoise: [300, 100]
- IFD0 BaselineSharpness: [133, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [12800, 256, 12800, 256, 12800, 256, 12800, 256]
- raw WhiteLevel: 1023
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [5472, 1, 3648, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw LinearizationTable: {"len": 65536, "sha1_prefix": "087f5aed6240554f"}
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw BestQualityScale: [1, 1]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033ff004189374bc6abfb597a24894c448bf8c0ebedfa43fe63f8a2c669057d178bed21b57ec9d6f09bebd1dea6e14d2ed3ff0041
- raw NewSubfileType: 0
- raw _shape: [3648, 5472]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Autel Robotics`, Model `XL720`, UniqueCameraModel `XL720`, Software `V2.1.7.29`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 819988 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1400], [10, 8000], [10, 4000], [10, 2000], [1, 150], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): XL720 built-in lens
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `autel_xl720-native`: pins 5472x3648 (native sensor geometry)

Base `--camera-profile=autel_xl720` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
