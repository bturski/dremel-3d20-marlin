# Contributing

This guide is meant to grow. Corrections, new slicers, new fixes, and photos of your board are all welcome.

## Quick fixes

Every page has an edit button (the pencil icon at the top). It opens the page on GitHub, where you can propose a change without installing anything.

## Bigger changes

1. Fork the repository and make a branch.
2. Install the tools: `pip install -r requirements.txt`
3. Preview the site: `mkdocs serve`, then open `http://127.0.0.1:8000`.
4. Run the checks: `python scripts/check_style.py` and `python scripts/build_profiles.py --check`.
5. Open a pull request. Say what you changed and how you tested it.

## Where things live

| Path | Contents |
|---|---|
| `docs/` | Every page of the site, in Markdown |
| `docs/downloads/` | Files people download: profiles and G-code |
| `scripts/build_profiles.py` | The values behind the PrusaSlicer and Cura profiles |
| `scripts/ff_firmware_tool.py` | Firmware encryption tool |
| `scripts/check_style.py` | The writing style checks |
| `mkdocs.yml` | Site settings and the page menu (`nav`) |
| `.github/workflows/` | Site publishing, checks, and monthly archiving |

## Adding a page

1. Create the Markdown file in the right folder under `docs/`.
2. Add it to `nav` in `mkdocs.yml`.
3. If you used an outside source, add it to [Sources](reference/sources.md) with an archive link.

## Adding a slicer

Copy the shape of the [PrusaSlicer](slicers/prusaslicer.md) page:

1. Option A, an importable profile, if the slicer supports one.
2. Option B, a table of settings with the default value, the new value, and why.
3. A "Check your setup" section.

Use the values on [What every slicer needs](slicers/index.md) so every slicer stays consistent.

## Writing style

The guide should read like a knowledgeable friend explaining things in person. Aim for an average reading level.

- **Short sentences.** One idea each.
- **Plain words.** "Use," not "utilize." "Check," not "verify the integrity of."
- **Second person.** "Turn the printer off," not "The printer should be turned off."
- **Steps are numbered.** Options and facts are tables or bullets.
- **Beginner first.** Put expert detail under a heading or box marked **Advanced**.
- **Say why.** A setting without a reason is hard to trust.
- **Link your source.** Every outside fact gets a link, and the source goes on the Sources page with an archive link.

The style check enforces a few rules automatically:

- No em dashes or en dashes. Use a period, a comma, or the word "to" for ranges ("10 to 15").
- No emoji.
- No filler phrases such as "it's worth noting," "delve," or "seamless."

## Reporting a problem

[Open an issue](https://github.com/bturski/dremel-3d20-marlin/issues/new/choose). For a printer problem, include your firmware version, your slicer and its version, and what you see on the screen.
