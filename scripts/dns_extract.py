#!/usr/bin/env python3
import argparse
from scapy.all import rdpcap,DNS,DNSQR
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args()
for x in rdpcap(a.file):
 if DNS in x and x[DNS].qd and DNSQR in x: print(x[DNS].qd.qname.decode(errors="replace").rstrip("."))
