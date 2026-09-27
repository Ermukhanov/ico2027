from pathlib import Path
import base64,re
s=(Path(__file__).resolve().parents[1]/"challenge/access.log").read_text()
v=re.search(r"data=([A-Za-z0-9+/=]+)",s).group(1)
print(base64.b64decode(v).decode())
