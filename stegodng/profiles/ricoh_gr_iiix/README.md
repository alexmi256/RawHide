# Ricoh GR IIIx
Profile slug: `ricoh_gr_iiix`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `RICOH GR IIIx`
Native geometry: 4800x3200 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Ricoh GR IIIx + GT-2 tele conversion lens/3831627921.dng`
Files seen: 6 (Ricoh GR IIIx + GT-2 tele conversion lens/3831627921.dng, Ricoh GR IIIx + GT-2 tele conversion lens/4164101943.dng, Ricoh GR IIIx 2/2349419887.dng, Ricoh GR IIIx 2/8439831709.dng, ...)
Software strings observed: RICOH GR IIIx Ver. 1.00, RICOH GR IIIx Ver. 1.10
Lenses observed: none
ISO observed: 100, 200
Exposure observed: 1/1000 s, 1/400 s, 1/50 s, 1/500 s, 1/800 s
F-number observed: F2.8, F3.2, F4, F5, F5.6
Focal length observed: 26.0 mm, 39.1 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "RICOH GR IIIx"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "RICOH GR IIIx"
- IFD0 ColorMatrix1: [[43877, 65536], [-18030, 65536], [-2001, 65536], [-24969, 65536], [65342, 65536], [29280, 65536], [-701, 65536], [2206, 65536], [45024, 65536]]
- IFD0 ColorMatrix2: [[40344, 65536], [-9320, 65536], [-5111, 65536], [-30238, 65536], [83413, 65536], [13536, 65536], [-4143, 65536], [9251, 65536], [36813, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [256, 689, 256, 256, 256, 469]
- IFD0 BaselineExposure: [-33165, 65536]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [64, 64, 64, 64]
- raw WhiteLevel: 16316
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [610, 412]
- raw DefaultCropSize: [4800, 3200]
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
- Make `RICOH IMAGING COMPANY, LTD.`, Model `RICOH GR IIIx`, UniqueCameraModel `RICOH GR IIIx`, Software `RICOH GR IIIx Ver. 1.10`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 257 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1000], [10, 8000], [1, 800], [1, 500], [10, 4000], [1, 400], [10, 2000], [10, 1000], [10, 500], [1, 50], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): RICOH GR IIIx built-in lens
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_gr_iiix-native`: pins 4800x3200 (native sensor geometry)

Base `--camera-profile=ricoh_gr_iiix` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
