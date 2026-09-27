#!/usr/bin/env bash
# Disassemble main non-interactively.
# Usage: read the corresponding command in the field manual.
set -u
gdb -q "$1" -ex 'set disassembly-flavor intel' -ex 'disassemble main' -ex quit
