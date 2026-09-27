#!/usr/bin/env bash
# List ELF sections.
# Usage: read the corresponding command in the field manual.
set -u
readelf -S "$1"
