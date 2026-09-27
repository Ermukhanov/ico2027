#!/usr/bin/env bash
# Run the full triage helper.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/file_triage.py" "$1"
