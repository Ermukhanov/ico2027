#!/usr/bin/env bash
# Source this file to use the project-local Kali package extractions and zsteg.
ICO2027_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
export ICO2027_ROOT
export PATH="$ICO2027_ROOT/.local/bin:$ICO2027_ROOT/.gem/bin:$PATH"
export LD_LIBRARY_PATH="$ICO2027_ROOT/.local/app-root/usr/lib/x86_64-linux-gnu:$ICO2027_ROOT/.local/app-root/usr/lib:$ICO2027_ROOT/.local/apt-root/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export GEM_HOME="$ICO2027_ROOT/.gem"
export GEM_PATH="$GEM_HOME:$(ruby -e 'print Gem.path.join(":")')"
