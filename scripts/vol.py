#!/usr/bin/env python3
"""Run the checked-out Volatility 3 CLI with project-local cache and Python."""
from __future__ import annotations

import os
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent.parent
VENV_PYTHON = ROOT / ".venv" / "bin" / "python"
ENTRYPOINT = ROOT / "05_REPOS" / "volatility3" / "vol.py"

if not ENTRYPOINT.is_file():
    raise SystemExit(f"Volatility checkout is missing: {ENTRYPOINT}")

if Path(sys.prefix).resolve() != (ROOT / ".venv").resolve():
    if not VENV_PYTHON.is_file():
        raise SystemExit(f"Project Python is missing: {VENV_PYTHON}")
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])

os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".cache"))
sys.path.insert(0, str(ENTRYPOINT.parent))
sys.argv[0] = str(ENTRYPOINT)
runpy.run_path(str(ENTRYPOINT), run_name="__main__")
