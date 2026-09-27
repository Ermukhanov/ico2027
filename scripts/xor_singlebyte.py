#!/usr/bin/env python3
import argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();b=Path(a.file).read_bytes();r=[]
for k in range(256):
 o=bytes(x^k for x in b);score=sum(32<=x<127 or x in (9,10,13) for x in o)/max(1,len(o));r.append((score,k,o[:120]))
for s,k,o in sorted(r,reverse=True)[:10]: print(f"{s:.3f} 0x{k:02x}",o)
