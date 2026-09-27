#!/usr/bin/env bash
# Probe common CTF paths.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/web_probe.py" "$1"
