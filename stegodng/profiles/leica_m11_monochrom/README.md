# Leica M11 Monochrom
Profile slug: `leica_m11_monochrom`  
EXIF Make/Model: `Leica Camera AG` / `LEICA M11 Monochrom`
Native geometry: 9528x6328 active area (harvested DefaultCropSize)  
Suggested bit depth: 16  
CFA: unknown  
Crop factor: 7.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Leica M11 Monochrom/7162099585.dng`
Files seen: 2 (Leica M11 Monochrom/7162099585.dng, Leica M11 Monochrom/9268498212.dng)
Software strings observed: 1.23.7.65
Lenses observed: Apo-Summicron-M 1:2/50 ASPH.; Summicron-M 1:2/28 ASPH.
ISO observed: 125, 8000
Exposure observed: 1/250 s, 1/80 s
F-number observed: none
Focal length observed: 28.0 mm, 50.0 mm
EXIF PixelDimensions observed: 9536 x 6336
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Leica Camera AG"
- IFD0 Model: "LEICA M11 Monochrom"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA M11 Monochrom"
- IFD0 BaselineExposure: [0, 100]
- IFD0 AntiAliasStrength: [0, 1]
- IFD0 BitsPerSample: 16
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 34892
- raw BlackLevel: 1023
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [9528, 6328]
- raw AntiAliasStrength: [0, 1]
- raw RawDataUniqueID: {"hex": "92936c1ea2538d762b074beb60aacbc5"}
- raw NewSubfileType: 0
- raw DNGVersion: {"hex": "01040000"}
- raw UniqueCameraModel: "LEICA M11 Monochrom"
- raw _shape: [6336, 9536]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `Leica Camera AG`, Model `LEICA M11 Monochrom`, UniqueCameraModel `LEICA M11 Monochrom`, Software `1.23.7.65`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [1, 80], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 8000]
- Lens pool (2): Apo-Summicron-M 1:2/50 ASPH.; Summicron-M 1:2/28 ASPH.
- FocalLength + 35mm equivalent (x7.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['56']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_m11_monochrom-native`: pins 9528x6328 (native sensor geometry)

Base `--camera-profile=leica_m11_monochrom` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
