#!/usr/bin/env bash
# Inspect the first 256 bytes.
# Usage: read the corresponding command in the field manual.
set -u
xxd -g 1 -l 256 "$1"
