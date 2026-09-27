#!/usr/bin/env bash
# List symbols.
# Usage: read the corresponding command in the field manual.
set -u
readelf -s "$1"
