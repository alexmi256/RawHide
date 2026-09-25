# Sealife DC2000
Profile slug: `sealife_dc2000`  
EXIF Make/Model: `SEALIFE` / `SEALIFE DC2000`
Native geometry: 5472x3648 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Sealife DC2000/2663237941.dng`
Files seen: 2 (Sealife DC2000/2663237941.dng, Sealife DC2000/9576987467.dng)
Software strings observed: 1.0100
Lenses observed: none
ISO observed: 125, 259
Exposure observed: (0/300), (0/8000)
F-number observed: F1.8
Focal length observed: 11.6 mm
EXIF PixelDimensions observed: 5472 x 3648
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "SEALIFE"
- IFD0 Model: "SEALIFE DC2000"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "20M DSC"
- IFD0 ColorMatrix1: [[7366, 10000], [-3213, 10000], [380, 10000], [-3609, 10000], [11127, 10000], [2852, 10000], [-218, 10000], [694, 10000], [5821, 10000]]
- IFD0 ColorMatrix2: [[6596, 10000], [-2079, 10000], [-562, 10000], [-4782, 10000], [13016, 10000], [1933, 10000], [-970, 10000], [1581, 10000], [5181, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [861953, 1000000, 1000000, 1000000, 296984, 1000000]
- IFD0 BaselineExposure: [-7, 100]
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
- raw WhiteLevel: 65535
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [5424, 1, 3616, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3648, 5472]
- raw NewSubfileType: 0
- raw _shape: [3648, 5472]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `SEALIFE`, Model `SEALIFE DC2000`, UniqueCameraModel `SEALIFE DC2000`, Software `1.0100`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [180, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 259, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): SEALIFE DC2000 built-in lens
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sealife_dc2000-native`: pins 5472x3648 (native sensor geometry)

Base `--camera-profile=sealife_dc2000` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
