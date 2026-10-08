# Print problems

Common problems after switching to Marlin, and how to fix them.

## Parts print in the wrong place

**Symptoms:** Parts land in the back right corner, get cut off, or the printer reports "move out of range."

**Cause:** The slicer thinks the origin is the front left corner. Marlin puts it at the bed center.

**Fix:**

- PrusaSlicer: **Printer Settings > General > Bed shape**, set **Origin** to X 115, Y 75.
- Cura: **Machine Settings**, turn on **Origin at center**.
- Keep parts about 4 mm in from the left edge. Marlin stops X at -111, and the bed edge is at -115.

## Printing starts before the nozzle is hot

**Cause:** The start G-code uses `M104` to set the temperature. In stock firmware `M104` waits. In Marlin it doesn't.

**Fix:** Use the start G-code from this guide. It sets the temperature with `M104` early, then waits with `M109` before printing. See [Start and end G-code](../slicers/gcode.md).

## Motors run hot or loud

**Stop the print and turn the printer off.**

**Cause:** Almost always `M907 X100 Y100 Z60 A100` (or similar) in the start G-code, copied from a stock Dremel profile. Marlin reads these numbers as amps, so every motor runs at maximum current.

**Fix:**

1. Remove every `M907` line from your slicer's G-code boxes.
2. Let the motors cool.
3. Restore the default currents by restarting the printer. If you saved settings while the bad values were active, run `M502` then `M500`.

If you want to change motor current on purpose, see the project's [stepper current wiki page](https://github.com/moonglow/FlashForge_Marlin/wiki/Tune-stepper-motor-current).

## First layer won't stick

The 3D20 has no heated bed, so the first layer needs more care than on most printers.

1. **Level and save a mesh.** See [First setup](../firmware/first-setup.md#4-build-and-save-a-mesh). Make sure `M420 S1` is in your start G-code.
2. **Slow down.** First layer speed 20 mm/s.
3. **Warm up.** First layer nozzle temperature 215 °C.
4. **Keep the fan off for layer 1.**
5. **Clean the bed.** Wipe it with isopropyl alcohol. Fingerprints are the most common cause.
6. **Add grip.** A thin layer of glue stick or blue painter's tape helps a lot on a cold bed.
7. **Use a brim** for small parts and long parts.
8. **Check the gap.** If the first lines look round and separate, the nozzle is too high. Redo the mesh with a little more drag on the paper, then save with `M500`. This build doesn't include babystepping, so you can't adjust the height during a print.

## Stringing, blobs, or clogs

**Cause:** Retraction settings meant for a Bowden printer. The 3D20 is direct drive and needs short retractions.

**Fix:**

- Retraction length 1.0 mm. Go no higher than 1.5 mm.
- Retraction speed 25 mm/s. The firmware caps the extruder at 27 mm/s, so higher values don't help.
- Turn on wipe (PrusaSlicer) or combing (Cura).
- Lower the temperature in 5 degree steps if stringing continues.

Long retractions pull hot plastic up into the cold part of the hotend. It hardens there and causes clogs.

## Prints are slow or the time estimate is wrong

**Cause:** The slicer isn't sending acceleration values. The firmware's own default is only 200 mm/s², so everything moves slowly.

**Fix:**

- PrusaSlicer: set **Default** acceleration first (800), then the others. They stay greyed out while Default is 0.
- Cura: turn on **Enable Acceleration Control**.
- Set the slicer's machine limits to match the firmware, so its time estimate is accurate. See [Firmware values](../reference/firmware-values.md).

## PrusaSlicer says relative extruder addressing needs G92 E0

**Message:** *Relative extruder addressing requires resetting the extruder position at each layer to prevent loss of floating point accuracy. Add "G92 E0" to layer_gcode.*

**Cause:** **Use relative E distances** is on, but nothing resets the extruder at each layer. Versions of our PrusaSlicer bundle from before 2026-10-08 had this gap.

**Fix:** Either re-import the [current bundle](../reference/downloads.md#slicer-profiles), or open **Printer Settings > Custom G-code > Before layer change G-code** and add `G92 E0` on its own line. Save the printer preset. See [Start and end G-code](../slicers/gcode.md#prusaslicer).

## Unknown command messages

**Cause:** Leftover stock Dremel or FlashForge codes such as `M132`, `M6`, or `M108`, or `M73` progress codes Marlin wasn't built for.

**Fix:** Replace your start and end G-code with the versions in this guide. In PrusaSlicer, turn off **Supports remaining times**.

## Mesh doesn't load

**Symptom:** "Failed to enable Bed Leveling" at the start of a print.

**Fix:**

1. Build the mesh again and run `M500` to save it.
2. Check with `M420 S1 V`. You should see a 3 by 3 grid.
3. If you don't want to use a mesh, remove `M420 S1` from the start G-code.

## File doesn't show up

| Check | Fix |
|---|---|
| File type | Must end in `.gcode`. Not `.g3drem`, not `.bgcode`. In PrusaSlicer, turn off **Supports binary G-code** |
| Card format | FAT32 works best. Cards over 32 GB often come formatted as exFAT |
| Card inserted after start-up | Use the menu to refresh or re-initialize the card |

## Under-extrusion on fast moves

**Cause:** The stock hotend can only melt so much plastic per second.

**Fix:** Cap the flow. PrusaSlicer: **Filament Settings > Advanced > Max volumetric speed** 7 mm³/s. Cura doesn't have a direct cap, so keep infill speed at or below 60 mm/s at 0.2 mm layers.
