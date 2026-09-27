#!/usr/bin/env bash
# Save the main page.
# Usage: read the corresponding command in the field manual.
set -u
curl -sk "$1" -o page.html
