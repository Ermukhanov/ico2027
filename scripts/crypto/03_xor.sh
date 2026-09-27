#!/usr/bin/env bash
# Rank single-byte XOR keys.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/xor_singlebyte.py" "$1"
