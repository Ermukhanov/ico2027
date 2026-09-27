from pathlib import Path
import base64
p=Path(__file__).resolve().parents[1]/"challenge/message.txt"
print(base64.b64decode(p.read_text().strip()).decode())
