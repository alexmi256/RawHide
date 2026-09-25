# Ricoh GR IV
Profile slug: `ricoh_gr_iv`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `RICOH GR IV`
Native geometry: 6192x4128 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Ricoh GR IV street/8901472343.dng`
Files seen: 4 (Ricoh GR IV street/8901472343.dng, Ricoh GR IV street/9809913719.dng, Ricoh GR IV/4024978768.dng, Ricoh GR IV/6069367571.dng)
Software strings observed: RICOH GR IV Ver. 1.01
Lenses observed: none
ISO observed: 100, 200, 3200, 640
Exposure observed: 1/30 s, 1/500 s, 1/60 s, 1/640 s
F-number observed: F2.8
Focal length observed: 18.3 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "RICOH GR IV"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "RICOH GR IV"
- IFD0 ColorMatrix1: [[45814, 65536], [-18825, 65536], [-2090, 65536], [-24969, 65536], [65342, 65536], [29280, 65536], [-740, 65536], [2326, 65536], [47485, 65536]]
- IFD0 ColorMatrix2: [[42124, 65536], [-9731, 65536], [-5337, 65536], [-30238, 65536], [83413, 65536], [13536, 65536], [-4370, 65536], [9757, 65536], [38825, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 447, 256, 256, 256, 764]
- IFD0 BaselineExposure: [26643, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1024, 1024, 1024, 1024]
- raw WhiteLevel: 15357
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
- Make `RICOH IMAGING COMPANY, LTD.`, Model `RICOH GR IV`, UniqueCameraModel `RICOH GR IV`, Software `RICOH GR IV Ver. 1.01`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4370 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 640], [1, 500], [10, 4000], [10, 2000], [10, 1000], [1, 60], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): RICOH GR IV built-in lens
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_gr_iv-native`: pins 6192x4128 (native sensor geometry)

Base `--camera-profile=ricoh_gr_iv` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
