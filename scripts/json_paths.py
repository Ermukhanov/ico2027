#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args()
def w(x,path="$"):
 if isinstance(x,dict):
  for k,v in x.items():w(v,path+"."+str(k))
 elif isinstance(x,list):
  for i,v in enumerate(x):w(v,f"{path}[{i}]")
 else:print(path,"=",repr(x))
w(json.load(open(a.file)))
