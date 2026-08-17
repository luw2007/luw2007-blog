# luw2007-blog

Pelican source for <https://luw2007.github.io/>.

## Build

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
```

Generated files are written to `output/`. The `tuxlite_tbs` theme is vendored under `themes/` from `getpelican/pelican-themes` commit `1f59f2d12ef9bd8e3fc912d6645001c154f1f0f2`; its license is included with the theme.
