#!/usr/bin/env bash
# Calculate a modular inverse.
# Usage: read the corresponding command in the field manual.
set -u
python3 -c 'print(pow(int("'$1'"),-1,int("'$2'")))'
