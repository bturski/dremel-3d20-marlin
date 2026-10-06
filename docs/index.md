# Dremel 3D20 Marlin Guide

The Dremel 3D20 (also sold as the Idea Builder) is a solid little printer held back by locked firmware and a slicer that only Dremel supports. You can replace that firmware with Marlin 2, use any modern slicer, and print plain `.gcode` files.

This guide walks you through the whole job. It covers picking the right firmware file, installing it, setting up PrusaSlicer or UltiMaker Cura, and getting the printer back if a flash goes wrong.

## Where to start

| If you want to... | Go here |
|---|---|
| Understand what changes before you commit | [Before you start](start-here/index.md) |
| Install Marlin for the first time | [Choose a build](firmware/choose-a-build.md), then [Install Marlin](firmware/install.md) |
| Set up a slicer on a printer that already runs Marlin | [What every slicer needs](slicers/index.md) |
| Import ready-made profiles | [Downloads](reference/downloads.md) |
| Fix a printer that won't boot after a flash | [Failed flash](troubleshooting/failed-flash.md) |
| Fix a print problem | [Print problems](troubleshooting/print-problems.md) |

## The short version

1. Download the Marlin release and pick the **one** file built for the 3D20. It starts with `dremel_`.
2. Install it with Dremel's firmware updater. The updater folder must hold **only that one file**.
3. Tune the hotend, level the bed, and save the mesh.
4. Set up your slicer with the bed origin at the **center** and no heated bed. Or import our profiles.
5. Never copy start G-code from the stock Dremel profile. Some of those codes can overheat your motors under Marlin.

## Who this is for

Every page starts with the steps a beginner needs. Extra detail for advanced users sits in clearly marked sections, so you can skip it or dig in.

You don't need to know how to code or build firmware. You will need to remove the bottom cover of the printer for some tasks, and you should be comfortable doing that.

## About this guide

This is a community guide. It is not made by Dremel or by the authors of the firmware. The firmware comes from the [moonglow/FlashForge_Marlin](https://github.com/moonglow/FlashForge_Marlin) project. Every fact we took from somewhere else is linked on the [Sources](reference/sources.md) page, along with an archived copy in case the original goes away.

Found a mistake or have a tip? See [Contributing](contributing.md).
