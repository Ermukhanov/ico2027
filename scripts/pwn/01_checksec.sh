#!/usr/bin/env bash
# Check mitigations.
# Usage: read the corresponding command in the field manual.
set -u
checksec --file="$1"
