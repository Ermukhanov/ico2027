from pathlib import Path
import subprocess
binpath=Path(__file__).resolve().parents[1]/"challenge/chall"
print(subprocess.check_output([str(binpath)],input=b"256\n").decode(),end="")
