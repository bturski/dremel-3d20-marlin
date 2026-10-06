# Install Marlin

This is the first install, going from stock Dremel firmware to Marlin. It uses Dremel's own firmware updater over USB. The steps follow the project's [install guide for the 3D20](https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20).

!!! info "Why not the SD card?"
    The 3D20 has an older bootloader (version 1.0). It can't take a first install straight from an SD card the way FlashForge printers can. Dremel's updater is the supported route for the first install. Later updates use the internal SD card. See [Update Marlin](update.md).

## Before you begin

- [ ] You picked **one** `dremel_` file. See [Choose a build](choose-a-build.md).
- [ ] File extensions are visible in Windows File Explorer (**View > Show > File name extensions**).
- [ ] The 3D20 USB driver is installed.
- [ ] Nothing is printing, and the printer is on a stable power source.

## Steps

1. **Connect the printer.** Plug the 3D20 into your PC with the USB cable and turn it on.

2. **Unpack the Dremel updater.** You get a folder like `Dremel3D20_Firmware_Update_Package_20180611`. Open the `firmware` folder inside it.

3. **Move the stock firmware out.** You'll see a file like `dremel_1.5.20180611.bin`. Move it to a safe place, such as a folder named `stock-firmware-backup`. Don't just rename it inside the folder. Keep this file forever. You need it to go back to stock.

4. **Copy in your Marlin file.** Copy your one `dremel_` file into the `firmware` folder. You don't need to rename it.

5. **Check the folder.** The `firmware` folder must now hold **exactly one** `.bin` file: your Marlin build. The updater installs any `.bin` it finds, so an extra file can brick the printer.

6. **Run the updater.** Start `dremel_firmware.exe`. The first button turns green and says **Printer Detected**. If it stays grey, check the cable and driver before going further.

7. **Start the update.** Click **Start Firmware Update** and wait for it to finish.

8. **Reboot the printer.** Turn it off, then on. A progress bar runs along the bottom of the screen while the new firmware installs.

9. **Confirm.** After the bar finishes, the printer restarts. You see the Dremel logo, then the Marlin screen.

Next, go to [First setup after install](first-setup.md). Don't skip it. The hotend needs a new temperature tune under Marlin.

## If something goes wrong

| What you see | What to do |
|---|---|
| The updater never shows **Printer Detected** | Reinstall the USB driver, try another USB port and cable, and turn the printer off and on with USB connected |
| The progress bar never appears after reboot | Turn the printer off and on once more. If it still boots to stock, run the updater again |
| The printer stops on the start screen and never reaches Marlin | Go to [Failed flash](../troubleshooting/failed-flash.md) |
| The screen stays black | Go to [Failed flash](../troubleshooting/failed-flash.md) |
