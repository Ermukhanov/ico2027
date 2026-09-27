#!/usr/bin/env bash
# Check robots.txt.
# Usage: read the corresponding command in the field manual.
set -u
curl -sk "$1/robots.txt"
