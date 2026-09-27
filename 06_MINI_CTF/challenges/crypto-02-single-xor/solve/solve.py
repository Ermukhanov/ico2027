from pathlib import Path
data=bytes.fromhex((Path(__file__).resolve().parents[1]/"challenge/cipher.hex").read_text().strip())
for k in range(256):
 out=bytes(b^k for b in data)
 if out.startswith(b"ICO{") and out.endswith(b"}"): print(f"key=0x{k:02x} {out.decode()}")
