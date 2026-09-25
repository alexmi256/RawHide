# Ricoh PENTAX K-3 II
Profile slug: `ricoh_pentax_k_3_ii`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `PENTAX K-3 II`
Native geometry: 6016x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 2.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Pentax K-3 II/8274731402.dng`
Files seen: 2 (Pentax K-3 II/8274731402.dng, Pentax K-3 II/9862872686.dng)
Software strings observed: PENTAX K-3 II Ver. 0.20
Lenses observed: HD PENTAX-DA 20-40mm F2.8-4 Limited
ISO observed: 400
Exposure observed: 1/30 s, 1/500 s
F-number observed: F4
Focal length observed: 40.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "PENTAX K-3 II"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "PENTAX K-3 II"
- IFD0 ColorMatrix1: [[63660, 65536], [-31530, 65536], [-5221, 65536], [-22911, 65536], [64449, 65536], [28093, 65536], [-1354, 65536], [2831, 65536], [51779, 65536]]
- IFD0 ColorMatrix2: [[56174, 65536], [-16976, 65536], [-7523, 65536], [-26184, 65536], [80617, 65536], [12325, 65536], [-6894, 65536], [12088, 65536], [45959, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 437, 256, 256, 256, 508]
- IFD0 BaselineExposure: [-34284, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1, 1, 1, 0]
- raw WhiteLevel: 16125
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [6, 12]
- raw DefaultCropSize: [6016, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [4, 10, 4028, 6038]
- raw NewSubfileType: 0
- raw _shape: [4032, 6080]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `PENTAX K-3 II`, UniqueCameraModel `PENTAX K-3 II`, Software `PENTAX K-3 II Ver. 0.20`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [10, 2000], [10, 1000], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): HD PENTAX-DA 20-40mm F2.8-4 Limited
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_pentax_k_3_ii-native`: pins 6016x4000 (native sensor geometry)

Base `--camera-profile=ricoh_pentax_k_3_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
