#!/usr/bin/env bash
# Predict future LCG states.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/lcg_predict.py" "$1" "$2" "$3" -n 20
