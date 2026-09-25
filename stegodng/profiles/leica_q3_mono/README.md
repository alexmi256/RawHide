# Leica Q3 MONO
Profile slug: `leica_q3_mono`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA Q3 MONO`
Native geometry: 9520x6336 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Leica Q3 Monochrom/1595045130.dng`
Files seen: 2 (Leica Q3 Monochrom/1595045130.dng, Leica Q3 Monochrom/2706748612.dng)
Software strings observed: 3.9.0
Lenses observed: SUMMILUX 1:1.7/28 ASPH.
ISO observed: 200, 6400
Exposure observed: 1/125 s, 1/320 s
F-number observed: F1.7, F2
Focal length observed: 28.0 mm
EXIF PixelDimensions observed: 9536 x 6344
Serial tags present: Exif.Image.CameraSerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA Q3 MONO"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA Q3 MONO"
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "6154548"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 34892
- raw BlackLevel: [512, 512, 512, 512]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [9520, 6336]
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "31003724120b0be90734e95d00000000"}
- raw ActiveArea: [0, 0, 6344, 9536]
- raw OpcodeList3: {"hex": "0000000100000001010400000000000000000044000000013feff9fc6f11c92fbfac0cce31cd1ce2bfb4bc63beecd4683fa6ba4575a116ed000000000000000000000000000000003fe0000
- raw NewSubfileType: 0
- raw _shape: [6344, 9536]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA Q3 MONO`, UniqueCameraModel `LEICA Q3 MONO`, Software `3.9.0`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 2048 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 320], [10, 2000], [1, 125], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): SUMMILUX 1:1.7/28 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['61']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_q3_mono-native`: pins 9520x6336 (native sensor geometry)

Base `--camera-profile=leica_q3_mono` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
