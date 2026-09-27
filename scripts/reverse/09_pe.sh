#!/usr/bin/env bash
# PE overview.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/pe_triage.py" "$1"
