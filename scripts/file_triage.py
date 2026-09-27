#!/usr/bin/env python3
import argparse,hashlib,math,re
from pathlib import Path
from collections import Counter
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();b=Path(a.file).read_bytes();n=len(b);c=Counter(b)
e=-sum((v/n)*math.log2(v/n) for v in c.values()) if n else 0
print("size",n);print("sha256",hashlib.sha256(b).hexdigest());print("md5",hashlib.md5(b).hexdigest());print("entropy",round(e,4));print("header",b[:64].hex(" "))
for s in re.findall(rb"[ -~]{5,}",b)[:100]: print(s.decode("ascii","replace"))
