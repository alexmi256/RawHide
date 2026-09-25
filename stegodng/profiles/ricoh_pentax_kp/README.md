# Ricoh PENTAX KP
Profile slug: `ricoh_pentax_kp`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `PENTAX KP`
Native geometry: 6016x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 2.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Pentax 11-18mm F2.8 DA/1983483059.dng`
Files seen: 4 (Pentax 11-18mm F2.8 DA/1983483059.dng, Pentax 11-18mm F2.8 DA/9554636555.dng, Pentax KP/6638780796.dng, Pentax KP/8441823012.dng)
Software strings observed: PENTAX KP Ver. 1.00
Lenses observed: HD PENTAX-DA 35mm F2.8 Macro Limited; SIGMA 18-35mm F1.8 DC HSM A013
ISO observed: 200, 320, 800
Exposure observed: 1/1250 s, 1/200 s, 1/500 s
F-number observed: F5, F5.6, F8
Focal length observed: 11.0 mm, 18.0 mm, 35.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "PENTAX KP"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "PENTAX KP"
- IFD0 ColorMatrix1: [[63802, 65536], [-29296, 65536], [-15695, 65536], [-29071, 65536], [76517, 65536], [20667, 65536], [-3055, 65536], [5413, 65536], [46996, 65536]]
- IFD0 ColorMatrix2: [[48851, 65536], [-13489, 65536], [-8763, 65536], [-31731, 65536], [88837, 65536], [8844, 65536], [-10102, 65536], [15869, 65536], [37677, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 630, 256, 256, 256, 457]
- IFD0 BaselineExposure: [32382, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [64, 64, 64, 64]
- raw WhiteLevel: 16318
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [6, 16]
- raw DefaultCropSize: [6016, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [28, 54, 4060, 6082]
- raw NewSubfileType: 0
- raw _shape: [4060, 6112]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `PENTAX KP`, UniqueCameraModel `PENTAX KP`, Software `PENTAX KP Ver. 1.00`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 257 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [10, 8000], [1, 500], [10, 4000], [1, 200], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): HD PENTAX-DA 35mm F2.8 Macro Limited; SIGMA 18-35mm F1.8 DC HSM A013
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_pentax_kp-native`: pins 6016x4000 (native sensor geometry)

Base `--camera-profile=ricoh_pentax_kp` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
