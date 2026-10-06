# Glossary

**Bootloader.** A small program at the start of the chip's memory that runs first at every power on. On the 3D20 it draws the start screen and can install firmware from the internal SD card when the update flag is set.

**BOOT0.** A leg on the main chip (leg 138). Held at 3.3 V during power-up, it makes the chip run ST's built-in factory loader instead of the firmware.

**Brick.** Slang for a printer that won't start after a bad firmware install. On the 3D20 this is almost always recoverable with an ST-Link.

**Config bundle.** A PrusaSlicer file holding printer, print, and filament presets together. Imported with **File > Import > Import Config Bundle**.

**Definition file.** A Cura file (`.def.json`) describing a printer and its default settings.

**DMS connector.** The white 3-pin connector next to the USB port on the Coreboard Rev D. Despite its label, it is also the SWD debug socket.

**E-steps.** How many motor steps push 1 mm of filament. Set with `M92 E`.

**EEPROM.** Memory that keeps saved settings through power off. `M500` writes to it.

**Encrypted firmware.** Firmware files for the 3D20 are scrambled with a Dremel key. The bootloader and Dremel's updater unscramble them while installing. An ST-Link needs the unscrambled (unencrypted) version.

**Firmware.** The main program the printer runs. Stock Dremel firmware or Marlin.

**G-code.** The text commands a printer follows, such as `G1 X10 Y10` to move.

**Junction deviation.** How Marlin decides how fast to take a corner. It replaces the older "jerk" setting.

**Linear Advance.** A Marlin feature that adjusts extruder pressure as speed changes. Available in the `la` build.

**Mesh bed leveling.** A stored height map of the bed. Marlin raises or lowers the nozzle to follow it.

**NRST.** The main chip's reset line (leg 25). The K201 button pulls it low. An ST-Link can hold it low while connecting.

**Origin.** The X0 Y0 point. On the 3D20 under Marlin it's the center of the bed.

**PID tuning.** Teaching the firmware how the heater responds, so it holds a steady temperature. Done with `M303`.

**ST-Link.** A USB programmer for STM32 chips. It writes straight to the chip and works when the printer won't boot.

**SWD.** Serial Wire Debug. The two-wire connection (plus ground) an ST-Link uses. The 3D20 board has a 3-pin SWD socket next to the USB port.

**Update flag.** A small marker in flash memory at `0x0800C000`. When set, the bootloader installs `sys/dremel.bin` from the internal card on the next boot. Marlin's "Firmware update trigger" sets it.

**Volumetric speed.** How much plastic per second the hotend melts, in mm³/s. The stock 3D20 hotend handles about 7.
