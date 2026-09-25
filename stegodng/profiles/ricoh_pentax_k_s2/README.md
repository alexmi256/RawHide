# Ricoh PENTAX K-S2
Profile slug: `ricoh_pentax_k_s2`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `PENTAX K-S2`
Native geometry: 5472x3648 active area (harvested DefaultCropSize)  
Suggested bit depth: 12  
CFA: RGGB  
Crop factor: 2.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Pentax K-S2/3765714985.dng`
Files seen: 2 (Pentax K-S2/3765714985.dng, Pentax K-S2/9530711734.dng)
Software strings observed: PENTAX K-S2 Ver. 1.00
Lenses observed: none
ISO observed: 100
Exposure observed: 1/2500 s, 1/400 s
F-number observed: F4
Focal length observed: 40.0 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "PENTAX K-S2"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "PENTAX K-S2"
- IFD0 ColorMatrix1: [[65455, 65536], [-33298, 65536], [-7486, 65536], [-23101, 65536], [66292, 65536], [26082, 65536], [-975, 65536], [2118, 65536], [47330, 65536]]
- IFD0 ColorMatrix2: [[52487, 65536], [-16497, 65536], [-7471, 65536], [-25443, 65536], [80936, 65536], [11071, 65536], [-5530, 65536], [9782, 65536], [41366, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 572, 256, 256, 256, 428]
- IFD0 BaselineExposure: [-33171, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 12
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [16, 16, 16, 16]
- raw WhiteLevel: 4078
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [8, 4]
- raw DefaultCropSize: [5472, 3648]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [0, 2, 3664, 5490]
- raw NewSubfileType: 0
- raw _shape: [3664, 5504]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `PENTAX K-S2`, UniqueCameraModel `PENTAX K-S2`, Software `PENTAX K-S2 Ver. 1.00`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 257 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 2500], [10, 8000], [10, 4000], [1, 400], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): PENTAX K-S2 built-in lens
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_pentax_k_s2-native`: pins 5472x3648 (native sensor geometry)

Base `--camera-profile=ricoh_pentax_k_s2` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
