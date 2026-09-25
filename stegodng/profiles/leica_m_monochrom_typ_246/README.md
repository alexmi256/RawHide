# Leica M MONOCHROM (Typ 246)
Profile slug: `leica_m_monochrom_typ_246`  
EXIF Make/Model: `Leica Camera AG` / `LEICA M MONOCHROM (Typ 246)`
Native geometry: 5976x3992 active area (harvested DefaultCropSize)  
Suggested bit depth: 12  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Leica M Monochrom (Typ 246) real-world/2368112374.dng`
Files seen: 2 (Leica M Monochrom (Typ 246) real-world/2368112374.dng, Leica M Monochrom (Typ 246) real-world/4088985824.dng)
Software strings observed: 1.0.0.4
Lenses observed: Summilux-M 1:1.4/35 ASPH.
ISO observed: 320
Exposure observed: 1/1500 s, 1/250 s
F-number observed: F3.4, F6.8
Focal length observed: 35.0 mm
EXIF PixelDimensions observed: 5984 x 4000
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Leica Camera AG"
- IFD0 Model: "LEICA M MONOCHROM (Typ 246)"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "LEICA M MONOCHROM (Typ 246)"
- IFD0 BaselineExposure: [0, 1]
- IFD0 BaselineNoise: [1, 1]
- IFD0 BaselineSharpness: [1, 1]
- IFD0 LinearResponseLimit: [1, 1]
- IFD0 CameraSerialNumber: "4830279"
- IFD0 ShadowScale: [1, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 12
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 34892
- raw BlackLevel: 0
- raw WhiteLevel: 3750
- raw DefaultCropOrigin: [4, 4]
- raw DefaultCropSize: [5976, 3992]
- raw AntiAliasStrength: [0, 1]
- raw NewSubfileType: 0
- raw _shape: [4000, 5984]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `Leica Camera AG`, Model `LEICA M MONOCHROM (Typ 246)`, UniqueCameraModel `LEICA M MONOCHROM (Typ 246)`, Software `1.0.0.4`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 1500], [10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [340, 100], [400, 100], [560, 100], [680, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): Summilux-M 1:1.4/35 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['48']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_m_monochrom_typ_246-native`: pins 5976x3992 (native sensor geometry)

Base `--camera-profile=leica_m_monochrom_typ_246` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
