#!/usr/bin/env python3
import argparse
from bs4 import BeautifulSoup
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args()
s=BeautifulSoup(open(a.file,encoding="utf-8",errors="replace"),"html.parser")
for f in s.find_all("form"):
 print("FORM",f.get("method"),f.get("action"))
 for i in f.find_all(["input","textarea","select"]): print(" ",i.name,i.get("name"),i.get("type"))
