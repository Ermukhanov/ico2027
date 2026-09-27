#!/usr/bin/env python3
import argparse,subprocess
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();subprocess.run(["ffprobe","-hide_banner",a.file])
