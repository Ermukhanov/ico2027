#!/usr/bin/env bash
# Factor a small integer.
# Usage: read the corresponding command in the field manual.
set -u
python3 -c 'import sympy as s; print(s.factorint(int("'$1'")))'
