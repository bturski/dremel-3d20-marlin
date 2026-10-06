# Choose a build

The firmware comes from the [moonglow/FlashForge_Marlin](https://github.com/moonglow/FlashForge_Marlin) project. It is Marlin 2.0.9.x adapted for FlashForge printers and the Dremel 3D20.

## Download

1. Open the [releases page](https://github.com/moonglow/FlashForge_Marlin/releases).
2. Download the newest release zip. At the time of writing this is **v0.15.1**, file `color_ui_01152023.zip`, which contains Marlin 2.0.9.5.
3. Unzip it somewhere you can find it.

## Pick the right file

The zip holds builds for many printers. Only two are for the 3D20:

| File | Use it when |
|---|---|
| `dremel_2.0.9.5_01152023.bin` | **Start here.** The standard build |
| `dremel_2.0.9.5_la_01152023.bin` | You want Linear Advance and are ready to calibrate it |

Everything else (`dreamer_`, `inventor_`, `nx_`) is for a different printer. Those files are encrypted with FlashForge's key, not Dremel's. On a 3D20 they install as garbage and the printer won't boot.

!!! danger
    Copy only the file you picked. Leave the rest of the zip out of every folder you use from here on.

### Check your download (optional)

These SHA-256 values are for the v0.15.1 files. If your release is newer, skip this check.

| File | SHA-256 |
|---|---|
| `dremel_2.0.9.5_01152023.bin` | `1418ae14b56f86c8ac1bd817cb06c39134281644e0d10810a1f6eb90ad4a6bd5` |
| `dremel_2.0.9.5_la_01152023.bin` | `64f7fc2a2c13142ff1d21594b5765d997aaf6e09ae85a5c65b97ae6c06f9037f` |

In Windows PowerShell:

```powershell
Get-FileHash .\dremel_2.0.9.5_01152023.bin -Algorithm SHA256
```

## Standard or Linear Advance?

Linear Advance adjusts extruder pressure as the print head speeds up and slows down. Tuned well, it gives sharper corners and more even walls.

- The `la` build ships with the Linear Advance factor (K) set to 0, which means it does nothing until you calibrate it.
- With Linear Advance on, this build turns off S-curve acceleration. The standard build keeps S-curve on.
- Calibrating K takes a test print. The [Marlin K-factor calibration tool](https://marlinfw.org/tools/lin_advance/k-factor.html) generates one.

If you're new to this, use the standard build. You can switch later with a normal update.

## Screen style

The v0.15.1 release ships the **Color UI** with touch support. Older releases also offered a classic Marlin screen and an MKS style screen. If you want one of those, check the release notes on the releases page before you download.

## Advanced: what the build contains

The 3D20 build is the Dreamer NX configuration with the heated bed and chamber sensor turned off. The full list of settings is on the [Firmware values](../reference/firmware-values.md) page.

If you build your own firmware, use the project's `marlin_builder.sh` with `-m dremel`. The script encrypts the result with the Dremel key for you.
