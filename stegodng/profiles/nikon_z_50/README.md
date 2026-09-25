# Nikon Z 50
Profile slug: `nikon_z_50`  
EXIF Make/Model: `NIKON CORPORATION` / `NIKON Z 50`
Native geometry: 5600x3728 most common decoded dims across 6 sample(s)  
Suggested bit depth: 14  
CFA: unknown  
Crop factor: 1.5  
Calibration source: `exif-plus-fallback`

## Sample metadata (from dpreview-raw)
Representative file: `Nikon Nikkor Z DX 24mm F1.7/4928099113.nef`
Files seen: 6 (Nikon Nikkor Z DX 24mm F1.7/4928099113.nef, Nikon Nikkor Z DX 24mm F1.7/9591944789.nef, Nikon Z50/5650940899.nef, Nikon Z50/5930443010.nef, ...)
Software strings observed: Ver.01.00, Ver.02.40
Lenses observed: NIKKOR Z 24mm f/1.8 S; NIKKOR Z DX 16-50mm f/3.5-6.3 VR; NIKKOR Z DX 24mm f/1.7; 56mm F1.4 DC DN | Contemporary 018
ISO observed: 100
Exposure observed: 1/160 s, 1/1600 s, 1/3200 s, 1/400 s, 1/800 s
F-number observed: F1.4, F1.7, F2.8, F5, F6.3
Focal length observed: 22.5 mm, 24.0 mm, 56.0 mm
Serial tags present: Exif.Nikon3.SerialNumber, Exif.Photo.BodySerialNumber (observed serial formats)

## Static fields (identical in every output file)
- Make `NIKON CORPORATION`, Model `NIKON Z 50`, UniqueCameraModel `NIKON Z 50`, Software `Ver.02.40`
- DNGVersion default 1.4, CalibrationIlluminants 17/21
- ColorMatrix1/2: GFX reference fallback
- BlackLevel ref 256 (scaled per bit depth); OpcodeList3: GFX reference fallback

## Randomized per file (seeded)
- DateTime*, OffsetTime*, SubSecTime* (2019-2024 window)
- ExposureTime pool: [[1, 3200], [1, 1600], [10, 8000], [1, 800], [10, 4000], [1, 400], [10, 2000], [1, 160], [10, 1000], [10, 500], [10, 250], [10, 125], [10, 60], [10, 30], [10, 21], [10, 17], [10, 16], [10, 8], [15, 10], [10, 5], [20, 10], [10, 4], [30, 10], [10, 3], [50, 10], [10, 2], [60, 10], [10, 1]]
- FNumber pool: [[140, 100], [170, 100], [200, 100], [250, 100], [280, 100], [320, 100], [400, 100], [500, 100], [560, 100], [630, 100], [710, 100], [800, 100], [1100, 100], [1600, 100], [2200, 100], [3200, 100]]
- ISO pool: [50, 64, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 3200, 6400]
- Lens pool (4): NIKKOR Z 24mm f/1.8 S; NIKKOR Z DX 16-50mm f/3.5-6.3 VR; NIKKOR Z DX 24mm f/1.7; 56mm F1.4 DC DN | Contemporary 018
- FocalLength + 35mm equivalent (x1.5), Metering [2, 3, 5], ExposureProgram [1, 2, 3, 4]
- Camera/lens serials (prefixes ['20', '30']), ImageNumber, AsShotNeutral, BaselineExposure, Brightness, ExposureBias

## Sub-profiles
- `nikon_z_50-native`: pins 5600x3728 (native sensor geometry)

Base `--camera-profile=nikon_z_50` auto-sizes like the default profile but stamps this camera's Make/Model/lenses.

## Plausible-deniability notes
Output is a converted-to-DNG story: the payload carrier claims whatever RAW the user converted. Fidelity limits an inspector could spot:
- Color matrices / opcode list are GFX reference values, not this camera's: a forensic comparison against Adobe DNG Converter output for this body would mismatch.
- Native geometry includes masked margins; exact active-area dimensions may differ by a few dozen pixels.
