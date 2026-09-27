#!/usr/bin/env bash
# Inspect the final 256 bytes.
# Usage: read the corresponding command in the field manual.
set -u
tail -c 256 "$1" | xxd -g 1
