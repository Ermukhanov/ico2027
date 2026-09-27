#!/usr/bin/env bash
# List TCP streams.
# Usage: read the corresponding command in the field manual.
set -u
tshark -r "$1" -T fields -e tcp.stream | sort -nu
