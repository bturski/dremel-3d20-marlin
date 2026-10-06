# PrusaSlicer

Written for PrusaSlicer 2.8 and 2.9. Older versions work too, but a few settings have different names. Those are noted below.

## Option A: import the profile (recommended)

1. Download [Dremel3D20_Marlin_PrusaSlicer.ini](../downloads/prusaslicer/Dremel3D20_Marlin_PrusaSlicer.ini). Right click and choose **Save link as** if your browser opens it as text.
2. In PrusaSlicer, go to **File > Import > Import Config Bundle** and pick the file.
3. PrusaSlicer adds three presets and selects them:
    - Printer: **Dremel 3D20 Marlin**
    - Print: **Dremel 3D20 Marlin 0.20mm QUALITY**
    - Filament: **Dremel 3D20 Marlin PLA**
4. If you haven't saved a mesh yet (see [First setup](../firmware/first-setup.md#4-build-and-save-a-mesh)), open **Printer Settings > Custom G-code** and delete the `M420 S1` line.
5. Slice a small test part and check that it sits in the middle of the bed preview.

The print and filament presets only show up while the Dremel printer preset is selected. That keeps them from being used on another printer by mistake.

To make your own variations, change a setting and use **Save preset** with a new name. Re-importing the bundle later overwrites presets with the same names, so give yours different names.

## Option B: set it up by hand

Start from a new custom printer: **Configuration > Configuration Wizard > Custom Printer**. Then switch to **Expert** mode in the top right corner, because some settings below are hidden in Simple mode.

Each table shows the PrusaSlicer default, what to change it to, and why. Rows marked **Required** will cause failed prints or crashes if skipped.

### Printer Settings

