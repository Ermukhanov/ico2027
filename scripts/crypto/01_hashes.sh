#!/usr/bin/env bash
# Print common hashes.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/hash_report.py" "$1"
