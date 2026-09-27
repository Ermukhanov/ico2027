#!/usr/bin/env python3
print("from pwn import *")
print("context.binary = ELF('./challenge', checksec=False)")
print("# io = process(context.binary.path)")
print("# io = remote('HOST', PORT)")
print("# payload = flat({OFFSET: [RET, POP_RDI, ARG, WIN]})")
print("# io.sendline(payload); io.interactive()")
