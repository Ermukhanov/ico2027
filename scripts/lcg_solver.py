#!/usr/bin/env python3
import argparse,math
p=argparse.ArgumentParser();p.add_argument("x0",type=int);p.add_argument("x1",type=int);p.add_argument("x2",type=int);p.add_argument("--m",type=int,default=2**32);a=p.parse_args();d=a.x1-a.x0
if math.gcd(d,a.m)!=1:raise SystemExit("x1-x0 is not invertible")
A=((a.x2-a.x1)*pow(d,-1,a.m))%a.m;C=(a.x1-A*a.x0)%a.m;print("a=",A);print("c=",C)
