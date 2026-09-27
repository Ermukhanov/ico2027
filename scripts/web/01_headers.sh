#!/usr/bin/env bash
# Fetch HTTP headers.
# Usage: read the corresponding command in the field manual.
set -u
curl -skI "$1"
