#!/usr/bin/env python3
import sys,math
from collections import Counter
b=open(sys.argv[1],"rb").read(); n=len(b); c=Counter(b)
print(-sum((v/n)*math.log2(v/n) for v in c.values()) if n else 0)
