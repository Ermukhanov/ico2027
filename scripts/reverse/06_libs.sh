#!/usr/bin/env bash
# Show dynamic dependencies.
# Usage: read the corresponding command in the field manual.
set -u
ldd "$1"
