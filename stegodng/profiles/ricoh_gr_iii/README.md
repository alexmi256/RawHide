# Ricoh GR III
Profile slug: `ricoh_gr_iii`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `RICOH GR III`
Native geometry: 6000x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Ricoh GR III 2/3972944157.dng`
Files seen: 6 (Ricoh GR III 2/3972944157.dng, Ricoh GR III 2/4897927126.dng, Ricoh GR III 3/0464016410.dng, Ricoh GR III 3/7093371365.dng, ...)
Software strings observed: RICOH GR III Ver. 1.00, RICOH GR III Ver. 1.10
Lenses observed: none
ISO observed: 100, 200, 400
Exposure observed: 1/100 s, 1/1250 s, 1/200 s, 1/250 s, 1/400 s
F-number observed: F2.8, F5.6, F7.1, F8
Focal length observed: 18.3 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "RICOH GR III"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "RICOH GR III"
- IFD0 ColorMatrix1: [[43566, 65536], [-17901, 65536], [-1987, 65536], [-24969, 65536], [65342, 65536], [29280, 65536], [-736, 65536], [2315, 65536], [47256, 65536]]
- IFD0 ColorMatrix2: [[40057, 65536], [-9253, 65536], [-5075, 65536], [-30238, 65536], [83413, 65536], [13536, 65536], [-4349, 65536], [9710, 65536], [38638, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 683, 256, 256, 256, 430]
- IFD0 BaselineExposure: [31251, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [128, 128, 128, 128]
- raw WhiteLevel: 16124
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [10, 12]
- raw DefaultCropSize: [6000, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [28, 58, 4052, 6078]
- raw NewSubfileType: 0
- raw _shape: [4064, 6112]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `RICOH GR III`, UniqueCameraModel `RICOH GR III`, Software `RICOH GR III Ver. 1.10`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 520 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1250], [10, 8000], [10, 4000], [1, 400], [1, 250], [1, 200], [10, 2000], [10, 1000], [1, 100], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): RICOH GR III built-in lens
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_gr_iii-native`: pins 6000x4000 (native sensor geometry)

Base `--camera-profile=ricoh_gr_iii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
