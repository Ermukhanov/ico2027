#!/usr/bin/env python3
import argparse,re
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args()
for x in re.findall(r"0x[0-9a-fA-F]{6,16}",open(a.file,errors="replace").read()): print(x,int(x,16))
