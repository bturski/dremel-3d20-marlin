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

- A `sys` folder. The bootloader looks for `sys/dremel.bin` when an update is requested.
- Image files for the start screen. If these go missing, you lose the Dremel splash screen but the printer still works.

To remove it, note which way it faces, slide the metal clip toward the USB connector, then flip the clip up. Reverse the steps to put it back.

!!! tip
    Copy the whole internal card to your PC the first time you open the printer. It costs nothing and protects the screen images.

### SWD socket

The SWD socket lets an ST-Link write directly to the chip. The [backup firmware wiki page](https://github.com/moonglow/FlashForge_Marlin/wiki/Backup-printer-firmware) lists this pin order:

| Socket pin | Signal | Chip pin |
|---|---|---|
| 1 | SWCLK | PA14 (pin 109) |
| 2 | SWDIO | PA13 (pin 105) |
| 3 | GND | Ground |

Always confirm ground with a multimeter before you connect anything. The full steps are in [ST-Link recovery](../troubleshooting/st-link-recovery.md).

## Flash memory layout

You only need this table for ST-Link work.

| Address | Size | Contents |
|---|---|---|
| `0x08000000` | 48 KB | Bootloader |
| `0x0800C000` | 16 KB | Update flag (written by Marlin's "Firmware update trigger") |
| `0x08010000` | Rest of the chip | Firmware (stock or Marlin) |

The update flag location comes from Marlin's own source code for this printer. The firmware address comes from the maintainer's recovery steps in [discussion #101](https://github.com/moonglow/FlashForge_Marlin/discussions/101).
