#!/usr/bin/env bash
# Carve recognizable files.
# Usage: read the corresponding command in the field manual.
set -u
mkdir -p carved; foremost -i "$1" -o carved
