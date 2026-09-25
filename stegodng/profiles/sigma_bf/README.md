# Sigma BF
Profile slug: `sigma_bf`  
EXIF Make/Model: `Sigma` / `Sigma BF`
Native geometry: 6016x4012 active area (harvested DefaultCropSize)  
Suggested bit depth: 14  
CFA: RGGB  
Crop factor: 1.5  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Sigma BF photo day/0312754091.dng`
Files seen: 6 (Sigma BF photo day/0312754091.dng, Sigma BF photo day/5952328216.dng, Sigma BF vacation photo challenge/0397378204.dng, Sigma BF vacation photo challenge/9609219312.dng, ...)
Software strings observed: Sigma BF Ver1.00.33FC
Lenses observed: LUMIX S 20-60/F3.5-5.6; 35mm F2 DG | Contemporary 020
ISO observed: 100, 200, 250, 5000
Exposure observed: 1/125 s, 1/40 s, 1/500 s
F-number observed: F13, F2, F3.2, F5.6, F6.3
Focal length observed: 35.0 mm, 49.7 mm
EXIF PixelDimensions observed: 6016 x 4012
Serial tags present: Exif.Image.CameraSerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Harvested DNG calibration
- IFD0 Make: "Sigma"
- IFD0 Model: "Sigma BF"
- IFD0 DNGVersion: {"hex": "01070000"}
- IFD0 DNGBackwardVersion: {"hex": "01040000"}
- IFD0 UniqueCameraModel: "Sigma BF"
- IFD0 ColorMatrix1: [[247078625, 100000000], [-110472345, 100000000], [-28887129, 100000000], [-12065621, 100000000], [110521917, 100000000], [868898, 100000000], [451310, 10000000
- IFD0 ColorMatrix2: [[82682658, 100000000], [-21722685, 100000000], [-6662944, 100000000], [-49088199, 100000000], [123360632, 100000000], [21395642, 100000000], [-10957767, 100000
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [4613, 10000, 10000, 10000, 7331, 10000]
- IFD0 BaselineExposure: [1337, 1024]
- IFD0 BaselineNoise: [10, 10]
- IFD0 BaselineSharpness: [13, 10]
- IFD0 CameraSerialNumber: "91702442"
- IFD0 LensInfo: [[350, 10], [350, 10], [20, 10], [20, 10]]
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 14
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [1024, 1024, 1024, 1024]
- raw WhiteLevel: 16383
- raw DefaultCropOrigin: [12, 14]
- raw DefaultCropSize: [6016, 4012]
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw ActiveArea: [2, 20, 4042, 6060]
- raw OpcodeList3: {"hex": "00000001000000010103000000000000000000a4000000033ff0006de46e7eeebfa6c297aa949cadbf61b5e5c74a022c3f71162eabd245d6000000000000000000000000000000003feffef
- raw NewSubfileType: 0
- raw _shape: [4042, 6080]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `Sigma`, Model `Sigma BF`, UniqueCameraModel `Sigma BF`, Software `Sigma BF Ver1.00.33FC`
- DNGVersion [1, 7, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 4096 (scaled per bit depth); OpcodeList3: harvested

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [10, 2000], [1, 125], [10, 1000], [10, 500], [1, 40], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1300, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 5000, 6400]
- Lens pool (2): LUMIX S 20-60/F3.5-5.6; 35mm F2 DG | Contemporary 020
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['91']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `sigma_bf-native`: pins 6016x4012 (native sensor geometry)

Base `--camera-profile=sigma_bf` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
