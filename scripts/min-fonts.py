#!/usr/bin/env python
# type:ignore

import json

from fontTools import subset, ttLib

CLASSES = json.load(open("./scripts/classes.json"))["classes"]  # noqa

CLASSES = [c[3:] for c in CLASSES]


class OPTIONS_ONE:
    recalc_bounds = False
    recalc_timestamp = False
    font_number = 0


class OPTIONS_TWO:
    flavor = "woff2"
    with_zopfli = True
    harfbuzz_repacker = True
    canonical_order = False


print("loading font")
font = ttLib.TTFont(
    "./vgarchive/static/fonts/bootstrap-icons.woff2",
    flavor="woff2",
    lazy=False,
    recalcBBoxes=False,
)

print("subsetting used glyphs")
subsetter = subset.Subsetter()
subsetter.populate(glyphs=CLASSES)
subsetter.subset(font)

print("saving minimal fonts")
subset.save_font(
    font, "./vgarchive/static/fonts/bootstrap-icons.min.woff2", options=OPTIONS_TWO
)
