#!/usr/bin/env python3
"""Show the least-significant-bit stream for each RGB image channel."""
import argparse

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("image")
p.add_argument("--pixels", type=int, default=4096, help="maximum pixels to inspect")
p.add_argument("--channel", choices=("R", "G", "B", "all"), default="all")
a = p.parse_args()
if a.pixels < 1:
    p.error("pixels must be positive")
try:
    from PIL import Image
except ImportError as e:
    raise SystemExit("Pillow is required: install the 'Pillow' requirement") from e

with Image.open(a.image) as source:
    image = source.convert("RGB")
    width, height = image.size
    pixels = [image.getpixel((i % width, i // width))
              for i in range(min(a.pixels, width * height))]
    print("size:", image.size, "pixels inspected:", len(pixels))
    channels = {"R": 0, "G": 1, "B": 2}
    selected = channels if a.channel == "all" else {a.channel: channels[a.channel]}
    for name, index in selected.items():
        bits = "".join(str(pixel[index] & 1) for pixel in pixels)
        usable = bits[: len(bits) // 8 * 8]
        data = bytes(int(usable[i:i + 8], 2) for i in range(0, len(usable), 8))
        print(f"{name} LSB bits:", bits[:256])
        print(f"{name} bytes:", repr(data[:128]))
