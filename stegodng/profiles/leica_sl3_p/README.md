# Leica SL3-P
Profile slug: `leica_sl3_p`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA SL3-P`
Native geometry: 8144x5424 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Leica SL3-P/1633761829.dng`
Files seen: 2 (Leica SL3-P/1633761829.dng, Leica SL3-P/6429615462.dng)
Software strings observed: 4.2.0-t-alpha.11
Lenses observed: SUMMILUX-SL 1:1.4/50 ASPH.; VARIO-ELMARIT-SL 1:2.8-4/24-90 ASPH.
ISO observed: 125, 64
Exposure observed: 1/125 s, 1/200 s
F-number observed: F13, F5.6
Focal length observed: 50.0 mm, 76.0 mm
EXIF PixelDimensions observed: 8160 x 5432
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA SL3-P"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA SL3-P"
- IFD0 ColorMatrix1: [[11483, 10000], [-4242, 10000], [-573, 10000], [-5429, 10000], [15138, 10000], [3353, 10000], [-830, 10000], [1771, 10000], [7757, 10000]]
- IFD0 ColorMatrix2: [[7738, 10000], [-2131, 10000], [-821, 10000], [-5239, 10000], [12941, 10000], [2286, 10000], [-1513, 10000], [2327, 10000], [5248, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1024, 2698, 1024, 1024, 1024, 1471]
- IFD0 BaselineExposure: [-66, 100]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "6239604"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [512, 512, 512, 512]
- raw WhiteLevel: 10319
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [8144, 5424]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "32010b18030801e90774355f00000000"}
- raw ActiveArea: [0, 0, 5432, 8160]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033ff001468313fec0bf7f70fc809b1836bf45405a3cdbaa303f675e8322d686bb000000000000000000000000000000003feffe4
- raw NewSubfileType: 0
- raw _shape: [5432, 8160]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA SL3-P`, UniqueCameraModel `LEICA SL3-P`, Software `4.2.0-t-alpha.11`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 3252 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 200], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1300, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): SUMMILUX-SL 1:1.4/50 ASPH.; VARIO-ELMARIT-SL 1:2.8-4/24-90 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['62']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_sl3_p-native`: pins 8144x5424 (native sensor geometry)

Base `--camera-profile=leica_sl3_p` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
