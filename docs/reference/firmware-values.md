# Firmware values

The defaults in the 3D20 build of [moonglow/FlashForge_Marlin](https://github.com/moonglow/FlashForge_Marlin) (Marlin 2.0.9.x). They come from the project's `Configuration.h` and `Configuration_adv.h` with the Dremel 3D20 option turned on.

Use these when you set up a slicer's machine limits, or to check what `M503` reports. Values you change and save with `M500` replace these.

## Motion

| Setting | Value | Change with |
|---|---|---|
| Steps per mm X, Y | 88.909720 (black pulleys) | `M92 X Y` |
| Steps per mm Z | 400 | `M92 Z` |
| Steps per mm E | 96.275202 | `M92 E` |
| Max feedrate X, Y, Z, E | 300, 300, 20, 27 mm/s | `M203` |
| Max acceleration X, Y, Z, E | 1000, 1000, 150, 4000 mm/s² | `M201` |
| Print acceleration | 200 mm/s² | `M204 P` |
| Retract acceleration | 1000 mm/s² | `M204 R` |
| Travel acceleration | 1000 mm/s² | `M204 T` |
| Junction deviation | 0.013 mm | `M205 J` |
| Classic jerk | Off. Junction deviation is used instead | |
| E jerk | 5 mm/s | `M205 E` |
| S-curve acceleration | On in the standard build, off in the `la` build | Rebuild only |
| Linear Advance | Off in the standard build. In the `la` build, K = 0 | `M900 K` |

The firmware limits edits from the screen or `M201` to twice the maximum acceleration.

## Geometry

| Setting | Value |
|---|---|
| Bed size | 230 x 150 mm |
| X travel | -111.0 to 158.5 |
| Y travel | -76.23 to 76.23 |
| Z travel | 0 to 140 |
| Home direction | X max, Y max, Z min |
| Software endstops | On, minimum and maximum |

## Temperature

| Setting | Value |
|---|---|
| Hotend sensor | K-type thermocouple through ADS1118 |
| Hotend maximum | 280 °C in firmware. Keep prints at 230 °C or below on the stock hotend |
| Cold extrusion limit | 170 °C |
| Heated bed | None |
| Thermal protection | On for the hotend |
| PID control | On. Tune with `M303` |

## Features

| Feature | State | Notes |
|---|---|---|
| Mesh bed leveling | On, manual, 3 x 3 grid, 10 mm inset | Turn on with `M420 S1` |
| Manual probe start height | 0.2 mm | |
| Mesh edit step | 0.025 mm | |
| Settings storage (EEPROM) | On | `M500` save, `M501` load, `M502` defaults, `M503` show |
| Arc moves (G2, G3) | On | Turn on arc fitting in PrusaSlicer |
| Firmware retraction (G10, G11) | Off | Use slicer retraction |
| Power loss recovery | Off | Only built for the FlashForge Inventor |
| Filament change (M600) | On | |
| Nozzle park | On | |
| Filament runout sensor | Built in, off by default | `M412` |
| Print progress (M73) | Off | Turn off "Supports remaining times" in PrusaSlicer |
| Object cancel (M486) | Off | Use OctoPrint comments for labels |
| Babystepping | Off | |
| Firmware update trigger | On (3D20 and Dreamer only) | Writes the update flag at `0x0800C000` |

## Commands you'll use

| Command | What it does |
|---|---|
| `M503` | Print all current settings |
| `M500` | Save settings |
| `M502` | Load firmware defaults (then `M500` to save them) |
| `M303 E0 S210 C8 U1` | Tune the hotend at 210 °C and apply the result |
| `M420 S1 V` | Turn on the saved mesh and print it |
| `M92 E96.28` | Set extruder steps per mm |

See the [Marlin G-code reference](https://marlinfw.org/meta/gcode/) for every command.
