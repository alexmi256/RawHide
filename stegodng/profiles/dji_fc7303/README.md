# DJI FC7303 (drone camera unit)
Profile slug: `dji_fc7303`  
EXIF Make/Model: `DJI` / `FC7303`
Native geometry: 4000x3000 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.7  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `DJI Mavic Mini 2/3450332848.dng`
Files seen: 2 (DJI Mavic Mini 2/3450332848.dng, DJI Mavic Mini 2/8303797075.dng)
Software strings observed: Adobe Photoshop Lightroom 10.0 Classic (Macintosh)
Lenses observed: 20.7 mm
ISO observed: 100, 120
Exposure observed: 1/10 s, 1/40 s
F-number observed: F2.8
Focal length observed: 4.5 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "DJI"
- IFD0 Model: "FC7303"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "FC7303"
- IFD0 ColorMatrix1: [[16804, 10000], [-9787, 10000], [-2259, 10000], [-3295, 10000], [13660, 10000], [-113, 10000], [-307, 10000], [1590, 10000], [6367, 10000]]
- IFD0 ColorMatrix2: [[6883, 10000], [-1326, 10000], [-981, 10000], [-4557, 10000], [13643, 10000], [632, 10000], [-1285, 10000], [2585, 10000], [4512, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [457704, 1000000, 1000000, 1000000, 644531, 1000000]
- IFD0 BaselineExposure: [-7500, 10000]
- IFD0 BaselineNoise: [100, 100]
- IFD0 BaselineSharpness: [100, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "1SFLH8S0AB04SL"
- IFD0 LensInfo: [[207000, 10000], [207000, 10000], [0, 0], [0, 0]]
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1020, 1, 1020, 1, 1020, 1, 1020, 1]
- raw WhiteLevel: 16383
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [4000, 1, 3000, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 3000, 4000]
- raw OpcodeList3: {"bytes_len": 38568, "sha1_prefix": "c61d09211f5e9c77", "hex_prefix": "00000003000000030103000000000000000000384000aef2f46f1396c00efc94"}
- raw NewSubfileType: 0
- raw _shape: [3000, 4000]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `DJI`, Model `FC7303`, UniqueCameraModel `FC7303`, Software `Adobe Photoshop Lightroom 10.0 Classic (Macintosh)`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4080 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [10, 1000], [10, 500], [1, 40], [10, 250], [10, 125], [1, 10], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 120, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): 20.7 mm
- FocalLength + 35mm equivalent (x2.7), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1SF']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `dji_fc7303-native`: pins 4000x3000 (native sensor geometry)

Base `--camera-profile=dji_fc7303` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
