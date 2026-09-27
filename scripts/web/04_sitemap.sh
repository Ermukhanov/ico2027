#!/usr/bin/env bash
# Check sitemap.xml.
# Usage: read the corresponding command in the field manual.
set -u
curl -sk "$1/sitemap.xml"
