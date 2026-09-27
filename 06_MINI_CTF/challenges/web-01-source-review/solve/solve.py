from pathlib import Path
import re
s=(Path(__file__).resolve().parents[1]/"challenge/page.html").read_text()
print(re.search(r'ICO\{[^}]+\}',s).group())
