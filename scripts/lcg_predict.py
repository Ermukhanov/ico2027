#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser();p.add_argument("x",type=int);p.add_argument("a",type=int);p.add_argument("c",type=int);p.add_argument("-m",type=int,default=2**32);p.add_argument("-n",type=int,default=10);q=p.parse_args()
for i in range(q.n):q.x=(q.a*q.x+q.c)%q.m;print(i+1,q.x)
