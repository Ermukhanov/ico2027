#!/usr/bin/env bash
# Inspect HTTP methods.
# Usage: read the corresponding command in the field manual.
set -u
curl -sk -X OPTIONS "$1"
