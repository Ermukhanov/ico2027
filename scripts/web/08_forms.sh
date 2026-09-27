#!/usr/bin/env bash
# Parse saved HTML forms.
# Usage: read the corresponding command in the field manual.
set -u
python3 "$HOME/ico2027/scripts/form_parser.py" page.html
