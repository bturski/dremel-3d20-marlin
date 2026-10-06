# Failed flash

A "bricked" 3D20 is almost always recoverable. Most of the time the bootloader survives and only the firmware is bad. This page helps you work out which case you have and what to do.

!!! tip "Stop and diagnose first"
    Don't keep trying random files. Each wrong attempt can make the problem harder to read. Work through this page in order.

## The most common cause

The Dremel updater installs **every** `.bin` file in its `firmware` folder. The Marlin release zip contains builds for several FlashForge printers. If you copy the whole zip into that folder, the updater can install a FlashForge build. FlashForge builds use a different encryption key, so on a 3D20 they decrypt into garbage. The printer then stops at the start screen or shows a blank screen.

The fix is to write a correct firmware file. How you do that depends on what still works.

## Check your file before you flash anything

Our [firmware tool](../reference/downloads.md#firmware-tool) can test a file without touching the printer. It decrypts the file with the Dremel key and checks that the result looks like real firmware:

```
python ff_firmware_tool.py decrypt dremel_2.0.9.5_01152023.bin test.bin
```

- "Check passed" means the file is a valid 3D20 build.
- "WARNING" means the file is for another printer or is damaged. Don't flash it.

## Stuck on the start screen

**What it means:** The bootloader runs, since it draws the start screen. The firmware it hands off to is bad.

**Why the SD card can't fix it:** The bootloader only installs `sys/dremel.bin` when an update flag is set in the chip's memory. Only working Marlin can set that flag (the "Firmware update trigger" menu item). With no working firmware, the bootloader ignores the card.

**What to try:**

1. **The Dremel updater, once.** Connect USB, turn the printer on, and run `dremel_firmware.exe`. If it shows **Printer Detected**, empty the updater's `firmware` folder, copy in only your one `dremel_` file, and run the update. The 3D20's bootloader usually can't be updated this way, so expect this to fail. It costs nothing to check.
2. **The ST-Link.** This is the reliable fix. Write the unencrypted firmware to address `0x08010000`. Only the firmware area is touched, and the bootloader stays as it is. See [ST-Link recovery](st-link-recovery.md).

This is the case in the maintainer's answer in [discussion #101](https://github.com/moonglow/FlashForge_Marlin/discussions/101). One owner recovered by writing the Color UI v0.15.0 build to `0x08010000`.

## Blank screen

**What it means:** Either the firmware crashes before it draws anything, or the bootloader itself is damaged.

**What to do:** Use the [ST-Link](st-link-recovery.md). After you connect, the first step is a backup, and it also shows you which case you have:

- If the bootloader area at `0x08000000` holds data, only the firmware is bad. Write the firmware as normal.
- If the bootloader area reads as all `FF`, the bootloader is gone. Restore it first, then write the firmware. See [Restore the bootloader](st-link-recovery.md#restore-the-bootloader).

## SD card update ignored

You put `dremel.bin` in `sys` on the internal card and nothing changed.

| Check | Fix |
|---|---|
| Did you use the Firmware update trigger menu before rebooting? | The bootloader needs the flag. Go to **Configuration > Advanced Settings > Firmware update trigger**, confirm, then turn the printer off and on |
| Is the file named exactly `dremel.bin`? | Turn on file name extensions in Windows and look for `dremel.bin.bin` |
| Is it in the `sys` folder? | Not the root of the card |
| Is it the only `.bin` in `sys`? | Remove the others |
| Is the card seated fully, with the clip locked? | Reseat it |
| Does Marlin run at all? | If not, the trigger can't be set. See [stuck on the start screen](#stuck-on-the-start-screen) |

## Updater can't see the printer

| Check | Fix |
|---|---|
| Driver installed? | Install the 3D20 USB driver linked from the [install wiki](https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20) |
| Cable and port | Try another cable and a USB port directly on the PC, not a hub |
| Printer state | Turn the printer off and on with USB connected |
| Firmware working? | A printer stuck at the start screen may not answer the updater. Use the ST-Link |

## No power at all

No backlight, no fans, no lights on the board. Firmware can't cause this. Check the power switch, the power supply, and the cable from the supply to the board.

## After any recovery

Once Marlin runs again:

1. Reset settings: `M502` then `M500`.
2. Redo [First setup](../firmware/first-setup.md).
3. Make a full backup of the chip with the ST-Link while everything works. See [Back up the chip](st-link-recovery.md#6-back-up-the-chip).
