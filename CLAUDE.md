# Palo Santo website

Static GitHub Pages site. No build step except the Spanish pages.

- `index.html` and `our-rhythms.html` (English) are the source of truth.
- `es/index.html` and `es/our-rhythms.html` are **generated**. After editing any text, markup or
  the `es:{...}` dictionary in an English page, run:

  ```bash
  python3 tools/build_es.py
  ```

  and commit the regenerated `es/` files with the change.
- Every visible string needs a `data-i18n` key with EN and ES entries in that page's `T` dictionary.
- Design rules live in `DESIGN.md`. The design skills are in `.claude/skills/`.
