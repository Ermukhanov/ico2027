#!/usr/bin/env python3
import argparse,subprocess
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args()
r=subprocess.run([a.file],input=b"test\n",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=3)
print(r.stdout.decode("utf-8","replace"))
