#!/usr/bin/env bash
# Estimate entropy.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/entropy.py" "$1"
