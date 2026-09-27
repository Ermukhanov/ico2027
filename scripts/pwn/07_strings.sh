#!/usr/bin/env bash
# Find target strings.
# Usage: read the corresponding command in the field manual.
set -u
strings -a "$1" | grep -Ei 'flag|admin|secret|win'
