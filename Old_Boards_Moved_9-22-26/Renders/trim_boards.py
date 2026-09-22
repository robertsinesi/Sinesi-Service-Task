#!/usr/bin/env python3
"""Trim uniform background padding from KiCad board renders.

Usage:
    python trim_boards.py rtm_smd_top.png rtm_smd_bottom.png
    python trim_boards.py *.png

Backs each original up as <name>_untrimmed.png before overwriting.
"""

import sys
import os
import numpy as np
from PIL import Image

TOLERANCE = 12   # how far from the corner colour counts as board
MARGIN = 0       # pixels of padding to leave on each side


def trim(path):
    img = Image.open(path).convert("RGB")
    arr = np.array(img).astype(int)

    bg = arr[0, 0]
    diff = np.abs(arr - bg).sum(axis=2)
    mask = diff > TOLERANCE

    if not mask.any():
        print(f"{path}: no content found, skipped")
        return

    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]

    top = max(0, rows[0] - MARGIN)
    left = max(0, cols[0] - MARGIN)
    bottom = min(arr.shape[0] - 1, rows[-1] + MARGIN)
    right = min(arr.shape[1] - 1, cols[-1] + MARGIN)

    stem, ext = os.path.splitext(path)
    backup = f"{stem}_untrimmed{ext}"
    if not os.path.exists(backup):
        img.save(backup)

    cropped = img.crop((left, top, right + 1, bottom + 1))
    cropped.save(path)

    print(f"{path}: {img.width}x{img.height} -> {cropped.width}x{cropped.height}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        trim(p)
