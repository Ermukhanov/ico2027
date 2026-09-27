#!/usr/bin/env bash
# Extract DNS queries.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/dns_extract.py" "$1"
