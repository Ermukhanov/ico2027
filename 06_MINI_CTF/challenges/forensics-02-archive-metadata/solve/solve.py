from pathlib import Path
import zipfile,base64
p=Path(__file__).resolve().parents[1]/"challenge/evidence.zip"
with zipfile.ZipFile(p) as z:
 comment=z.comment.decode(); print(base64.b64decode(comment.split(":",1)[1]).decode())
