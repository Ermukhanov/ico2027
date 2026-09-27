#!/usr/bin/env bash
# Find a cyclic offset.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/offset_finder.py" --value "$1"
