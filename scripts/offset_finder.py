#!/usr/bin/env python3
from pwn import cyclic,cyclic_find
import argparse
p=argparse.ArgumentParser();p.add_argument("--length",type=int,default=300);p.add_argument("--value");a=p.parse_args();print(cyclic(a.length).decode("latin1") if a.value is None else cyclic_find(int(a.value,0)))
