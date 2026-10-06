# Find your problem

Find what you see in the left column, then follow the link.

## The printer won't start properly

| What you see | Likely cause | Go to |
|---|---|---|
| Stops on the Dremel start screen and never reaches Marlin | Bad firmware installed. Bootloader is fine | [Failed flash: stuck on the start screen](failed-flash.md#stuck-on-the-start-screen) |
| Screen lights up but stays blank | Bad firmware, or damaged bootloader | [Failed flash: blank screen](failed-flash.md#blank-screen) |
| Nothing at all: no backlight, no fans | Power problem, not firmware | [Failed flash: no power](failed-flash.md#no-power-at-all) |
| Dremel updater never says "Printer Detected" | Driver, cable, or no working firmware | [Failed flash: updater can't see the printer](failed-flash.md#updater-cant-see-the-printer) |
| Put `dremel.bin` on the internal card, nothing happened | The update flag wasn't set | [Failed flash: SD card update ignored](failed-flash.md#sd-card-update-ignored) |

## Prints go wrong

| What you see | Go to |
|---|---|
| Parts print in a corner, or the printer says "move out of range" | [Print problems: position](print-problems.md#parts-print-in-the-wrong-place) |
| The print starts with a cold nozzle | [Print problems: temperature](print-problems.md#printing-starts-before-the-nozzle-is-hot) |
| Motors are very hot, loud, or smell | [Print problems: motors](print-problems.md#motors-run-hot-or-loud) |
| First layer won't stick | [Print problems: adhesion](print-problems.md#first-layer-wont-stick) |
| Stringing, blobs, or clogs | [Print problems: retraction](print-problems.md#stringing-blobs-or-clogs) |
| Prints are slow, or take much longer than the slicer said | [Print problems: speed](print-problems.md#prints-are-slow-or-the-time-estimate-is-wrong) |
| "Unknown command" messages | [Print problems: unknown commands](print-problems.md#unknown-command-messages) |
| Mesh doesn't load | [Print problems: mesh](print-problems.md#mesh-doesnt-load) |
| File doesn't show up on the SD card | [Print problems: files](print-problems.md#file-doesnt-show-up) |

## Still stuck?

Search the firmware project's [issues](https://github.com/moonglow/FlashForge_Marlin/issues) and [discussions](https://github.com/moonglow/FlashForge_Marlin/discussions). If you solve something new, please add it here. See [Contributing](../contributing.md).
