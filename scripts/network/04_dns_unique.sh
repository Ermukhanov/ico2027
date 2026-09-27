#!/usr/bin/env bash
# List unique DNS queries.
# Usage: read the corresponding command in the field manual.
set -u
tshark -r "$1" -Y dns -T fields -e dns.qry.name | sort -u
