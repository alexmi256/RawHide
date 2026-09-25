# Ricoh GR II
Profile slug: `ricoh_gr_ii`  
EXIF Make/Model: `RICOH IMAGING COMPANY, LTD.` / `GR II`
Native geometry: 4944x3280 most common decoded dims across 2 sample(s)  
Suggested bit depth: 12  
CFA: RGGB  
Crop factor: 1.0  
Calibration source: `harvested-dng`

## Sample metadata (from dpreview-raw)
Representative file: `Ricoh GR II/8487721668.dng`
Files seen: 2 (Ricoh GR II/8487721668.dng, Ricoh GR II/9471479438.dng)
Software strings observed: GR Firmware Ver 01.10
Lenses observed: GR LENS
ISO observed: 200, 400
Exposure observed: 1/30 s, 1/500 s
F-number observed: F5.6, F8
Focal length observed: 18.3 mm
Serial tags present: none (generic fallback (no serial tags observed))

## Harvested DNG calibration
- IFD0 Make: "RICOH IMAGING COMPANY, LTD."
- IFD0 Model: "GR II"
- IFD0 DNGVersion: {"hex": "01030000"}
- IFD0 DNGBackwardVersion: {"hex": "01010000"}
- IFD0 UniqueCameraModel: "GR II"
- IFD0 ColorMatrix1: [[31702, 65536], [-11198, 65536], [2937, 65536], [-25246, 65536], [63107, 65536], [32449, 65536], [-605, 65536], [2096, 65536], [46890, 65536]]
- IFD0 ColorMatrix2: [[30916, 65536], [-5569, 65536], [-2824, 65536], [-32615, 65536], [83919, 65536], [15838, 65536], [-4201, 65536], [9659, 65536], [40261, 65536]]
- IFD0 CalibrationIlluminant1: 17
- IFD0 CalibrationIlluminant2: 21
- IFD0 AsShotNeutral: [1024, 2997, 1024, 1024, 1024, 1731]
- IFD0 BaselineExposure: [-20, 100]
- IFD0 BaselineNoise: [400, 100]
- IFD0 BaselineSharpness: [133, 100]
- IFD0 LinearResponseLimit: [100, 100]
- IFD0 LensInfo: [[1830, 100], [1830, 100], [28, 10], [28, 10]]
- IFD0 MakerNoteSafety: 0
- IFD0 BitsPerSample: [8, 8, 8]
- raw BitsPerSample: 12
- raw SamplesPerPixel: 1
- raw PhotometricInterpretation: 32803
- raw BlackLevel: [0, 1]
- raw WhiteLevel: 4095
- raw DefaultScale: [16777216, 16777216, 16777216, 16777216]
- raw DefaultCropOrigin: [8, 1, 8, 1]
- raw DefaultCropSize: [4928, 1, 3264, 1]
- raw CFAPlaneColor: {"hex": "000102"}
- raw CFALayout: 1
- raw CFARepeatPatternDim: [2, 2]
- raw CFAPattern: {"hex": "00010102"}
- raw AntiAliasStrength: [1, 1]
- raw ActiveArea: [0, 0, 3280, 4944]
- raw NewSubfileType: 0
- raw _shape: [3280, 4960]
- raw _dtype: "uint16"
- raw _photometric: 32803

## Static fields (identical in every output file)
- Make `RICOH IMAGING COMPANY, LTD.`, Model `GR II`, UniqueCameraModel `GR II`, Software `GR Firmware Ver 01.10`
- DNGVersion [1, 3, 0, 0], CalibrationIlluminants 17/21
- ColorMatrix1/2: harvested from DNG
- BlackLevel ref 1 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[10, 8000], [1, 500], [10, 4000], [10, 2000], [10, 1000], [10, 500], [1, 30], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [560, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (1): GR LENS
- FocalLength + 35mm equivalent (x1.0), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['1A', '4E', '7B', 'C2']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `ricoh_gr_ii-native`: pins 4944x3280 (native sensor geometry)

Base `--camera-profile=ricoh_gr_ii` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
