# ST-Link recovery

An ST-Link is a small USB programmer that writes straight into the printer's main chip. It doesn't depend on the bootloader or the firmware, so it works when nothing else does. Use it to fix a printer that won't boot after a bad flash.

The method comes from the firmware maintainer's answer in [discussion #101](https://github.com/moonglow/FlashForge_Marlin/discussions/101) and the pinout on the [backup firmware wiki page](https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware).

**Time needed:** about 30 minutes, once the parts arrive.

## Buy an ST-Link

Any of these work. For a one-time recovery, the clone stick is the easiest choice.

| Option | Rough cost | Notes | Where to buy |
|---|---|---|---|
| **Clone ST-Link V2 USB stick** | $8 to $15 | Easiest. Pins are labeled on the case, and most come with female to female jumper wires | [Amazon search](https://www.amazon.com/s?k=st-link+v2+programmer), [AliExpress search](https://www.aliexpress.com/w/wholesale-st-link-v2.html) |
| **Official STLINK-V3MINIE** | $12 to $15 | Genuine ST part. It uses a small 1.27 mm 14-pin cable, so you also need a breakout adapter or fine jumper wires | [ST product page](https://www.st.com/en/development-tools/stlink-v3minie.html), [Digi-Key](https://www.digikey.com/en/products/detail/stmicroelectronics/STLINK-V3MINIE/16284301), [Mouser](https://www.mouser.com/c/?q=STLINK-V3MINIE) |
| **An STM32 Nucleo board you already own** | Free if you have one | Every Nucleo-64 board has an ST-Link built in. Remove both CN2 jumpers, then use the CN4 header: pin 2 SWCLK, pin 3 GND, pin 4 SWDIO | You already have it |

You also need three female to female jumper wires if your ST-Link didn't come with them.

## 1. Install the software

1. Download and install [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) from ST. It's free but needs an ST account. The installer includes the ST-Link USB driver.
2. Install Python 3 from [python.org](https://www.python.org/downloads/) if you don't have it. You need it for the next step.

## 2. Make the unencrypted firmware

The `.bin` files in the Marlin release are encrypted for the bootloader. The ST-Link writes straight to the chip, with no bootloader in between, so it needs the **unencrypted** version.

1. Download [`ff_firmware_tool.py`](../reference/downloads.md#firmware-tool) from this guide.
2. Put it in the same folder as your Marlin file, for example `dremel_2.0.9.5_01152023.bin`.
3. Open a terminal in that folder (in Windows File Explorer, type `cmd` in the address bar and press Enter) and run:

    ```
    python ff_firmware_tool.py decrypt dremel_2.0.9.5_01152023.bin dremel_unencrypted.bin
    ```

4. Look for **Check passed** in the output. If you see a WARNING, the file is not a 3D20 build. Don't flash it.

??? info "Advanced: using the original C tool"
    The script is a port of [moonglow/flashforge_firmware_tool](https://github.com/moonglow/flashforge_firmware_tool) and produces the same output byte for byte. To use the original, build it with `gcc main.c -o ff_fw_tool` and run:

    ```
    ./ff_fw_tool -k flashforge123456 -i dremel_2.0.9.5_01152023.bin -o dremel_unencrypted.bin
    ```

    Leaving out `-e` means decrypt. `flashforge123456` is the Dremel key.

## 3. Find the SWD socket

1. Turn the printer off and unplug it.
2. Flip it over and remove the six 2.5 mm hex screws from the bottom cover. The cover is held by a grounding strap, so lift it gently.
3. Find the small **white 3-pin connector next to the USB port**. On the Coreboard Rev D it is labeled **DMS**, but it doubles as the SWD socket. Pin 1 connects to chip leg 109 (SWCLK) and pin 2 to chip leg 105 (SWDIO).
4. Find pin 1. Look for a "1", a triangle, or a square solder pad on the board.

The [backup firmware wiki page](https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware) lists this order:

| Socket pin | Signal |
|---|---|
| 1 | SWCLK |
| 2 | SWDIO |
| 3 | GND |

5. **Confirm ground with a multimeter.** Set it to continuity (beep) mode. Touch one probe to the metal shell of the USB port and the other to each socket pin in turn. Only the GND pin should beep. If pin 1 beeps instead of pin 3, the order on your board is reversed, so swap SWCLK and SWDIO too.

## 4. Connect

| ST-Link pin | Printer SWD socket |
|---|---|
| SWCLK | SWCLK |
| SWDIO | SWDIO |
| GND | GND |
| 3.3V | **Not connected** |

The pin names are printed on the ST-Link case. Don't connect the ST-Link's 3.3V pin. The printer powers itself.

1. Push the three jumper wires onto the socket pins and the matching ST-Link pins.
2. Plug the printer's power cord back in.
3. Plug the ST-Link into your PC.
4. Turn the printer on.

## 5. Back up the chip

Always make a backup before you write anything. It also tells you whether the bootloader survived.

1. Open STM32CubeProgrammer.
2. In the top right, choose **ST-LINK** from the drop-down and click the refresh button next to the serial number.
3. Set **Port** to SWD, **Frequency** to 4000 kHz, **Mode** to Normal, and **Reset mode** to Software reset.
4. Click **Connect**. The log at the bottom should show the chip, an STM32F40x/F41x.
5. In the memory view, set **Address** to `0x08000000` and **Size** to `0x100000` (the whole 1 MB chip). Click **Read**.
6. Use the arrow next to **Read** and choose **Save As**. Save it as `3d20-full-backup.bin` and keep it safe.
7. Look at the first rows at `0x08000000`:
    - **Normal numbers:** the bootloader is fine. Go to step 6.
    - **All `FFFFFFFF`:** the bootloader is gone. Go to [Restore the bootloader](#restore-the-bootloader) first.

!!! danger "Read protection"
    If CubeProgrammer reports **read out protection level 1**, stop. Removing that protection erases the entire chip, bootloader included. Ask in [discussion #101](https://github.com/moonglow/FlashForge_Marlin/discussions/101) before you go on.

## 6. Write the firmware

1. Open the **Erasing & Programming** page (the second icon on the left toolbar).
2. **File path:** browse to `dremel_unencrypted.bin`.
3. **Start address:** `0x08010000`. Check this twice. Writing to the wrong address can wipe the bootloader.
4. Tick **Verify programming**.
5. **Don't** click **Full chip erase**. It wipes the bootloader. CubeProgrammer erases only the space your file needs.
6. Click **Start Programming** and wait for "File download complete" and a successful verify.

## 7. Restart

1. Click **Disconnect** in CubeProgrammer.
2. Turn the printer off, remove the jumper wires, and turn it on.
3. You should see the Dremel start screen, then Marlin.
4. Follow [After any recovery](failed-flash.md#after-any-recovery).

You can leave `sys/dremel.bin` on the internal card if it's the same version. For future updates, use the normal [SD card method](../firmware/update.md).

## Restore the bootloader

Only do this if the backup in step 5 showed the bootloader area as all `FF`.

- **If you have your own backup** from before the problem, write its first 48 KB back to `0x08000000`. This is the best option.
- **If you don't,** the maintainer posted a bootloader file, `dreamer_bootloader_v1.4_20161121_no_check.zip`, in [discussion #101](https://github.com/moonglow/FlashForge_Marlin/discussions/101). It is a Dreamer bootloader with the chip ID check removed. Write it to `0x08000000`, then write the firmware to `0x08010000` as in step 6.

!!! warning
    A Dreamer bootloader isn't Dremel's own. The start screen images and SD card updates may behave differently afterward. Plan to do future updates with the ST-Link until you confirm the SD card route works. If you learn how it behaves on a 3D20, please [tell us](../contributing.md).

## Using OpenOCD instead

[OpenOCD](https://openocd.org/) is a free command line alternative to CubeProgrammer. It also works with clones that CubeProgrammer refuses. On Windows, the [xPack OpenOCD](https://xpack-dev-tools.github.io/openocd-xpack/) build is the easiest to install.

Back up the whole chip:

```
openocd -f interface/stlink.cfg -f target/stm32f4x.cfg -c "init" -c "reset halt" -c "flash read_bank 0 3d20-full-backup.bin 0 0x100000" -c "exit"
```

Write the firmware. This erases only the sectors the file needs:

```
openocd -f interface/stlink.cfg -f target/stm32f4x.cfg -c "program dremel_unencrypted.bin 0x08010000 verify reset exit"
```

Older OpenOCD versions call the interface file `interface/stlink-v2.cfg`.

## If it won't connect

| Problem | Try |
|---|---|
| "No ST-Link detected" | Reinstall the driver, try another USB port, or update the ST-Link firmware from CubeProgrammer's **Firmware upgrade** button. Don't upgrade clones. Some stop working afterward |
| "Cannot connect to target" | Check the GND pin with a multimeter. Swap SWCLK and SWDIO. Lower the frequency to 480 kHz |
| Connects, then drops | Set **Mode** to Hot plug. Keep the wires short and away from the power supply |
| Clone refused by CubeProgrammer | Use OpenOCD instead |
| Verify fails | Lower the frequency and try again. Check the start address |
