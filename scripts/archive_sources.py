#!/usr/bin/env python3
"""Ask the Wayback Machine to save every outside page this guide links to.

Run by .github/workflows/archive-sources.yml once a month. You can also run
it by hand:
    python scripts/archive_sources.py            # save everything
    python scripts/archive_sources.py --list     # only print the links

Links to shopping searches and to the Wayback Machine itself are skipped.
"""

import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\((https?://[^)\s]+)\)")

SKIP_HOSTS = (
    "web.archive.org", "archive.org", "amazon.", "aliexpress.", "mouser.",
    "127.0.0.1", "localhost", "bturski.github.io", "github.com/bturski/",
)
DELAY_SECONDS = 15  # stay well under the Wayback Machine's rate limit


def collect():
    urls = set()
    for path in [*ROOT.glob("docs/**/*.md"), ROOT / "README.md"]:
        for url in LINK.findall(path.read_text(encoding="utf-8")):
            if not any(h in url for h in SKIP_HOSTS):
                urls.add(url.rstrip(".,"))
    return sorted(urls)


def save(url):
    req = urllib.request.Request(
        "https://web.archive.org/save/" + url,
        headers={"User-Agent": "dremel-3d20-marlin archive job (github.com/bturski/dremel-3d20-marlin)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:  # network errors should not stop the run
        return f"error: {e}"


def main():
    urls = collect()
    if "--list" in sys.argv:
        print("\n".join(urls))
        return
    failed = 0
    for i, url in enumerate(urls, 1):
        status = save(url)
        ok = status == 200
        failed += not ok
        print(f"[{i}/{len(urls)}] {status} {url}", flush=True)
        time.sleep(DELAY_SECONDS)
    print(f"Done. {len(urls) - failed} saved, {failed} not saved.")


if __name__ == "__main__":
    main()
