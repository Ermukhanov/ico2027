#!/usr/bin/env bash
# List ROP gadgets.
# Usage: read the corresponding command in the field manual.
set -u
ROPgadget --binary "$1"
