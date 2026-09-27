#!/usr/bin/env bash
# ELF overview.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/elf_triage.py" "$1"
