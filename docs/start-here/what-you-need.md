# What you need

## For a normal install

| Item | Why | Notes |
|---|---|---|
| Windows PC | Dremel's firmware updater only runs on Windows | A virtual machine with USB pass-through can work, but a real PC is easier |
| USB cable (Type B) | Connects the printer to the PC | The same kind of cable most desktop printers use |
| Dremel 3D20 USB driver | Lets Windows see the printer | Linked from the [install wiki](https://github.com/moonglow/FlashForge_Marlin/wiki/Installing-Marlin-on-Dremel-3D20) |
| Dremel 3D20 firmware updater | Installs the first Marlin build | From [Dremel's 3D20 documentation page](https://digilab.dremel.com/service-3d20-documentation) |
| Marlin release for the 3D20 | The new firmware | From [moonglow/FlashForge_Marlin releases](https://github.com/moonglow/FlashForge_Marlin/releases) |
| SD card for prints | You will print from it | The card slot on the side of the printer |
| A slicer | Turns models into G-code | [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) or [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura/) |

## For updates, going back to stock, or recovery

| Item | Why | Notes |
|---|---|---|
| 2.5 mm hex key | Opens the bottom cover (six screws) | The cover is held by a grounding strap, so lift it gently |
| Micro SD card reader | Edits the internal card on the main board | Any USB card reader works |

## Only if a flash fails

| Item | Why | Notes |
|---|---|---|
| ST-Link programmer | Writes firmware straight to the chip | About $10 to $15. See [ST-Link recovery](../troubleshooting/st-link-recovery.md#buy-an-st-link) |
| Three female to female jumper wires | Connect the ST-Link to the board | Usually included with clone ST-Link sticks |
| Programming software | Drives the ST-Link | With a clone ST-Link V2, use [STM32 ST-Link Utility](https://www.st.com/en/development-tools/stsw-link004.html). With a genuine ST-Link, use [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html). Both need a free ST account |
| Multimeter with a continuity beep | Checks that each wire reaches the right chip leg | A basic one is fine |
| Clip leads or a soldering iron | Solid contact on the debug connector | Optional, but loose jumper wires are the most common cause of failed connections |

## Skills

You don't need to solder or build firmware. You should be comfortable:

- Removing and replacing screws on the bottom of the printer.
- Copying, renaming, and deleting files, with file extensions shown. In Windows File Explorer, turn on **View > Show > File name extensions**.
- Sending a G-code command from the printer screen or a USB terminal. We explain each one when it comes up.
