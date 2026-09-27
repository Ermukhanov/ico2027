#!/usr/bin/env bash
# Inspect TLS handshakes.
# Usage: read the corresponding command in the field manual.
set -u
tshark -r "$1" -Y tls.handshake
