#!/usr/bin/env bash
# Show HTTP requests.
# Usage: read the corresponding command in the field manual.
set -u
tshark -r "$1" -Y 'http.request'
