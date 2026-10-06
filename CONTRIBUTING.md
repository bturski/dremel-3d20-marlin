# Contributing

Thanks for helping. The full contributing guide, including the writing style rules, is on the site:

**https://bturski.github.io/dremel-3d20-marlin/contributing/**

The short version:

1. `pip install -r requirements.txt`
2. Preview with `mkdocs serve`.
3. Before you open a pull request, run:

    ```
    python scripts/check_style.py
    python scripts/build_profiles.py --check
    mkdocs build --strict
    ```

4. Add any outside source to `docs/reference/sources.md` with an archive link.
5. Keep the writing plain and short. No em dashes, en dashes, or emoji.
