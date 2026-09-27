#!/usr/bin/env python3
"""List PNG chunks and report their CRC validity."""
import argparse
import struct
import zlib

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("image")
a = p.parse_args()
with open(a.image, "rb") as f:
    if f.read(8) != PNG_SIGNATURE:
        raise SystemExit("not a PNG file")
    offset = 8
    while True:
        header = f.read(8)
        if not header:
            break
        if len(header) != 8:
            raise SystemExit(f"truncated chunk header at offset {offset}")
        length, kind = struct.unpack(">I4s", header)
        data = f.read(length)
        crc_bytes = f.read(4)
        if len(data) != length or len(crc_bytes) != 4:
            raise SystemExit(f"truncated {kind!r} chunk at offset {offset}")
        stored_crc, = struct.unpack(">I", crc_bytes)
        actual_crc = zlib.crc32(kind + data) & 0xFFFFFFFF
        name = kind.decode("ascii", "replace")
        print(f"{offset:>10}  {name:4s}  {length:>9} bytes  CRC {'OK' if stored_crc == actual_crc else 'BAD'}")
        offset += 12 + length
        if kind == b"IEND":
            trailing = f.read()
            if trailing:
                print("trailing bytes:", len(trailing))
            break
