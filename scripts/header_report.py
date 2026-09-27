#!/usr/bin/env python3
import argparse,requests
p=argparse.ArgumentParser();p.add_argument("url");a=p.parse_args()
r=requests.get(a.url,verify=False,timeout=10);print(r.status_code,r.url)
for k,v in r.headers.items(): print(k+":",v)
