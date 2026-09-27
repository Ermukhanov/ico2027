#!/usr/bin/env bash
# Follow TCP stream 0.
# Usage: read the corresponding command in the field manual.
set -u
tshark -r "$1" -z follow,tcp,ascii,0
