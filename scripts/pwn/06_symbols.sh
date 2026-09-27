#!/usr/bin/env bash
# Find likely win/flag/admin symbols.
# Usage: read the corresponding command in the field manual.
set -u
nm -an "$1" | grep -Ei 'win|flag|admin|secret'
