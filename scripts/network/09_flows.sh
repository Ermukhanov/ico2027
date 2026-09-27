#!/usr/bin/env bash
# Summarize IP flows.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/pcap_summary.py" "$1"
