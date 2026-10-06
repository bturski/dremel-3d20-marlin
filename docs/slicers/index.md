# What every slicer needs

These settings apply no matter which slicer you use. Get them right and any slicer that writes Marlin G-code will work. The PrusaSlicer and Cura pages show exactly where each one lives.

## Required settings

| Setting | Value | Why |
|---|---|---|
| Bed size | 230 x 150 mm | The 3D20 build plate |
| Max height | 140 mm | Marlin's Z limit |
| Origin | **Center of the bed** | Marlin puts X0 Y0 in the middle. With a corner origin, every part lands in the back right and runs into the limits |
| Heated bed | **None** | The 3D20 has no heated bed. Bed temperature must be 0 so the slicer never waits for it |
| G-code flavor | Marlin (Marlin 2 if offered) | Matches the firmware |
| Output | Plain `.gcode` | Marlin can't read `.g3drem` or PrusaSlicer's binary `.bgcode` |
| Nozzle | 0.4 mm | Stock nozzle |
| Filament | 1.75 mm | Stock filament size |
| Start and end G-code | From this guide | Stock Dremel G-code is unsafe under Marlin. See [Start and end G-code](gcode.md) |
| Retraction speed | 25 mm/s or less | The firmware caps the extruder at 27 mm/s |

## Recommended starting values

These are good first values for PLA. Tune from here.

| Setting | Value | Why |
|---|---|---|
| Nozzle temperature | 215 first layer, 210 after | A warm first layer helps on a cold bed |
| Max nozzle temperature | 230 | The stock hotend's practical limit. The firmware allows more, but the hotend isn't built for it |
| Layer height | 0.20 mm, first layer 0.25 mm | Good balance of quality and time |
| Retraction | 1.0 mm at 25 mm/s, Z hop 0.2 mm | Direct drive needs very little |
| First layer speed | 20 mm/s | The biggest single help for adhesion |
| Outer wall speed | 30 mm/s | Cleaner surfaces |
| Inner wall speed | 40 mm/s | |
| Infill speed | 60 mm/s | Stays inside what the hotend can melt |
| Travel speed | 120 mm/s | |
| Acceleration | 300 first layer, 500 outer walls, 800 default, 1000 infill and travel | The firmware's limit is 1000 |
| Part fan | 100% from layer 2 | The fan is small, so run it full |
| Max flow | 7 mm³/s | Keeps fast moves from under-extruding |

## Why acceleration matters here

The firmware's built-in print acceleration is only 200 mm/s². If your slicer doesn't send its own acceleration values, every print runs at 200. That is slow, and the slicer's time estimate will be far too short. Both profiles in this guide send acceleration per feature.

## Pick your slicer

- [PrusaSlicer](prusaslicer.md). Import one file and you are done.
- [UltiMaker Cura](cura.md). Copy two files into Cura's settings folder, then add the printer.

Using another slicer? Copy the values above and the G-code from [Start and end G-code](gcode.md). If you write it up, we'd like to add it. See [Contributing](../contributing.md).
