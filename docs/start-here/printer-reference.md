# Printer reference

Facts about the 3D20 hardware that the rest of the guide relies on.

## Machine

| Item | Value |
|---|---|
| Build volume | 230 x 150 x 140 mm |
| Filament | 1.75 mm |
| Nozzle | 0.4 mm |
| Heated bed | None |
| Hotend sensor | K-type thermocouple, read through an ADS1118 converter |
| Extruder | Direct drive |
| Screen | Color touch screen |
| Close relative | FlashForge Dreamer NX. The 3D20 is the same design without a heated bed or chamber sensor |

## Coordinates under Marlin

Marlin puts the origin (X0 Y0) in the **center** of the bed. This is the single most important fact for slicer setup.

| Axis | Minimum | Maximum | Homes to |
|---|---|---|---|
| X | -111.0 | 158.5 | Maximum (right) |
| Y | -76.23 | 76.23 | Maximum (back) |
| Z | 0 | 140 | Minimum (bed up to nozzle) |

The bed is 230 mm wide, so a centered slicer bed runs from X -115 to 115. Marlin stops X at -111, so keep parts about 4 mm in from the left edge of the slicer bed. The extra travel on the right side is for parking at home, not printing.

## Main board

Boards seen in 3D20 printers include the **FlashForge Coreboard Rev D**. Other revisions may exist. If yours looks different, compare it with the photos in the [backup firmware wiki page](https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware) and tell us in an issue.

| Part | What it does |
|---|---|
| STM32F407ZG chip | The main processor. 1 MB of flash memory |
| USB Type B port | Serial connection to a PC |
| Internal micro SD slot | Holds firmware update files and screen images. Under a sliding metal clip |
| White 3-pin connector next to the USB port, labeled **DMS** | Doubles as the SWD debug socket for an ST-Link. Pin 1 goes to chip leg 109 (SWCLK), pin 2 to leg 105 (SWDIO). See below |
| NTC1 and NTC2 pads | Unused thermistor inputs on the 3D20. Ignore them |

### Internal micro SD card

The card in the slot on the main board is not the one you print from. It holds:

- `sys/dremel.bin`, which the bootloader installs when an update is requested.
- `sys/bosch1.bmp` and `sys/bosch2.bmp`, the start screen images. If these go missing, you lose the splash screen but the printer still works.

These file names come from the text inside the stock bootloader. If the bootloader can't read the card at all, it shows **TF card Fail...** on screen. Reseat the card and check that it isn't damaged.

To remove it, note which way it faces, slide the metal clip toward the USB connector, then flip the clip up. Reverse the steps to put it back.

!!! tip
    Copy the whole internal card to your PC the first time you open the printer. It costs nothing and protects the screen images.

### SWD socket

The SWD socket lets an ST-Link write directly to the chip. On the Coreboard Rev D it is the white 3-pin connector next to the USB port, labeled **DMS**. We confirmed with continuity tests on a real board that it carries the debug signals, matching the pin order on the [backup firmware wiki page](https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware):

| Socket pin | Signal | Chip leg |
|---|---|---|
| 1 (square pad on the back) | SWCLK | 109 (PA14) |
| 2 | SWDIO | 105 (PA13) |
| 3 | GND | Ground |

![The DMS connector next to the USB port, with SWCLK, SWDIO, GND and the K201 reset button marked](../assets/images/coreboard-revd-swd-connector.jpg)

![The back of the board, showing the connector's solder joints with the square pin 1 pad](../assets/images/coreboard-revd-back-swd-pads.jpg)

Always check the wiring with a multimeter before you connect anything. The full steps are in [ST-Link recovery](../troubleshooting/st-link-recovery.md).

### Chip legs worth knowing

The STM32F407ZG has 144 legs, numbered counterclockwise from the corner with the small dot. Holding the board so the dot is at the top left: legs 1 to 36 run down the left side, 37 to 72 along the bottom, 73 to 108 up the right side, and 109 to 144 right to left along the top.

![The STM32F407 chip with legs 109, 105, 138 and 25 marked](../assets/images/coreboard-revd-chip-legs.jpg)

| Leg | Signal | Why you'd care |
|---|---|---|
| 109 | SWCLK (PA14) | Debug clock. Should beep to socket pin 1 |
| 105 | SWDIO (PA13) | Debug data. Should beep to socket pin 2 |
| 25 | NRST | Reset. Also wired to the **K201** reset button next to the USB port |
| 138 | BOOT0 | Held at 3.3 V during power-up, the chip runs ST's factory loader instead of the firmware. Wired to resistors R212 and R213, next to that corner of the chip |

## Flash memory layout

You only need this table for ST-Link work.

| Address | Size | Contents |
|---|---|---|
| `0x08000000` | 48 KB | Bootloader. About 46 KB is used. The text "Bootloader V1.0" and "Copyright 2014 by Bosch." appears inside it |
| `0x0800C000` | 16 KB | Update flag area, written by Marlin's "Firmware update trigger" |
| `0x08010000` | Rest of the chip | Firmware (stock or Marlin) |

The update flag location comes from Marlin's own source code for this printer. The firmware address comes from the maintainer's recovery steps in [discussion #101](https://github.com/moonglow/FlashForge_Marlin/discussions/101).

### Advanced: how the update flag works

This comes from a bootloader backup of a working 3D20, read alongside Marlin's trigger code. The flag area holds two things:

| Address | Bytes | Contents |
|---|---|---|
| `0x0800C000` | 28 | A signature: the text `flashforge12` followed by 16 bytes tied to that particular chip |
| `0x0800C01C` | 4 | A status word. `00 FF 00 FF` on a printer with no update waiting |

Marlin's trigger erases the area and writes back only the 28-byte signature, which leaves the status word blank (`FF FF FF FF`). The best explanation is that a blank status word tells the bootloader to install `sys/dremel.bin` on the next boot, and the bootloader writes `00 FF 00 FF` back when it finishes. We have not tested this directly.

!!! warning "The flag area belongs to one chip"
    The signature is different on every printer. Never write the `0x0800C000` area from someone else's backup onto your printer. Keep your own backup of it, from your own printer.
