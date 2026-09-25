# Phase One IQ4 150MP
Profile slug: `phase_one_iq4_150mp`  
EXIF Make/Model: `Phase One` / `IQ4 150MP`
Native geometry: 14204x10652 most common decoded dims across 2 sample(s)  
Suggested bit depth: 16  
CFA: RGGB  
Crop factor: 0.79  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Phase One IQ4/0315648440.dng`
Files seen: 2 (Phase One IQ4/0315648440.dng, Phase One IQ4/1706932725.dng)
Software strings observed: Capture One 12 Macintosh
Lenses observed: Schneider Kreuznach LS 150mm f/2.8; Schneider Kreuznach LS 35mm LS f/3.5
ISO observed: 100, 50
Exposure observed: 1/250 s, 80 s
F-number observed: F11, F8
Focal length observed: 150.0 mm, 35.0 mm
Serial tags present: Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Phase One"
- IFD0 Model: "IQ4 150MP"
- IFD0 DNGVersion: {"hex": "01010000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "IQ4 150MP"
- IFD0 ColorMatrix1: [[665934655, 2147483647], [0, 1], [0, 1], [0, 1], [1, 1], [0, 1], [0, 1], [0, 1], [1731516031, 2147483647]]
- IFD0 ColorMatrix2: [[520335295, 2147483647], [0, 1], [0, 1], [0, 1], [2126223615, 2147483647], [0, 1], [0, 1], [0, 1], [1715624703, 2147483647]]
- IFD0 CalibrationIlluminant1: 20
- IFD0 CalibrationIlluminant2: 22
- IFD0 AsShotNeutral: [1325607167, 4294967295, 1, 1, 2825636351, 4294967295]
- IFD0 BaselineExposure: [0, 1]
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 16
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1024, 1]
- raw DefaultCropOrigin: [0, 1, 0, 1]
- raw DefaultCropSize: [14204, 1, 10652, 1]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw ActiveArea: [0, 0, 10652, 14204]
- raw NewSubfileType: 0
- raw _shape: [10652, 14204]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Phase One`, Model `IQ4 150MP`, UniqueCameraModel `IQ4 150MP`, Software `Capture One 12 Macintosh`
- DNGVersion [1, 1, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [10, 4000], [1, 250], [10, 2000], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1], [800000, 10000]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (2): Schneider Kreuznach LS 150mm f/2.8; Schneider Kreuznach LS 35mm LS f/3.5
- FocalLength + 35mm equivalent (x0.79), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['JD0']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `phase_one_iq4_150mp-native`: pins 14204x10652 (native sensor geometry)

Base `--camera-profile=phase_one_iq4_150mp` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
