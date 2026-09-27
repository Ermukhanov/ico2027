#!/usr/bin/env python3
import sys
n=int(sys.argv[1])+int(sys.argv[2]); pad=(56-(n+1)%64)%64
print("message bytes:",n,"padding bytes:",1+pad+8,"total:",n+1+pad+8)
