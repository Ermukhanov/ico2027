#!/usr/bin/env python3
import argparse,struct
p=argparse.ArgumentParser();p.add_argument("value");p.add_argument("--bits",choices=[32,64],type=int,default=64);a=p.parse_args()
print(struct.pack("<Q" if a.bits==64 else "<I",int(a.value,0)).hex())
