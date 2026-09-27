#!/usr/bin/env bash
set -euo pipefail
R="$HOME/ico2027"
getent hosts github.com >/dev/null || { echo "Network/DNS unavailable; stop."; exit 2; }
sudo apt update
sudo apt install -y python3-full python3-venv python3-pip python3-dev build-essential git curl wget file binutils gdb ffmpeg sox exiftool tshark tcpdump p7zip-full unzip zip jq sqlite3
python3 -m venv "$R/.venv"
source "$R/.venv/bin/activate"
python -m pip install -U pip setuptools wheel
python -m pip install -r "$R/docs/requirements.txt"
mkdir -p "$R/10_WHEELS"
python -m pip download -d "$R/10_WHEELS" -r "$R/docs/requirements.txt"
sha256sum "$R"/10_WHEELS/* > "$R/10_WHEELS/SHA256SUMS.txt" || true
