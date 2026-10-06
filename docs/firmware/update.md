# Update Marlin

Once Marlin runs on your printer, you update it from the internal micro SD card. You don't need the Dremel updater again. These steps follow the project's [install guide](https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20).

!!! warning "Marlin must be working first"
    This method needs a working Marlin to set the update flag. If your printer doesn't boot, go to [Failed flash](../troubleshooting/failed-flash.md) instead.

## Steps

1. **Turn the printer off** and unplug it.

2. **Open the bottom.** Flip the printer over and remove the six 2.5 mm hex screws from the metal cover. The cover is attached by a grounding strap, so lift it gently.

3. **Remove the internal micro SD card.** Note which way it faces. Slide the metal clip toward the USB connector, flip it up, and take the card out.

4. **Back up the card.** Copy everything on it to your PC. Do this every time.

5. **Prepare the `sys` folder.**
    - Delete any old `.bin` files in `sys`. Leave the image files alone.
    - Copy in your one new `dremel_` file.
    - Rename it to exactly `dremel.bin`. With extensions visible, check that it isn't `dremel.bin.bin`.

6. **Put the card back.** Seat it fully, flip the clip down, and slide it away from the USB connector. You can leave the cover off until you confirm the update worked.

7. **Turn the printer on** and wait for Marlin to finish starting.

8. **Set the update flag.** Go to **Configuration > Advanced Settings > Firmware update trigger** and confirm **Write trigger?**. The screen says "Reboot your printer."

9. **Reboot.** Turn the printer off, then on. A progress bar runs along the bottom while the bootloader installs `dremel.bin`. Then Marlin starts.

10. **Reset settings if the version changed a lot.** New versions can change how settings are stored. Run `M502` then `M500`, and redo the [first setup](first-setup.md) steps you need.

11. Replace the bottom cover.

## Advanced: what the trigger does

The menu item rewrites a small area of flash at `0x0800C000`, keeping the chip's signature and blanking the status word after it. On the next boot the bootloader sees the blank status, installs `sys/dremel.bin`, and marks the update done. See [how the update flag works](../start-here/printer-reference.md#advanced-how-the-update-flag-works). Without the flag, the bootloader ignores the card. That is why a printer with broken firmware can't fix itself from the SD card.
