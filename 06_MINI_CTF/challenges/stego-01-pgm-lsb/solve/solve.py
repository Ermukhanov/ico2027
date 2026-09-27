from pathlib import Path
txt=(Path(__file__).resolve().parents[1]/"challenge/hidden.pgm").read_text()
tokens="\n".join(line.split("#",1)[0] for line in txt.splitlines()).split()
# P2, width, height, maxval, then pixels
pixels=list(map(int,tokens[4:]))
bits=''.join(str(p&1) for p in pixels)
out=bytes(int(bits[i:i+8],2) for i in range(0,len(bits)-7,8))
print((out.split(b"}",1)[0]+b"}").decode())
