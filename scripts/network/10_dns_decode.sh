#!/usr/bin/env bash
# Join DNS labels and try decoders.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/dns_join_decode.py" "$1"
