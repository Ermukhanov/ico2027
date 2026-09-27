#!/usr/bin/env bash
# Extract useful printable strings.
# Usage: read the corresponding command in the field manual.
set -u
strings -a -n 6 "$1" | grep -Ei 'flag|ico|key|pass|token|http|user|admin'
