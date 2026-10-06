# Go back to stock

You can return to Dremel's firmware with the same SD card method used for updates. You need the stock file you set aside during the install, such as `dremel_1.5.20180611.bin`. If you lost it, it's inside Dremel's updater package, available from [Dremel's 3D20 documentation page](https://digilab.dremel.com/service-3d20-documentation).

## Steps

1. Follow steps 1 to 4 of [Update Marlin](update.md) to open the printer and back up the internal card.
2. In the `sys` folder, delete any `.bin` files and copy in the stock file.
3. Rename it to exactly `dremel.bin`.
4. Put the card back and turn the printer on.
5. In Marlin, go to **Configuration > Advanced Settings > Firmware update trigger** and confirm.
6. Turn the printer off, then on. The bootloader installs the stock firmware.

The project's [install guide](https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20) describes this same route.

## After going back

- Slice with DigiLab 3D Slicer or a Cura profile set to the stock Dremel output again.
- Remove the Marlin profiles from your slicer, or rename them, so you don't send Marlin G-code to stock firmware.

## If Marlin isn't running

The trigger needs a working Marlin. If your printer won't boot, write the stock firmware with an ST-Link instead. The steps are the same as [ST-Link recovery](../troubleshooting/st-link-recovery.md), using an unencrypted copy of the stock file. Decrypt it with the same tool, using the Dremel key.
