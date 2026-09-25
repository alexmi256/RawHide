# Panasonic DC-S1H
Profile slug: `panasonic_dc_s1h`  
EXIF Make/Model: `Panasonic` / `DC-S1H`
Native geometry: 6024x4016 most common decoded dims across 5 sample(s) (also seen 6028x4016)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Panasonic S 20-60mm F3.5-5.6/6156999779.dng`
Files seen: 5 (Panasonic S 20-60mm F3.5-5.6/6156999779.dng, Sigma 24mm F2 DG DN/2325811684.rw2, Sigma 24mm F2 DG DN/7084886804.rw2, Sigma 35mm F2 DG DN 2/4691372422.rw2, ...)
Software strings observed: Ver.2.2, Ver.2.4
Lenses observed: LUMIX S 20-60/F3.5-5.6
ISO observed: 100, 400, 800
Exposure observed: 1/160 s, 1/200 s, 1/30 s, 1/500 s
F-number observed: F2, F2.8, F4
Focal length observed: 24.0 mm, 28.0 mm, 35.0 mm
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (fallback (serials non-alphanumeric))

## Harvested DNG calibration
- IFD0 Make: "Panasonic"
- IFD0 Model: "DC-S1H"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "Panasonic DC-S1H"
- IFD0 ColorMatrix1: [[11335, 10000], [-6469, 10000], [804, 10000], [-4415, 10000], [12413, 10000], [2235, 10000], [-223, 10000], [804, 10000], [6653, 10000]]
- IFD0 ColorMatrix2: [[9397, 10000], [-3719, 10000], [-805, 10000], [-5425, 10000], [13326, 10000], [2309, 10000], [-972, 10000], [1715, 10000], [6034, 10000]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [423841, 1000000, 1000000, 1000000, 632099, 1000000]
- IFD0 BaselineExposure: [10, 100]
- IFD0 BaselineNoise: [150, 100]
- IFD0 BaselineSharpness: [133, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 CameraSerialNumber: "WJ-PP001062"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [130816, 256, 130560, 256, 130560, 256, 130816, 256]
- raw WhiteLevel: 16380
- raw DefaultScale: [1, 1, 1, 1]
- raw DefaultCropOrigin: [12, 1, 8, 1]
- raw DefaultCropSize: [6000, 1, 4000, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [100, 100]
- raw BestQualityScale: [1, 1]
- raw ActiveArea: [0, 0, 4016, 6028]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033feffac5485bc3e8bfb13f02d1939b803fa7e00d4e173900bf80807ac2ae3000000000000000000000000000000000003feffb2
- raw NewSubfileType: 0
- raw _shape: [4016, 6028]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Panasonic`, Model `DC-S1H`, UniqueCameraModel `DC-S1H`, Software `Ver.2.4`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 523384 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [1, 200], [10, 2000], [1, 160], [10, 1000], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): LUMIX S 20-60/F3.5-5.6
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['92A', '94A', '93A', '95A']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `panasonic_dc_s1h-native`: pins 6024x4016 (native sensor geometry)

Base `--camera-profile=panasonic_dc_s1h` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
