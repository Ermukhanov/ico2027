#!/usr/bin/env python3
import argparse,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();b=Path(a.file).read_bytes()
for n in ("md5","sha1","sha256","sha512"): print(n,getattr(hashlib,n)(b).hexdigest())
