#!/usr/bin/env python3
import argparse,base64,urllib.parse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("file");a=p.parse_args();s=Path(a.file).read_text(errors="replace").strip();print("url",urllib.parse.unquote(s))
for n,f in (("b16",base64.b16decode),("b32",base64.b32decode),("b64",base64.b64decode),("b85",base64.b85decode)):
 try: print(n,f(s,casefold=True))
 except Exception: print(n,"FAIL")
