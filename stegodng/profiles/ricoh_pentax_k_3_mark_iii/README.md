# Ricoh PENTAX K-3 Mark III
Profile slug: `ricoh_pentax_k_3_mark_iii`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `PENTAX K-3 Mark III`
Native geometry: 6192x4128 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 2.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Pentax DA 20-40mm F2.8-4 WR/6587307867.dng`
Files seen: 6 (Pentax DA 20-40mm F2.8-4 WR/6587307867.dng, Pentax DA 20-40mm F2.8-4 WR/7887488406.dng, Pentax K-3 Mark III 2/6974781584.dng, Pentax K-3 Mark III 2/9992388841.dng, ...)
Software strings observed: PENTAX K-3 Mark III Ver. 1.00, PENTAX K-3 Mark III Ver. 1.01
Lenses observed: HD PENTAX-DA 20-40mm F2.8-4 Limited
ISO observed: 100, 200, 5000
Exposure observed: 1/100 s, 1/125 s, 1/2000 s, 1/250 s, 1/60 s
F-number observed: F4, F5.6, F7.1, F8
Focal length observed: 16.0 mm, 20.0 mm, 28.8 mm, 35.6 mm, 67.5 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "PENTAX K-3 Mark III"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "PENTAX K-3 Mark III"
- IFD0 ColorMatrix1: [[49916, 65536], [-20511, 65536], [-2277, 65536], [-24969, 65536], [65342, 65536], [29280, 65536], [-716, 65536], [2252, 65536], [45958, 65536]]
- IFD0 ColorMatrix2: [[45896, 65536], [-10602, 65536], [-5814, 65536], [-30238, 65536], [83413, 65536], [13536, 65536], [-4229, 65536], [9443, 65536], [37576, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 625, 256, 256, 256, 443]
- IFD0 BaselineExposure: [17666, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [64, 64, 64, 64]
- raw WhiteLevel: 16378
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [28, 24]
- raw DefaultCropSize: [6192, 4128]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [34, 26, 4194, 6250]
- raw NewSubfileType: 0
- raw _shape: [4224, 6304]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `PENTAX K-3 Mark III`, UniqueCameraModel `PENTAX K-3 Mark III`, Software `PENTAX K-3 Mark III Ver. 1.01`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2000], [10, 8000], [10, 4000], [1, 250], [10, 2000], [1, 125], [10, 1000], [1, 100], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 5000, 6400]
- Lens pool (1): HD PENTAX-DA 20-40mm F2.8-4 Limited
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_pentax_k_3_mark_iii-native`: pins 6192x4128 (native sensor geometry)

Base `--camera-profile=ricoh_pentax_k_3_mark_iii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
