#!/usr/bin/env bash
# Run a harmless local check.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/pwn_local_check.py" "$1"
