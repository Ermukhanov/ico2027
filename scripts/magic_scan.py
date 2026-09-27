#!/usr/bin/env python3
import argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();b=Path(a.file).read_bytes();m={b"PK\x03\x04":"ZIP",b"\x89PNG\r\n\x1a\n":"PNG",b"\xff\xd8\xff":"JPEG",b"RIFF":"RIFF",b"GIF89a":"GIF",b"%PDF":"PDF"}
for sig,n in m.items():
 i=0
 while True:
  i=b.find(sig,i)
  if i<0:break
  print(n,hex(i));i+=1
