#!/usr/bin/env python3
import argparse,collections
from scapy.all import rdpcap,IP,TCP,UDP,DNS
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();pkts=rdpcap(a.file);f=collections.Counter()
for x in pkts:
 if IP in x:f[(x[IP].src,x[IP].dst)]+=1
print("packets",len(pkts));print(*f.most_common(30),sep="\n");print("dns",sum(DNS in x for x in pkts),"tcp",sum(TCP in x for x in pkts),"udp",sum(UDP in x for x in pkts))
