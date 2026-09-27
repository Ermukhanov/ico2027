#!/usr/bin/env python3
import argparse
from elftools.elf.elffile import ELFFile
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args()
with open(a.file,"rb") as f:
 e=ELFFile(f);print("class",e.elfclass,"machine",e["e_machine"],"entry",hex(e["e_entry"]))
 for s in e.iter_sections():print(s.name,hex(s["sh_addr"]),s["sh_size"])
