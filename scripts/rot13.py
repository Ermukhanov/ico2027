#!/usr/bin/env python3
"""Decode a text file with ROT13."""
import argparse
import codecs
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("file")
a = p.parse_args()
print(codecs.decode(Path(a.file).read_text(errors="replace"), "rot_13"), end="")
