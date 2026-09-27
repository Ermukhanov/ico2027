from pathlib import Path
s=Path(__file__).resolve().parents[1]/"challenge/checker.py"
import re
txt=s.read_text(); data=bytes.fromhex(re.search(r'fromhex\("([0-9a-f]+)"',txt).group(1)); key=int(re.search(r'key = 0x([0-9a-f]+)',txt).group(1),16)
print(bytes(x^key for x in data).decode())
