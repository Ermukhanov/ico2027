#!/usr/bin/env python3
"""Recover a 32-bit LCG state when the low bits of x2 are hidden."""
import argparse
import math

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("x2_top", type=int, help="known high bits of x2")
p.add_argument("--x0", type=int, default=3398650787)
p.add_argument("--x1", type=int, default=3458068990)
p.add_argument("--x3", type=int, default=27663828)
p.add_argument("--bits", type=int, default=16, help="number of hidden low bits")
p.add_argument("--modulus", type=int, default=2**32)
a = p.parse_args()
if not 1 <= a.bits <= 24 or a.modulus <= 1:
    p.error("bits must be 1..24 and modulus must be greater than 1")
if math.gcd(a.x1 - a.x0, a.modulus) != 1:
    raise SystemExit("x1-x0 has no modular inverse for this modulus")

inverse = pow(a.x1 - a.x0, -1, a.modulus)
for low in range(1 << a.bits):
    x2 = (a.x2_top << a.bits) | low
    mult = ((x2 - a.x1) * inverse) % a.modulus
    inc = (a.x1 - mult * a.x0) % a.modulus
    if (mult * x2 + inc) % a.modulus == a.x3:
        print("lower =", low)
        print("x2 =", x2)
        print("a =", mult)
        print("c =", inc)
        break
else:
    raise SystemExit("no candidate matched x3")
