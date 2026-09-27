#!/usr/bin/env python3
import argparse,pefile
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();x=pefile.PE(a.file);print("machine",hex(x.FILE_HEADER.Machine));print("imagebase",hex(x.OPTIONAL_HEADER.ImageBase));print("entry",hex(x.OPTIONAL_HEADER.AddressOfEntryPoint));print([s.Name.rstrip(b"\0").decode(errors="replace") for s in x.sections])
