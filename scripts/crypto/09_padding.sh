#!/usr/bin/env bash
# Calculate SHA-style padding size.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/hash_padding.py" "$1" "$2"
