#!/usr/bin/env python3
print("from pwn import *")
print("context.binary = ELF('./challenge', checksec=False)")
print("# payload = fmtstr_payload(OFFSET, {TARGET: VALUE}, write_size='byte')")
