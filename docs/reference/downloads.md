# Downloads

Every file here is in this repository under `docs/downloads/` and `scripts/`. If your browser shows a file as text instead of saving it, right click the link and choose **Save link as**.

## Slicer profiles

| File | For | How to use |
|---|---|---|
| [Dremel3D20_Marlin_PrusaSlicer.ini](../downloads/prusaslicer/Dremel3D20_Marlin_PrusaSlicer.ini) | PrusaSlicer 2.8 and newer | **File > Import > Import Config Bundle**. See [PrusaSlicer](../slicers/prusaslicer.md) |
| [Dremel3D20_Marlin_Cura.zip](../downloads/cura/Dremel3D20_Marlin_Cura.zip) | UltiMaker Cura 5.x | Unzip both files into Cura's `definitions` folder. See [Cura](../slicers/cura.md) |

## G-code

| File | Use |
|---|---|
| [prusaslicer-start.gcode](../downloads/gcode/prusaslicer-start.gcode) | PrusaSlicer start G-code |
| [prusaslicer-end.gcode](../downloads/gcode/prusaslicer-end.gcode) | PrusaSlicer end G-code |
| [cura-start.gcode](../downloads/gcode/cura-start.gcode) | Cura start G-code |
| [cura-end.gcode](../downloads/gcode/cura-end.gcode) | Cura end G-code |

Each line is explained on the [Start and end G-code](../slicers/gcode.md) page.

## Firmware tool

[ff_firmware_tool.py](https://github.com/bturski/dremel-3d20-marlin/raw/main/scripts/ff_firmware_tool.py) decrypts and encrypts 3D20 firmware files. It needs Python 3 and nothing else.

```
python ff_firmware_tool.py decrypt dremel_2.0.9.5_01152023.bin dremel_unencrypted.bin
```

Use it to:

- **Check a file before flashing.** It prints "Check passed" only for a real 3D20 build.
- **Make an unencrypted file** for [ST-Link recovery](../troubleshooting/st-link-recovery.md).
- **Encrypt your own build** so the bootloader accepts it: `python ff_firmware_tool.py encrypt firmware.bin dremel.bin`

It is a Python port of [moonglow/flashforge_firmware_tool](https://github.com/moonglow/flashforge_firmware_tool). We tested it against the original on the v0.15.1 Dremel files, and the output matches byte for byte in both directions.

## Firmware

This guide doesn't host firmware. Download it from the [moonglow/FlashForge_Marlin releases](https://github.com/moonglow/FlashForge_Marlin/releases), so you always get the authors' current files. See [Choose a build](../firmware/choose-a-build.md).

## Advanced: changing the profiles

The profile files are generated. To change a value:

1. Edit `scripts/build_profiles.py`, or a G-code file in `docs/downloads/gcode/`.
2. Run `python scripts/build_profiles.py`.
3. Commit both the script change and the regenerated files.

A check on every pull request fails if the profiles are out of date.
