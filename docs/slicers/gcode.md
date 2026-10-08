# Start and end G-code

Your slicer adds start G-code before every print and end G-code after it. Both need to be written for Marlin. This page has the versions used by our profiles, explains each line, and lists the stock Dremel codes you must not reuse.

## What the start G-code does

1. Sets absolute positioning and turns the part fan off.
2. Starts heating the nozzle, so it warms up while the printer homes.
3. Homes all axes. X and Y go to the back right, Z raises the bed to the nozzle.
4. Turns on the saved bed mesh with `M420 S1`.
5. Moves to the front left corner and waits for full temperature with `M109`.
6. Draws two purge lines along the left edge to prime the nozzle.
7. Retracts a little, lifts, and resets the extruder position.

There is no bed heating. The 3D20 has no heated bed, and asking Marlin to wait for one can stall the print.

!!! note "No saved mesh yet?"
    If you haven't built and saved a mesh (see [First setup](../firmware/first-setup.md#4-build-and-save-a-mesh)), delete the `M420 S1` line. Marlin prints an error otherwise. The print still runs, just without mesh correction.

## PrusaSlicer

Paste these into **Printer Settings > Custom G-code**. They assume **Use relative E distances** is on.

**Start G-code** ([download](../downloads/gcode/prusaslicer-start.gcode))

```gcode
--8<-- "prusaslicer-start.gcode"
```

**End G-code** ([download](../downloads/gcode/prusaslicer-end.gcode))

```gcode
--8<-- "prusaslicer-end.gcode"
```

The end G-code lowers the bed 10 mm below the last layer, capped at the 140 mm limit, before parking. That keeps the nozzle from dragging across the finished part.

**Before layer change G-code**

```gcode
;BEFORE_LAYER_CHANGE
G92 E0
;[layer_z]
```

With relative extrusion on, PrusaSlicer requires a `G92 E0` at every layer change. It resets the extruder position so tiny rounding errors don't add up over a long print. Without it, PrusaSlicer refuses to slice and shows: *Relative extruder addressing requires resetting the extruder position at each layer to prevent loss of floating point accuracy.*

## Cura

Paste these into **Preferences > Printers > Machine Settings**. They purge with relative extrusion, then switch back to absolute extrusion, which is Cura's default.

**Start G-code** ([download](../downloads/gcode/cura-start.gcode))

```gcode
--8<-- "cura-start.gcode"
```

**End G-code** ([download](../downloads/gcode/cura-end.gcode))

```gcode
--8<-- "cura-end.gcode"
```

## Stock Dremel codes to avoid

The stock Dremel profile sends commands that mean something different in Marlin. The firmware project warns about this on its [attention page](https://github.com/moonglow/FlashForge_Marlin/wiki/%5BATTENTION%5D-Avoid-using-FlashForge-original-firmware-G-Codes). A typical stock start block looks like this:

```gcode
G90
G28
M132 X Y Z A
G1 Z100 F3300
G1 X-110.5 Y-74 F6000
M6 T0
M907 X100 Y100 Z60 A100
G1 Z0.6 F3300
G4 P2000
M108 T0
```

| Code | In stock firmware | In Marlin | Risk |
|---|---|---|---|
| `M907 X100 Y100 Z60 A100` | Sets motor current with raw numbers | Sets motor current in **amps** | **High.** Every motor runs at maximum current. Motors overheat and can melt their plastic mounts. Newer builds reject odd values, but don't rely on that |
| `M104` | Sets temperature **and waits** | Sets temperature and **doesn't wait** | Printing starts with a cold nozzle. Use `M109` to wait |
| `M140` | Sets bed temperature and waits | Sets bed temperature, doesn't wait | Not needed on a 3D20 |
| `M132` | Loads stored positions | Not supported | Does nothing, prints "Unknown command" |
| `M6`, `M108 T0` | Tool select and heater control | Not supported the same way | Does nothing or behaves unexpectedly |
| `M18` | Motors off | Motors off | Fine, but `M84` is the usual choice |

If a line came from a Dremel or FlashForge profile, check it against the [Marlin G-code reference](https://marlinfw.org/meta/gcode/) before you use it. This also applies to pause, color change, and layer change G-code boxes.

## Advanced: customizing

- **Purge position.** The purge runs at X -108 and -107.4, close to Marlin's left limit of X -111. If you move it, stay inside X -111 to 158.5 and Y -76 to 76.
- **Purge length.** Two lines of 10 mm and 8 mm of filament. Shorten them if you see a blob at the end.
- **Waiting at the corner.** The nozzle heats over the front left corner so any ooze lands near the purge line, not on the bed center.
- **Relative extrusion.** PrusaSlicer stays in relative mode (`M83`). Cura switches back to absolute (`M82`). If you turn on relative extrusion in Cura, remove the `M82` line.
