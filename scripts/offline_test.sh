#!/usr/bin/env bash
set -euo pipefail
R="$HOME/ico2027"; source "$R/.venv/bin/activate"
python -m compileall -q "$R/scripts"
python - <<'PY'
import pwn,scapy,Crypto,z3,requests,elftools,pefile,capstone
print("PYTHON_IMPORTS_OK")
PY
for x in file strings xxd readelf objdump gdb tshark ffprobe exiftool 7z jq sqlite3; do command -v "$x" >/dev/null && echo "OK $x" || echo "MISSING $x"; done
