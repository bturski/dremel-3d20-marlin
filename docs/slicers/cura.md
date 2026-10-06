# UltiMaker Cura

Written for Cura 5.x.

Cura's built-in Dremel 3D20 profile targets the **stock** firmware. Don't use it with Marlin. Use our printer definition, or set up a custom printer.

## Option A: install the printer definition (recommended)

The definition adds a printer called **Dremel 3D20 (Marlin)** with the bed size, origin, G-code, speeds, acceleration, and retraction already set.

1. Download [Dremel3D20_Marlin_Cura.zip](../downloads/cura/Dremel3D20_Marlin_Cura.zip) and unzip it. It holds two files:
    - `dremel_3d20_marlin.def.json` (the printer)
    - `dremel_3d20_marlin_extruder_0.def.json` (its extruder)
2. In Cura, go to **Help > Show Configuration Folder**. A file window opens.
3. Open the `definitions` folder inside it. If there isn't one, create it with exactly that name.
4. Copy **both** files into `definitions`.
5. Close Cura completely and start it again.
6. Go to **Settings > Printer > Add Printer**, then **Non UltiMaker printer > Add a non-networked printer**. Find **Dremel** in the list and choose **Dremel 3D20 (Marlin)**.
7. If you haven't saved a mesh yet (see [First setup](../firmware/first-setup.md#4-build-and-save-a-mesh)), open **Preferences > Printers > Machine Settings** and delete the `M420 S1` line from the start G-code.

### Set the temperature

Cura takes nozzle temperature from the material, not the printer. Generic PLA uses 200 °C. For the 3D20:

1. Open the print settings panel and click **Custom**.
2. Search for **Printing Temperature** and set 210.
3. Search for **Printing Temperature Initial Layer** and set 215.
4. Save it: **Profile > Create profile from current settings**, and give it a name like "3D20 PLA".

## Option B: set up a custom printer

1. Go to **Settings > Printer > Add Printer**, then **Non UltiMaker printer > Add a non-networked printer**.
2. Choose **Custom > Custom FFF printer** and name it "Dremel 3D20 Marlin".
3. In **Machine Settings**, set:

| Tab | Setting | Value |
|---|---|---|
| Printer | X (Width) | 230 mm |
| Printer | Y (Depth) | 150 mm |
| Printer | Z (Height) | 140 mm |
| Printer | Build plate shape | Rectangular |
| Printer | Origin at center | **On** |
| Printer | Heated bed | **Off** |
| Printer | G-code flavor | Marlin |
| Printer | Start G-code | [See G-code page](gcode.md#cura) |
| Printer | End G-code | [See G-code page](gcode.md#cura) |
| Extruder 1 | Nozzle size | 0.4 mm |
| Extruder 1 | Compatible material diameter | 1.75 mm |

4. Close Machine Settings. Click **Custom** in the print settings panel and set these. Use the search box to find each one. Some are hidden until you search or change setting visibility to **All**.

| Setting | Value | Why |
|---|---|---|
| Layer Height | 0.2 mm | |
| Initial Layer Height | 0.25 mm | Forgiving first layer |
| Top Thickness, Bottom Thickness | 1.0 mm, 0.8 mm | Solid surfaces |
| Infill Density | 15% | |
| Infill Pattern | Gyroid | No nozzle strikes |
| Printing Temperature | 210 °C | |
| Printing Temperature Initial Layer | 215 °C | Better adhesion on a cold bed |
| Print Speed | 50 mm/s | |
| Infill Speed | 60 mm/s | Inside the hotend's limit |
| Outer Wall Speed | 30 mm/s | |
| Inner Wall Speed | 40 mm/s | |
| Top/Bottom Speed | 30 mm/s | |
| Travel Speed | 120 mm/s | |
| Initial Layer Speed | 20 mm/s | Adhesion |
| Enable Acceleration Control | On | Otherwise the firmware uses 200 mm/s² for everything |
| Print Acceleration | 800 | |
| Infill Acceleration | 1000 | Firmware maximum |
| Outer Wall Acceleration | 500 | |
| Inner Wall Acceleration | 800 | |
| Top/Bottom Acceleration | 600 | |
| Travel Acceleration | 1000 | |
| Initial Layer Acceleration | 300 | |
| Enable Jerk Control | Off | The firmware uses junction deviation and ignores jerk |
| Retraction Distance | 1.0 mm | **Required.** Direct drive |
| Retraction Speed | 25 mm/s | **Required.** Firmware caps E at 27 |
| Retraction Prime Speed | 20 mm/s | |
| Z Hop When Retracted | On, 0.2 mm | |
| Combing Mode | Not in Skin | |
| Fan Speed | 100% | The fan is weak |
| Regular Fan Speed at Layer | 2 | |
| Minimum Layer Time | 10 s | |
| Build Plate Adhesion Type | Skirt (Brim for small or long parts) | |
| Skirt Line Count | 2 | |
| Skirt Distance | 3 mm | |
| Initial Layer Horizontal Expansion | -0.1 mm | Elephant foot compensation |

5. Save it as a profile: **Profile > Create profile from current settings**.

## Advanced: Machine Settings for time estimates

Cura uses these only to estimate print time. Set them to match the firmware so estimates are close. They are hidden unless you search for them.

| Setting | Value |
|---|---|
| Maximum Speed X, Y, Z, E | 300, 300, 20, 27 |
| Maximum Acceleration X, Y, Z, E | 1000, 1000, 150, 4000 |
| Default Acceleration | 800 |
| Default X-Y Jerk, Z Jerk, E Jerk | 10, 0.3, 5 |

## Check your setup

Slice a 20 mm test cube and save the G-code:

- The cube appears in the center of the build plate.
- The file ends in `.gcode`, not `.g3drem` or `.ufp`.
- Open it in a text editor. You should see `M204` acceleration lines, and no `M190` or `M140` bed temperature lines.
