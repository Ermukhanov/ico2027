#!/usr/bin/env bash
# Search for pop RDI.
# Usage: read the corresponding command in the field manual.
set -u
ROPgadget --binary "$1" | grep -E 'pop rdi|ret'
