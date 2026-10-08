# OctoPrint on a Raspberry Pi

OctoPrint runs on a Raspberry Pi connected to the printer's USB port. It puts the 3D20 on your network, so you can upload, start, watch, and stop prints from a browser.

This page was written for a **Raspberry Pi 3B**, but the steps are the same on any Pi that OctoPrint recommends.

## What it adds

- **Printing over the network.** The 3D20's built-in Wi-Fi doesn't work under this Marlin build, and OctoPrint fills that gap. No more carrying SD cards.
- **Send from the slicer.** PrusaSlicer and Cura can upload, and even start, a print with one click.
- **A terminal.** Setup commands like `M303` (heater tuning), `M503` (show settings), and `M420 S1 V` (show the mesh) are easy to send. See [First setup](../firmware/first-setup.md).
- **Cancel one object.** The firmware can't skip a single part, but OctoPrint's **Cancel Objects** plugin can. The PrusaSlicer profile in this guide already labels objects the way it needs.
- **Webcam and timelapse.** Watch prints from another room and record timelapses.

## What you need

| Item | Notes |
|---|---|
| Raspberry Pi 3B, 3B+, 4B, or Zero 2 | OctoPrint's recommended models. Older or slower Pis can cause stutters and blobs |
| Power supply for the Pi | Use the official supply for your model, 2.5 A or more for a Pi 3. A weak supply is the most common cause of OctoPrint problems |
| microSD card | 16 GB or larger |
| USB cable, Type A to Type B | The same kind of cable you used for the Dremel updater |
| Camera (optional) | A Raspberry Pi camera module or a USB webcam |

!!! note "Pi 3B and Wi-Fi"
    The Pi 3B only connects to **2.4 GHz** Wi-Fi. If your router uses one name for both bands, it usually works anyway. If the Pi never shows up on your network, this is the first thing to check.

## 1. Flash OctoPi

