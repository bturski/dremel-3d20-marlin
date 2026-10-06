#!/usr/bin/env python3
"""Check the guide's writing style rules and file formats.

Run from the repository root:
    python scripts/check_style.py

Fails if any Markdown or text file has an em dash, en dash, emoji, or a
listed filler phrase, or if a JSON or INI download doesn't parse.
"""

import configparser
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEXT_GLOBS = ["*.md", "docs/**/*.md", "docs/**/*.gcode", "docs/**/*.ini",
              "docs/**/*.json", "scripts/*.py", ".github/**/*.yml", ".github/**/*.md",
              "mkdocs.yml"]

DASHES = {"\u2014": "em dash", "\u2013": "en dash"}

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]"
)

# Phrases that make writing sound generated. Matched case-insensitively.
FILLER = [
    "it's worth noting", "it is worth noting", "worth noting that", "delve",
    "seamless", "seamlessly", "leverage", "robust", "game-changer", "game changer",
    "in today's", "unlock the", "dive into", "deep dive", "navigate the",
    "rest assured", "needless to say", "in conclusion", "at the end of the day",
    "a testament to", "plays a crucial role", "it is important to note",
]
# Pages allowed to mention the filler list itself.
FILLER_EXEMPT = {"docs/contributing.md", "scripts/check_style.py", "CONTRIBUTING.md"}


def text_files():
    seen = set()
    for pattern in TEXT_GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file() and path not in seen:
                seen.add(path)
                yield path


def main():
    problems = []

    for path in sorted(text_files()):
        rel = path.relative_to(ROOT).as_posix()
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for ch, name in DASHES.items():
                if ch in line:
                    problems.append(f"{rel}:{n}: {name}")
            if EMOJI.search(line):
                problems.append(f"{rel}:{n}: emoji")
            if rel not in FILLER_EXEMPT:
                low = line.lower()
                for phrase in FILLER:
                    if re.search(r"\b" + re.escape(phrase) + r"\b", low):
                        problems.append(f'{rel}:{n}: filler phrase "{phrase}"')

    for path in ROOT.glob("docs/downloads/**/*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except ValueError as e:
            problems.append(f"{path.relative_to(ROOT)}: invalid JSON: {e}")

    for path in ROOT.glob("docs/downloads/**/*.ini"):
        cp = configparser.RawConfigParser(comment_prefixes=("#", ";"), interpolation=None)
        try:
            cp.read_string(path.read_text(encoding="utf-8"))
        except configparser.Error as e:
            problems.append(f"{path.relative_to(ROOT)}: invalid INI: {e}")

    if problems:
        print("Style check failed:")
        for p in problems:
            print(f"  {p}")
        sys.exit(1)
    print("Style check passed.")


if __name__ == "__main__":
    main()
