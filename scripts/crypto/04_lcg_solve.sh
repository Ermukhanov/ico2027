#!/usr/bin/env bash
# Recover LCG a/c from three states.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/lcg_solver.py" "$1" "$2" "$3"
