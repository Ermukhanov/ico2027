#!/usr/bin/env bash
# Disassemble with Intel syntax.
# Usage: read the corresponding command in the field manual.
set -u
objdump -d -M intel "$1" | less
