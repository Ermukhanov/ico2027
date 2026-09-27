#!/usr/bin/env python3
"""List DNS questions in a PCAP and try common decoders on joined labels."""
import argparse
import base64
import binascii
import codecs
import re
from urllib.parse import unquote

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("file", help="PCAP/PCAPNG file")
a = p.parse_args()
try:
    from scapy.all import DNS, DNSQR, rdpcap
except ImportError as e:
    raise SystemExit("Scapy is required: install the 'scapy' requirement") from e

names = []
for packet in rdpcap(a.file):
    if DNS in packet and packet[DNS].qd and DNSQR in packet:
        name = packet[DNS].qd.qname.decode("ascii", "replace").rstrip(".")
        if name:
            names.append(name)
for name in names:
    print(name)

if not names:
    raise SystemExit("no DNS questions found")
unique = list(dict.fromkeys(names))
labels = [part for name in unique for part in name.split(".")]
candidates = {
    "joined labels": "".join(labels),
    "joined first labels": "".join(name.split(".")[0] for name in unique),
}
for title, value in candidates.items():
    compact = re.sub(r"[^A-Za-z0-9+/=_-]", "", value)
    if compact:
        print(f"\n[{title}] {compact}")
        print("rot13:", codecs.decode(compact, "rot_13"))
        for label, decoder in (
            ("hex", bytes.fromhex),
            ("base32", base64.b32decode),
            ("base64", base64.b64decode),
            ("base85", base64.b85decode),
        ):
            try:
                decoded = decoder(compact.upper() if label == "base32" else compact)
                print(f"{label}:", repr(decoded))
            except (ValueError, binascii.Error):
                pass
        decoded_url = unquote(value)
        if decoded_url != value:
            print("URL:", decoded_url)
