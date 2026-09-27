#!/usr/bin/env bash
# Search embedded signatures.
# Usage: read the corresponding command in the field manual.
set -u
binwalk "$1"
