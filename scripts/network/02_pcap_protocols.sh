#!/usr/bin/env bash
# Protocol hierarchy.
# Usage: read the corresponding command in the field manual.
set -u
tshark -r "$1" -q -z io,phs
