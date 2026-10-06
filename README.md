# Dremel 3D20 Marlin Guide

A complete guide to running Marlin 2 firmware on the Dremel 3D20 (Idea Builder). It covers installing the firmware, setting up PrusaSlicer and UltiMaker Cura, and recovering a printer after a failed flash.

**Read the guide: https://bturski.github.io/dremel-3d20-marlin/**

## What's inside

| Section | What you'll find |
|---|---|
| [Start here](docs/start-here/index.md) | What changes, what you need, and the rules that prevent most bricked printers |
| [Firmware](docs/firmware/choose-a-build.md) | Choosing the right file, first install, first setup, updates, going back to stock |
| [Slicers](docs/slicers/index.md) | PrusaSlicer and Cura setup, and safe start and end G-code |
| [Troubleshooting](docs/troubleshooting/index.md) | Failed flash diagnosis, ST-Link recovery, print problems |
| [Reference](docs/reference/downloads.md) | Downloads, firmware values, glossary, sources with archive links |

## Downloads

| File | Use |
|---|---|
| [PrusaSlicer config bundle](docs/downloads/prusaslicer/Dremel3D20_Marlin_PrusaSlicer.ini) | **File > Import > Import Config Bundle** |
| [Cura printer definition](docs/downloads/cura/Dremel3D20_Marlin_Cura.zip) | Unzip into Cura's `definitions` folder |
| [Start and end G-code](docs/downloads/gcode/) | For any slicer |
| [Firmware tool](scripts/ff_firmware_tool.py) | Check, decrypt, or encrypt 3D20 firmware files. Python 3, no extra packages |

## Two rules before you flash

1. Use **one** firmware file, and only one whose name starts with `dremel_`. The Dremel updater installs every `.bin` in its folder.
2. Never reuse start G-code from a stock Dremel profile. Under Marlin, its `M907` line runs every motor at maximum current.

## Contributing

Corrections and additions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits and license

The firmware is [moonglow/FlashForge_Marlin](https://github.com/moonglow/FlashForge_Marlin), by moonglow and contributors. This repository doesn't include it.

Guide text is CC BY 4.0. Code and profiles are MIT. See [LICENSE](LICENSE).

This project is not affiliated with Dremel, Bosch, FlashForge, or UltiMaker.
