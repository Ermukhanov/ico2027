#!/usr/bin/env bash
# Check WordPress REST.
# Usage: read the corresponding command in the field manual.
set -u
curl -sk "$1/wp-json/"