OctoPi is a ready-made system image with OctoPrint already installed. The steps follow [OctoPrint's download page](https://octoprint.org/download/).

1. Install [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your PC.
2. Click **Choose OS**, then **Other specific-purpose OS > 3D printing > OctoPi**, and pick the **stable** version.
3. Choose your microSD card as the storage.
4. Open the advanced options (the gear button, or ++ctrl+shift+x++) and set:
    - **Hostname:** `octopi` (the default is fine)
    - **Username and password:** for logging in to the Pi itself over SSH. This is not your OctoPrint login.
    - **Wireless LAN:** your Wi-Fi name, password, and country
    - **Locale:** your time zone
    - **SSH:** turn it on. It helps with troubleshooting later
5. Write the card.

!!! warning
    When Windows offers to format the card after writing, click **Cancel**. Formatting it erases OctoPi.

## 2. Connect the hardware

1. Put the card in the Pi.
2. Connect the Pi to the printer with the USB cable.
3. Plug in the Pi's power supply. The first boot takes a few minutes.

??? tip "Printer screen stays on when the printer is off?"
    The Pi's USB port can feed 5 V back into the printer's board, so the screen stays lit with the printer switched off. It's harmless but confusing. The usual fix is a small piece of tape over the **5 V pin** (pin 1) on the USB Type A end of the cable. Check a USB Type A pinout diagram to find it, since taping the wrong pin stops the connection. The data pins still work, and the printer runs from its own power supply.

## 3. Run the setup wizard

1. On your PC, open `http://octopi.local`. If that doesn't load, find the Pi's IP address in your router's device list and open `http://<that address>`.
2. Follow the wizard:
    - **Access control:** create your OctoPrint user and password.
    - **Online connectivity check:** turn it on.
    - **Anonymous usage tracking** and **plugin blacklist:** your choice.
    - **Default printer profile:** use the values below.

| Section | Setting | Value |
|---|---|---|
| General | Name | Dremel 3D20 Marlin |
| Print bed & build volume | Form factor | Rectangular |
| Print bed & build volume | Origin | **Center** |
| Print bed & build volume | Heated bed | **Off** |
| Print bed & build volume | Heated chamber | Off |
| Print bed & build volume | Width, depth, height | 230, 150, 140 mm |
| Axes | X, Y speed | 6000 mm/min |
| Axes | Z speed | 1200 mm/min (the firmware's limit of 20 mm/s) |
| Axes | E speed | 300 mm/min |
| Hotend & extruder | Nozzle diameter | 0.4 mm |
| Hotend & extruder | Number of extruders | 1 |

The origin and heated bed settings matter most. They match the [slicer setup](../slicers/index.md), and with the heated bed off, OctoPrint won't show bed controls the printer doesn't have.

## 4. Connect to the printer

1. Turn the printer on and wait for the Marlin screen.
2. In OctoPrint's **Connection** panel on the left, leave **Serial Port** and **Baudrate** on **AUTO**.
3. Tick **Save connection settings** and **Auto-connect on server startup**.
4. Click **Connect**. The state changes to **Operational**, and temperatures start graphing.
5. Open the **Terminal** tab and send `M115`. Marlin replies with its version. That confirms two-way communication.

## 5. Connect your slicer

First, make a key for the slicer in OctoPrint. Open **Settings** (the wrench icon) and go to **Application Keys**. Generate a key for your slicer and copy it.

=== "PrusaSlicer"

    These steps follow [Prusa's OctoPrint help article](https://help.prusa3d.com/en/article/sending-files-to-octoprint-duet_1663/).

    1. In the printer preset list, choose **Add physical printer**, or click the cog icon next to the printer preset.
    2. Give it a name, and pick **Dremel 3D20 Marlin** as its preset.
    3. **Host type:** OctoPrint.
    4. **Hostname, IP or URL:** `octopi.local`, or the Pi's IP address.
    5. **API key:** paste the key from OctoPrint.
    6. Click **Test**. It should report a successful connection.
    7. After slicing, a **Send to printer** button appears next to **Export G-code**. It offers **Upload** or **Upload and print**.

=== "Cura"

    1. Open **Marketplace**, search for **OctoPrint Connection**, install it, and restart Cura.
    2. Go to **Preferences > Configure Cura > Printers**, select **Dremel 3D20 (Marlin)**, and click **Connect OctoPrint**.
    3. Pick your OctoPrint from the list, or add it by address.
    4. Click **Request** to get an API key, and approve the request in the OctoPrint browser tab.
    5. After slicing, the main button changes to **Print with OctoPrint**.

## 6. Recommended plugins

Install these from **Settings > Plugin Manager > Get More**.

| Plugin | Why |
|---|---|
| **Cancel Objects** | Skip one failed part and keep printing the rest. Works with the object labels from the PrusaSlicer profile (**Label objects: OctoPrint comments**). With Cura, check the plugin's notes first |
| **PrintTimeGenius** | More accurate time estimates than OctoPrint's default |

OctoPi also includes the **Pi Support** plugin, which shows a warning if the Pi's power supply is too weak. Take that warning seriously. Under-voltage causes dropped connections and stutters.

## 7. Webcam (optional)

Plug in a USB webcam, or connect a Pi camera module to the camera connector with the Pi powered off. OctoPi detects most cameras on its own, and the picture appears on the **Control** tab.

On a Pi 3B, keep the camera at 1280 x 720 or lower. Higher settings can slow the Pi enough to cause pauses in the print.

## Remote access

Don't open OctoPrint to the internet with port forwarding. Anyone who finds it could control your printer. To watch from outside your home, use a VPN such as Tailscale, or a service built for OctoPrint, such as OctoEverywhere or Obico.

## Streaming vs. printing from SD

OctoPrint normally streams G-code to the printer line by line over USB. That's reliable, but a USB disconnect ends the print. For very long prints, you can upload the file to the printer's SD card from OctoPrint's **Files** panel and print from there. The printer then keeps going even if the Pi drops out. Uploading over USB to the SD card is slow, though.

## Troubleshooting

| Problem | Fix |
|---|---|
| `octopi.local` doesn't load | Use the Pi's IP address from your router. Check that the Pi 3B is on a 2.4 GHz network. Recheck the Wi-Fi details in Imager and write the card again |
| Connection fails: "No more candidates to test" | Turn the printer on first. Try another cable, since some cables only carry power. Try another USB port on the Pi |
| Lightning bolt or under-voltage warning | Use a proper 2.5 A or larger power supply. Phone chargers often aren't enough |
| Printer screen stays on when switched off | Tape the 5 V pin. See [step 2](#2-connect-the-hardware) |
| Stutters or blobs only when printing through OctoPrint | Lower the webcam resolution, check for under-voltage, and remove plugins you don't use |
| Connection drops in the middle of prints | Keep the USB cable short and away from the motor wires. For long jobs, print from SD |
| PrusaSlicer **Test** fails | Check the address and the API key. Make sure the key was generated under **Application Keys** |

## Going further: Klipper

Klipper is another printer firmware that also runs on a Raspberry Pi. It can print faster and smoother than Marlin, using features like input shaping. Switching means replacing Marlin with a Klipper build on the board, which on the 3D20 would mean using the ST-Link. It's a much bigger project than OctoPrint, and isn't covered here yet. If you try it, please [share your notes](../contributing.md).
