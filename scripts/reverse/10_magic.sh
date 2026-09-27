#!/usr/bin/env bash
# Search embedded signatures.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/magic_scan.py" "$1"
