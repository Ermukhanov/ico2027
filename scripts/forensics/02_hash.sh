#!/usr/bin/env bash
# Hash a file.
# Usage: read the corresponding command in the field manual.
set -u
sha256sum "$1"; md5sum "$1"