| Where | Setting | Default | Set to | Why |
|---|---|---|---|---|
| General > Size and coordinates | Bed shape: Size | 200 x 200 | X 230, Y 150 | **Required.** The build plate |
| General > Size and coordinates | Bed shape: Origin | 0, 0 | X 115, Y 75 | **Required.** Marlin's origin is the bed center |
| General > Size and coordinates | Max print height | 200 | 140 | **Required.** Marlin's Z limit |
| General > Firmware | G-code flavor | RepRap/Sprinter | Marlin 2 | **Required.** Correct acceleration commands |
| General > Firmware | Supports binary G-code | Off | Off | **Required.** Marlin can't read `.bgcode` |
| General > Firmware | Supports remaining times | Off | Off | This build doesn't support `M73` progress |
| General > Advanced | Use relative E distances | Off | On | The start G-code is written for it |
| General > Thumbnails | G-code thumbnails | Empty | Empty | The screen can't show them |
| Custom G-code | Start G-code | Short default | [See G-code page](gcode.md#prusaslicer) | **Required.** Safe start, mesh, purge line |
| Custom G-code | End G-code | Short default | [See G-code page](gcode.md#prusaslicer) | **Required.** Lowers the bed before parking |
| Machine limits | How to apply limits | Varies | Use for time estimate | Firmware keeps control, estimates stay accurate |
| Machine limits | Max feedrates X, Y, Z, E | Prusa values | 300, 300, 20, 27 | Match the firmware |
| Machine limits | Max accelerations X, Y, Z, E | Prusa values | 1000, 1000, 150, 4000 | Match the firmware |
| Machine limits | Max acceleration when extruding, retracting, travel | Prusa values | 1000 each | Match the firmware |
| Machine limits | Jerk X, Y, Z, E | Prusa values | 10, 10, 0.3, 5 | Estimate only. The firmware uses junction deviation |
| Extruder 1 > Size | Nozzle diameter | 0.4 | 0.4 | Stock nozzle |
| Extruder 1 > Layer height limits | Min, Max | 0.07, 0 | 0.08, 0.30 | Keeps variable layer height sensible |
| Extruder 1 > Retraction | Length | 2 mm | 1 mm | **Required.** Long retractions jam a direct drive |
| Extruder 1 > Retraction | Retraction speed | 40 mm/s | 25 mm/s | **Required.** The firmware caps E at 27 |
| Extruder 1 > Retraction | Deretraction speed | 0 | 20 mm/s | Fewer blobs at seams |
| Extruder 1 > Retraction | Wipe while retracting | Off | On | Cleaner seams |
| Extruder 1 > Travel lift | Lift height | 0 | 0.2 mm | Keeps the nozzle off finished surfaces |
| Extruder 1 > Travel lift | Ramping lift | Off | Off | Z is slow on this printer |

!!! note "Older PrusaSlicer versions"
    Before 2.8, **Lift height** was called **Lift Z** and sat in the Retraction section.

### Filament Settings (PLA)

| Where | Setting | Default | Set to | Why |
|---|---|---|---|---|
| Filament | Diameter | 1.75 | 1.75 | |
| Filament > Temperature | Nozzle first layer, other layers | 200, 200 | 215, 210 | Better first layer on a cold bed |
| Filament > Temperature | Bed first layer, other layers | 0, 0 | 0, 0 | **Required.** No heated bed |
| Advanced | Max volumetric speed | 0 | 7 mm³/s | Protects the small hotend |
| Filament | Extrusion multiplier | 1 | Calibrate later | Usually ends up 0.95 to 1.0 |
| Cooling | Keep fan always on | Off | On | |
| Cooling | Min fan speed | 35% | 100% | The fan is weak |
| Cooling | Disable fan for the first | 3 layers | 1 layer | |
| Cooling | Slow down if layer print time is below | 5 s | 10 s | Small parts cool between layers |

### Print Settings (0.20 mm)

| Where | Setting | Default | Set to | Why |
|---|---|---|---|---|
| Layers and perimeters | Layer height | 0.3 | 0.2 | |
| Layers and perimeters | First layer height | 0.35 | 0.25 | Forgiving on a hand leveled bed |
| Layers and perimeters | Solid layers top, bottom | 3, 3 | 5, 4 | Solid tops at 0.2 mm |
| Infill | Fill density | 20% | 15% | Plenty for most parts |
| Infill | Fill pattern | Stars | Gyroid | No nozzle strikes on curled infill |
| Skirt and brim | Skirt loops, distance | 1, 6 mm | 2, 3 mm | Primes the nozzle and shows leveling problems |
| Skirt and brim | Brim width | 0 | 5 mm when needed | Use for small or long parts |
| Advanced | Elephant foot compensation | 0 | 0.1 mm | |
| Speed | Perimeters | 60 | 40 | |
| Speed | Small perimeters | 15 | 20 | |
| Speed | External perimeters | 50% | 30 | |
| Speed | Infill | 80 | 60 | Inside the hotend's limit |
| Speed | Solid infill, top solid infill | 20, 15 | 45, 30 | |
| Speed | Support, bridges, gap fill | 60, 60, 20 | 40, 30, 25 | |
| Speed | Travel | 130 | 120 | |
| Speed | First layer speed | 30 | 20 | Adhesion |
| Speed > Acceleration control | **Default (set this first)** | 0 | 800 | The other acceleration fields stay greyed out while this is 0 |
| Speed > Acceleration control | External perimeters, perimeters | 0, 0 | 500, 800 | |
| Speed > Acceleration control | Infill, solid infill, top solid infill | 0, 0, 0 | 1000, 800, 600 | |
| Speed > Acceleration control | Bridges, first layer, travel | 0, 0, 0 | 500, 300, 1000 | |
| Output options | Label objects | OctoPrint comments | OctoPrint comments | Don't use Firmware-specific. This build has no `M486` |
| Advanced > Arc fitting | Arc fitting | Disabled | Enabled | The firmware supports arcs. Smaller files, smoother curves |

## Check your setup

Slice a 20 mm test cube and look at the G-code preview:

- The cube sits in the middle of the bed.
- The purge lines run along the left edge, front to back.
- No `M190` or `M140` lines appear (open the G-code in a text editor and search).
- `M204` lines appear as features change. That means acceleration is being sent.
