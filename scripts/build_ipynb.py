#!/usr/bin/env python3
"""Convert staged section markdown (nbmd/<stem>.md) → notebooks/<stem>.ipynb.

Each section notebook is a single markdown cell whose source is the authored
markdown (one `## ` heading + body). Run from the repo root:

    python3 scripts/build_ipynb.py            # convert every nbmd/*.md
    python3 scripts/build_ipynb.py 01         # only stems starting "01-"

The nbmd/ staging dir is git-ignored; the notebooks/ output is the committed
source of truth. This mirrors the docker-ct authoring flow.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "nbmd"
OUT = ROOT / "notebooks"


def to_cell_source(text: str):
    # Notebook cell source is a list of lines with trailing newlines kept
    # (except the last). Normalise trailing whitespace on the file as a whole.
    text = text.rstrip("\n")
    return [l + "\n" for l in text.split("\n")[:-1]] + [text.split("\n")[-1]] if text else [""]


def build(md_path: Path):
    text = md_path.read_text()
    nb = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": to_cell_source(text)}
        ],
        "metadata": {"language_info": {"name": "python"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    out = OUT / (md_path.stem + ".ipynb")
    out.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
    return out


def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    OUT.mkdir(exist_ok=True)
    n = 0
    for md in sorted(SRC.glob("*.md")):
        if prefix and not md.stem.startswith(prefix):
            continue
        build(md)
        n += 1
    print(f"built {n} notebook(s) into {OUT}")


if __name__ == "__main__":
    main()
