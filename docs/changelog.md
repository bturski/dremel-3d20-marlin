# Changelog

Notable changes to this guide. Newest first.

## 2026-10-08

- Fixed the PrusaSlicer bundle: added `G92 E0` to the before layer change G-code. Without it, PrusaSlicer refuses to slice when relative E distances are on. Re-import the bundle, or add the line by hand.

## 2026-10-06 (afternoon)

Updated from a real ST-Link recovery on a Coreboard Rev D.

- Added annotated photos of the board: the DMS connector, its solder pads, and the chip legs for SWCLK, SWDIO, NRST, and BOOT0.
- Confirmed that the DMS connector is the SWD socket, and how its pins map to chip legs.
- Added a multimeter check from each ST-Link wire to its chip leg.
- Added STM32 ST-Link Utility as the recommended tool for clone ST-Link V2 sticks.
- Added backing up the bootloader on its own, and the rest of the chip in pieces when a full read crashes.
- Documented the bootloader version, the start screen image names, and how the update flag area is laid out, from a real bootloader backup.
- Added connecting while holding reset, and BOOT0 as a last resort. BOOT0 is confirmed to connect to R212 and R213.

## 2026-10-06

First release.

- Firmware: choosing a build, first install, first setup, updates, going back to stock.
- Slicers: PrusaSlicer and UltiMaker Cura, with importable profiles and shared start and end G-code.
- Troubleshooting: failed flash diagnosis, ST-Link recovery, common print problems.
- Reference: firmware values, downloads, glossary, sources with archive links.
- Tools: a Python firmware encryption tool, a profile generator, style checks, and monthly source archiving.
