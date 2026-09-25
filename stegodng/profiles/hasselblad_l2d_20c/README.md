# Hasselblad L2D-20c
Profile slug: `hasselblad_l2d_20c`  
EXIF Make/Model: `Hasselblad` / `L2D-20c`
Native geometry: 5280x3956 most common decoded dims across 6 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 0.79  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Mavic 3 Cine/1433194902.dng`
Files seen: 6 (DJI Mavic 3 Cine/1433194902.dng, DJI Mavic 3 Cine/6686608347.dng, DJI Mavic 3 Classic/0459566529.dng, DJI Mavic 3 Classic/8601017911.dng, ...)
Software strings observed: 00.04.80.83, 10.00.16.11, 10.01.67.27
Lenses observed: none
ISO observed: 100, 120, 130, 190, 400
Exposure observed: 1/1500 s, 1/160 s, 1/1600 s, 1/240 s, 1/320 s, 1/40 s
F-number observed: F11, F2.8
Focal length observed: 12.3 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Hasselblad"
- IFD0 Model: "L2D-20c"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "Hasselblad L2D-20c"
- IFD0 ColorMatrix1: [[13364, 10000], [-8291, 10000], [1230, 10000], [-3009, 10000], [11905, 10000], [3937, 10000], [446, 10000], [-215, 10000], [8437, 10000]]
- IFD0 ColorMatrix2: [[8575, 10000], [-3219, 10000], [-868, 10000], [-3351, 10000], [11451, 10000], [1593, 10000], [207, 10000], [468, 10000], [4876, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [4096, 9879, 4096, 4096, 4096, 7655]
- IFD0 BaselineExposure: [78, 100]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "493OJ7Q7AA0204"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [4096, 1, 4096, 1, 4096, 1, 4096, 1]
- raw WhiteLevel: 65472
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [5280, 1, 3956, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3956, 5280]
- raw OpcodeList3: {"bytes_len": 12564, "sha1_prefix": "c4377c81a40db8d5", "hex_prefix": "000000020000000901030000000000000000304c000000000000000000000f8e"}
- raw NewSubfileType: 0
- raw _shape: [3956, 5376]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Hasselblad`, Model `L2D-20c`, UniqueCameraModel `L2D-20c`, Software `10.01.67.27`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4100 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1600], [1, 1500], [10, 8000], [10, 4000], [1, 320], [1, 240], [10, 2000], [1, 160], [10, 1000], [10, 500], [1, 40], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 120, 125, 130, 160, 190, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): L2D-20c built-in lens
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['49']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `hasselblad_l2d_20c-native`: pins 5280x3956 (native sensor geometry)

Base `--camera-profile=hasselblad_l2d_20c` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
