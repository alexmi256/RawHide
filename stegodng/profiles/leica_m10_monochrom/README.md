# Leica M10 MONOCHROM
Profile slug: `leica_m10_monochrom`  
EXIF Make/Model: `Leica Camera AG` / `LEICA M10 MONOCHROM`
Native geometry: 7864x5200 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Leica M10 Monochrom 2/5210499415.dng`
Files seen: 4 (Leica M10 Monochrom 2/5210499415.dng, Leica M10 Monochrom 2/5310664851.dng, Leica M10 Monochrom/1671480145.dng, Leica M10 Monochrom/8747625113.dng)
Software strings observed: 2.12.8.0
Lenses observed: Summaron-M 1:5.6/28; Summicron-M 1:2/35 ASPH.; Summilux-M 1:1.4/28 ASPH.; Summilux-M 1:1.5/90 ASPH.
ISO observed: 1250, 1600, 640, 8000
Exposure observed: 1/250 s, 1/60 s
F-number observed: none
Focal length observed: 28.0 mm, 35.0 mm, 90.0 mm
EXIF PixelDimensions observed: 7872 x 5208
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Leica Camera AG"
- IFD0 Model: "LEICA M10 MONOCHROM"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA M10 MONOCHROM"
- IFD0 BaselineExposure: [0, 100]
- IFD0 AntiAliasStrength: [0, 1]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 34892
- raw BlackLevel: 0
- raw WhiteLevel: 15000
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [7864, 5200]
- raw AntiAliasStrength: [0, 1]
- raw NewSubfileType: 0
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "LEICA M10 MONOCHROM"
- raw _shape: [5208, 7872]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `Leica Camera AG`, Model `LEICA M10 MONOCHROM`, UniqueCameraModel `LEICA M10 MONOCHROM`, Software `2.12.8.0`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 8000]
- Lens pool (4): Summaron-M 1:5.6/28; Summicron-M 1:2/35 ASPH.; Summilux-M 1:1.4/28 ASPH.; Summilux-M 1:1.5/90 ASPH.
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['55']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_m10_monochrom-native`: pins 7864x5200 (native sensor geometry)

Base `--camera-profile=leica_m10_monochrom` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
