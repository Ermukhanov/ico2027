#!/usr/bin/env python3
"""Factor a small RSA modulus and decrypt one ciphertext integer."""
import argparse
import math

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("n", type=int)
p.add_argument("e", type=int)
p.add_argument("c", type=int, help="ciphertext integer")
a = p.parse_args()
if a.n <= 1 or a.e <= 0 or not 0 <= a.c < a.n:
    p.error("require n > 1, e > 0, and 0 <= c < n")
if a.n > 10**12:
    raise SystemExit("this helper is for small practice moduli only (n <= 10^12)")
p_factor = next((d for d in range(2, math.isqrt(a.n) + 1) if a.n % d == 0), None)
if p_factor is None:
    raise SystemExit("n is prime or was not factorable by trial division")
q_factor = a.n // p_factor
phi = (p_factor - 1) * (q_factor - 1)
if math.gcd(a.e, phi) != 1:
    raise SystemExit("e has no inverse modulo phi(n)")
d = pow(a.e, -1, phi)
message = pow(a.c, d, a.n)
length = max(1, (message.bit_length() + 7) // 8)
raw = message.to_bytes(length, "big")
print("p =", p_factor)
print("q =", q_factor)
print("phi(n) =", phi)
print("d =", d)
print("message integer =", message)
print("message bytes =", repr(raw))
