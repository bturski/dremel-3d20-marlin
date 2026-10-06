# Before you start

Read this page once before you flash anything. It explains what you gain, what you give up, and the few mistakes that cause most bricked printers.

## What you gain

- **Any slicer.** PrusaSlicer, Cura, OrcaSlicer, or anything else that writes Marlin G-code.
- **Plain G-code.** The printer reads normal `.gcode` files from the SD card. No more `.g3drem` files.
- **Real settings.** You can change speeds, acceleration, temperatures, and steps from the screen or with G-code, and save them.
- **Mesh bed leveling.** The firmware can store a 3 by 3 height map of your bed and correct for it.
- **USB printing.** The printer shows up as a serial port, so tools like OctoPrint and Pronterface work.

## What you give up

- **Dremel's slicer and cloud tools.** DigiLab 3D Slicer and `.g3drem` files stop working.
- **Official support.** Dremel won't help with a printer running custom firmware.
- **Simple updates.** Updating or going back to stock means opening the bottom of the printer. See [Update Marlin](../firmware/update.md) and [Go back to stock](../firmware/revert-to-stock.md).

## How the printer starts up

Knowing this makes every other page easier to follow.

The main chip has two parts in its memory:

1. **The bootloader.** A small program that runs first, every time. It can install new firmware from the internal SD card, but only when a "please update" flag is set. It also shows the first screen you see at power on.
2. **The firmware.** Stock Dremel firmware or Marlin. This is what you interact with.

Firmware files for the 3D20 are encrypted with a Dremel key. The bootloader and Dremel's updater decrypt them as they install. A file built for a different printer uses a different key, so it decrypts into garbage. If garbage gets installed, the firmware won't run, but the bootloader usually survives. That is the most common "bricked" state, and it is fixable. See [Failed flash](../troubleshooting/failed-flash.md).

## The rules that prevent most problems

!!! danger "Use one file, and only the Dremel build"
    The Marlin release contains builds for several printers. Only files that start with `dremel_` are for the 3D20. When you run Dremel's updater, the `firmware` folder must contain **exactly one** `.bin` file. The updater uses any `.bin` it finds there. Putting the whole release in that folder is the most common way people brick this printer.

!!! danger "Never reuse stock start G-code"
    The stock Dremel profile sends `M907 X100 Y100 Z60 A100`. In stock firmware those are raw values. In Marlin, `M907` sets motor current in amps, so this line drives every motor at maximum current. Motors can overheat and melt their plastic mounts. Use the start G-code from this guide instead. See [Start and end G-code](../slicers/gcode.md).

!!! warning "Keep the stock firmware file"
    Before you install Marlin, copy Dremel's original firmware file somewhere safe. You need it to go back to stock.

## Paths through this guide

**Beginner, first install:** read [What you need](what-you-need.md), then follow the Firmware section in order, then pick one slicer page.

**Already running Marlin:** go straight to [What every slicer needs](../slicers/index.md) and import a profile from [Downloads](../reference/downloads.md).

**Printer won't boot:** go to [Failed flash](../troubleshooting/failed-flash.md). Don't keep retrying random files first.
