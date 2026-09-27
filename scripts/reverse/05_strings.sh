#!/usr/bin/env bash
# Find interesting binary strings.
# Usage: read the corresponding command in the field manual.
set -u
strings -a "$1" | grep -Ei 'flag|secret|admin|win|password|token'
