# Sources

Every outside fact in this guide comes from one of these pages. Each one has an archived copy on the Internet Archive's Wayback Machine, in case the original moves or disappears.

Archive links with a date point to a specific saved copy. Links marked **latest** open the newest saved copy. A scheduled job in this repository asks the Wayback Machine to save every linked page once a month, so the latest copy stays current. See [How archiving works](#how-archiving-works).

## Firmware

| Source | Used for | Archive |
|---|---|---|
| [moonglow/FlashForge_Marlin](https://github.com/moonglow/FlashForge_Marlin) | The firmware, its supported printers, and its configuration values | [Mar 2026](https://web.archive.org/web/20260311063620/https://github.com/moonglow/FlashForge_Marlin) |
| [FlashForge_Marlin releases](https://github.com/moonglow/FlashForge_Marlin/releases) | Release versions and file names | [Mar 2026](https://web.archive.org/web/20260310195425/https://github.com/moonglow/FlashForge_Marlin/releases) |
| [Installing Marlin on Dremel 3D20](https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20) | First install with the Dremel updater, SD card updates, going back to stock, bootloader version | [Mar 2023](https://web.archive.org/web/20230319091507/https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20) |
| [Avoid using FlashForge original firmware G-Codes](https://github.com/moonglow/FlashForge_Marlin/wiki/%5BATTENTION%5D-Avoid-using-FlashForge-original-firmware-G-Codes) | The `M907`, `M104`, and `M140` differences | [latest](https://web.archive.org/web/https://github.com/moonglow/FlashForge_Marlin/wiki/%5BATTENTION%5D-Avoid-using-FlashForge-original-firmware-G-Codes) |
| [Start and end G-code examples](https://github.com/moonglow/FlashForge_Marlin/wiki/FlashForge-Dreamer-NX-Start-End-G-Codes-examples) | Base for our start and end G-code | [Mar 2026](https://web.archive.org/web/20260312004923/https://github.com/moonglow/FlashForge_Marlin/wiki/FlashForge-Dreamer-NX-Start-End-G-Codes-examples) |
| [Backup printer firmware](https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware) | SWD socket pin order, chip pins, OpenOCD backup command | [Jan 2022](https://web.archive.org/web/20220110162622/https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware) |
| [Tune stepper motor current](https://github.com/moonglow/FlashForge_Marlin/wiki/Tune-stepper-motor-current) | Safe motor current changes | [latest](https://web.archive.org/web/https://github.com/moonglow/FlashForge_Marlin/wiki/Tune-stepper-motor-current) |
| [Discussion #101: Bricked Dremel 3D20](https://github.com/moonglow/FlashForge_Marlin/discussions/101) | ST-Link recovery addresses, bootloader restore file, a confirmed recovery | [latest](https://web.archive.org/web/https://github.com/moonglow/FlashForge_Marlin/discussions/101) |
| [moonglow/flashforge_firmware_tool](https://github.com/moonglow/flashforge_firmware_tool) | Firmware encryption, the Dremel key | [latest](https://web.archive.org/web/https://github.com/moonglow/flashforge_firmware_tool) |
| [Dremel 3D20 documentation](https://digilab.dremel.com/service-3d20-documentation) | Dremel's firmware updater and stock firmware | [Sep 2021](https://web.archive.org/web/20210919071812/https://digilab.dremel.com/service-3d20-documentation) |

## Slicers

| Source | Used for | Archive |
|---|---|---|
| [Cura Dremel Printer Plugin](https://github.com/metalman3797/Cura-Dremel-Printer-Plugin) | Stock 3D20 G-code and speeds, for comparison | [latest](https://web.archive.org/web/https://github.com/metalman3797/Cura-Dremel-Printer-Plugin) |
| [Cura Dremel plugin issue #81](https://github.com/metalman3797/cura-dremel-printer-plugin/issues/81) | Stock firmware acceleration and jerk values | [latest](https://web.archive.org/web/https://github.com/metalman3797/cura-dremel-printer-plugin/issues/81) |
| [Cura: Definition Files Explained](https://github.com/Ultimaker/Cura/wiki/Definition-Files-Explained) | Format of our Cura printer definition | [latest](https://web.archive.org/web/https://github.com/Ultimaker/Cura/wiki/Definition-Files-Explained) |
| [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) | Slicer download | [latest](https://web.archive.org/web/https://www.prusa3d.com/page/prusaslicer_424/) |
| [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura/) | Slicer download | [latest](https://web.archive.org/web/https://ultimaker.com/software/ultimaker-cura/) |

## Marlin

| Source | Used for | Archive |
|---|---|---|
| [Marlin G-code reference](https://marlinfw.org/meta/gcode/) | Meaning of every G-code in this guide | [latest](https://web.archive.org/web/https://marlinfw.org/meta/gcode/) |
| [Linear Advance K-factor tool](https://marlinfw.org/tools/lin_advance/k-factor.html) | Calibrating the `la` build | [latest](https://web.archive.org/web/https://marlinfw.org/tools/lin_advance/k-factor.html) |

## ST-Link and tools

| Source | Used for | Archive |
|---|---|---|
| [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) | Writing firmware with an ST-Link | [latest](https://web.archive.org/web/https://www.st.com/en/development-tools/stm32cubeprog.html) |
| [STLINK-V3MINIE](https://www.st.com/en/development-tools/stlink-v3minie.html) | Official ST-Link option | [latest](https://web.archive.org/web/https://www.st.com/en/development-tools/stlink-v3minie.html) |
| [OpenOCD](https://openocd.org/) | Command line alternative | [latest](https://web.archive.org/web/https://openocd.org/) |
| [xPack OpenOCD](https://xpack-dev-tools.github.io/openocd-xpack/) | OpenOCD build for Windows | [latest](https://web.archive.org/web/https://xpack-dev-tools.github.io/openocd-xpack/) |
| [Pronterface](https://www.pronterface.com/) | Sending G-code over USB | [latest](https://web.archive.org/web/https://www.pronterface.com/) |

## Checked in this guide's own testing

Some facts come from reading the firmware source or testing files directly, not from a web page:

- The update flag address `0x0800C000` comes from the "Firmware update trigger" code in the firmware's `menu_advanced.cpp`.
- The 3D20 firmware settings on [Firmware values](firmware-values.md) come from `Configuration.h` and `Configuration_adv.h` at the `marlin_2.0.x` branch.
- The [firmware tool](downloads.md#firmware-tool) was checked against the original C tool on the v0.15.1 Dremel files.
- The PrusaSlicer bundle's setting names were checked against PrusaSlicer 2.9.2's source code. The Cura definition's setting names were checked against Cura's `fdmprinter.def.json`.

## How archiving works

The workflow `.github/workflows/archive-sources.yml` runs on the first day of each month and can also be started by hand from the **Actions** tab. It collects every outside link in the guide and asks the Wayback Machine to save a fresh copy. Shopping search pages are skipped.

If a link breaks, use its archive link, then [open an issue](https://github.com/bturski/dremel-3d20-marlin/issues) so we can update it.
