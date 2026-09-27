#!/usr/bin/env bash
set -u
f="${1:?usage: quick_triage.sh FILE}"
file "$f"; stat "$f"; sha256sum "$f"; xxd -l 128 "$f"; strings -a -n 6 "$f" | head -100
command -v exiftool >/dev/null && exiftool "$f" || true
command -v binwalk >/dev/null && binwalk "$f" || true
