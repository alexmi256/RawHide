# Ricoh PENTAX K-70
Profile slug: `ricoh_pentax_k_70`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `PENTAX K-70`
Native geometry: 6000x4000 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 2.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Pentax 55-300mm F4.5-6.3 ED PLM WR RE/1799575229.dng`
Files seen: 6 (Pentax 55-300mm F4.5-6.3 ED PLM WR RE/1799575229.dng, Pentax 55-300mm F4.5-6.3 ED PLM WR RE/9371331238.dng, Pentax DA 11-18mm F2.8/2077432261.dng, Pentax DA 11-18mm F2.8/8234187056.dng, ...)
Software strings observed: Digital Camera Utility 5 Ver.5.6.0, PENTAX K-70 Ver. 1.00, PENTAX K-70 Ver. 1.11
Lenses observed: HD PENTAX-DA 55-300mm F4.5-6.3 ED PLM WR RE; smc PENTAX-DA 18-135mm F3.5-5.6 ED AL[IF] DC WR
ISO observed: 100, 1000
Exposure observed: 1/125 s, 1/30 s, 1/320 s, 1/400 s, 1/500 s
F-number observed: F2, F2.8, F5.6, F8, F9
Focal length observed: 11.0 mm, 18.0 mm, 35.0 mm, 48.0 mm, 55.0 mm, 88.0 mm
Serial tags present: Exif.Pentax.SerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "PENTAX K-70"
- IFD0 DNGVersion: {"hex": "01020000"}
- IFD0 DNGBackwardVersion: {"hex": "01020000"}
- IFD0 UniqueCameraModel: "PENTAX K-70"
- IFD0 ColorMatrix1: [[34273, 65536], [-5330, 65536], [23644, 65536], [-32348, 65536], [66185, 65536], [64554, 65536], [287, 65536], [-7184, 65536], [79153, 65536]]
- IFD0 ColorMatrix2: [[49270, 65536], [-15144, 65536], [-3446, 65536], [-27430, 65536], [72863, 65536], [18004, 65536], [-4204, 65536], [6705, 65536], [42512, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [30560, 65536, 65536, 65536, 38568, 65536]
- IFD0 BaselineExposure: [-32768, 65536]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [64, 64, 64, 64]
- raw WhiteLevel: 16319
- raw DefaultScale: [65536, 65536, 65536, 65536]
- raw DefaultCropOrigin: [66, 32]
- raw DefaultCropSize: [6000, 4000]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw NewSubfileType: 0
- raw _shape: [4064, 6080]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `PENTAX K-70`, UniqueCameraModel `PENTAX K-70`, Software `PENTAX K-70 Ver. 1.11`
- DNGVersion [1, 2, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 257 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [1, 400], [1, 320], [10, 2000], [1, 125], [10, 1000], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): HD PENTAX-DA 55-300mm F4.5-6.3 ED PLM WR RE; smc PENTAX-DA 18-135mm F3.5-5.6 ED AL[IF] DC WR
- FocalLength + 35mm equivalent (x2.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['63']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_pentax_k_70-native`: pins 6000x4000 (native sensor geometry)

Base `--camera-profile=ricoh_pentax_k_70` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
