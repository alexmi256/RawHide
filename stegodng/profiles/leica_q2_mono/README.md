# Leica Q2 MONO
Profile slug: `leica_q2_mono`  
EXIF Make/Model: `LEICA CAMERA AG` / `LEICA Q2 MONO`
Native geometry: 8368x5584 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.0  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Leica Q2 Monochrom 2/0744606078.dng`
Files seen: 4 (Leica Q2 Monochrom 2/0744606078.dng, Leica Q2 Monochrom 2/1836812008.dng, Leica Q2 Monochrom/0343025465.dng, Leica Q2 Monochrom/6445653628.dng)
Software strings observed: 1.03
Lenses observed: SUMMILUX 1:1.7/28 ASPH.
ISO observed: 100, 12500, 250, 6400
Exposure observed: 1/125 s, 1/60 s
F-number observed: F1.7, F2.5, F5.6, F9
Focal length observed: 28.0 mm
EXIF PixelDimensions observed: 8424 x 5632
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "LEICA CAMERA AG"
- IFD0 Model: "LEICA Q2 MONO"
- IFD0 DNGVersion: {"hex": "01040000"}
- IFD0 DNGBackwardVersion: {"hex": "01030000"}
- IFD0 UniqueCameraModel: "LEICA Q2 MONO"
- IFD0 BaselineExposure: [-51, 100]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [10, 10]
- IFD0 LinearResponseLimit: [10, 10]
- IFD0 CameraSerialNumber: "5597106"
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 34892
- raw BlackLevel: 512
- raw WhiteLevel: 11500
- raw DefaultCropOrigin: [12, 24]
- raw DefaultCropSize: [8368, 5584]
- raw AntiAliasStrength: [7, 10]
- raw BestQualityScale: [10, 10]
- raw RawDataUniqueID: {"hex": "110037030d020be407b2675500000000"}
- raw ActiveArea: [0, 0, 5632, 8392]
- raw OpcodeList3: {"hex": "0000000100000001010400000000000000000044000000013feff9dd749860e8bfa85d28a44e886ebfb93314992c14d43fac55699909f008000000000000000000000000000000003fe0000
- raw NewSubfileType: 0
- raw _shape: [5632, 8424]
- raw _dtype: "uint16"
- raw _photometric: 34892

## Static fields (identical in every output file)
- Make `LEICA CAMERA AG`, Model `LEICA Q2 MONO`, UniqueCameraModel `LEICA Q2 MONO`, Software `1.03`
- DNGVersion [1, 4, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [10, 2000], [1, 125], [10, 1000], [1, 60], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [900, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400, 12500]
- Lens pool (1): SUMMILUX 1:1.7/28 ASPH.
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['55']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `leica_q2_mono-native`: pins 8368x5584 (native sensor geometry)

Base `--camera-profile=leica_q2_mono` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
