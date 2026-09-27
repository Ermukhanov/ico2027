from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1]/"challenge/queries.pcap"
raw=subprocess.check_output(["tshark","-r",str(p),"-Y","dns","-T","fields","-e","dns.qry.name"],text=True)
parts=[line.split(".",1)[0] for line in raw.splitlines() if line]
print(bytes.fromhex("".join(parts)).decode())
