# First setup after install

Do these once, right after Marlin is installed. They take about 20 minutes.

You will send a few G-code commands. Two ways to do that:

- **From a PC:** connect USB and use a terminal such as [Pronterface](https://www.pronterface.com/) or the terminal in OctoPrint. Connect at 115200 baud.
- **From the printer:** most settings also have a menu item. We list the menu path where it helps.

`M500` saves settings so they survive a restart. `M503` prints the current settings so you can check them.

## 1. Reset stored settings

Marlin keeps settings in memory that survives power off. Start clean.

```gcode
M502   ; load the firmware defaults
M500   ; save them
```

## 2. Tune the hotend temperature (PID)

Stock firmware tuned the heater its own way. Marlin needs its own tune, or the temperature can swing during prints.

1. Make sure the nozzle is clear and nothing is on the bed.
2. Turn the part fan on, since it runs during real prints:

    ```gcode
    M106 S255
    ```

3. Run the tune at your normal printing temperature. It cycles the heater 8 times.

    ```gcode
    M303 E0 S210 C8 U1
    ```

4. Wait until the terminal reports that the tune finished. `U1` applies the new values.
5. Save, and turn the fan off:

    ```gcode
    M500
    M107
    ```

## 3. Level the bed with the screws

This gets the bed roughly flat before you build a mesh.

1. Open **User menu > Bed leveling (3-point)**. The printer homes and moves the nozzle over each of the three adjustment screws, then to the center.
2. At each stop, slide a sheet of printer paper under the nozzle. Turn the screw until you feel light drag on the paper.
3. Press the screen to move to the next point. Do two full passes. The center stop is only a check, since there is no screw there.

## 4. Build and save a mesh

The firmware uses manual mesh bed leveling with a 3 by 3 grid, 10 mm in from the edges.

1. Go to **Motion > Bed Leveling > Level Bed** (the exact menu name can differ slightly between screen styles).
2. The printer homes and moves to the first point at 0.2 mm above the bed.
3. Use the paper test again. Adjust the height on screen (it moves in 0.025 mm steps) until you feel light drag, then confirm.
4. Repeat for all 9 points.
5. Save:

    ```gcode
    M500
    ```

6. Check that the mesh loads:

    ```gcode
    M420 S1 V
    ```

    You should see a 3 by 3 grid of small numbers. If you see "Failed to enable Bed Leveling," the mesh wasn't saved. Repeat the steps.

The start G-code in this guide runs `M420 S1` before every print, which turns this mesh on.

## 5. Check the extruder (E-steps)

The firmware default is 96.275 steps per mm. Most printers are close. Checking takes five minutes.

1. Heat the nozzle: `M109 S210`
2. Measure 120 mm up the filament from where it enters the extruder, and mark it.
3. Extrude 100 mm slowly:

    ```gcode
    M83
    G1 E100 F100
    ```

4. Measure from the extruder to your mark. If 20 mm remain, it's perfect.
5. If not, work out the new value:

    ```
    new value = 96.275 x 100 / (120 - remaining length)
    ```

6. Set and save it. For example, if 18 mm remain, the new value is 96.275 x 100 / 102 = 94.39:

    ```gcode
    M92 E94.39
    M500
    ```

## 6. Advanced: check X and Y steps

The firmware assumes the **black** belt pulleys (88.91 steps per mm). Some FlashForge family printers use **silver** pulleys (94.14 steps per mm). If a 100 mm test part comes out about 94 mm, your printer has the silver pulleys. Fix it with:

```gcode
M92 X94.14 Y94.14   ; only if your test part proves you need it
M500
```

## Done

Run `M503` and save the output somewhere. It is a record of your working settings.

Next: [set up your slicer](../slicers/index.md).
