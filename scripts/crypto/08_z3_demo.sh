#!/usr/bin/env bash
# Run a tiny Z3 constraint example.
# Usage: read the corresponding command in the field manual.
set -u
python3 -c 'from z3 import *; x=Int("x"); s=Solver(); s.add(x>10,x<20); print(s.check(),s.model())'
