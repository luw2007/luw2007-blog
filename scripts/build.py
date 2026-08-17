from pathlib import Path
import os
import shutil

from pelican import Pelican
from pelican.settings import read_settings

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
OUTPUT = ROOT / "output"

shutil.rmtree(OUTPUT, ignore_errors=True)
settings = read_settings(path=str(ROOT / "pelicanconf.py"))
Pelican(settings).run()

for path in OUTPUT.rglob("*"):
    if path.suffix not in {".html", ".xml"}:
        continue
    text = path.read_text(encoding="utf-8")
    path.write_text("\n".join(line.rstrip() for line in text.splitlines()) + "\n", encoding="utf-8")
