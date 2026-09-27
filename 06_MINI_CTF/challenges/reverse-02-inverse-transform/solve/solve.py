from pathlib import Path
import ast,re
txt=(Path(__file__).resolve().parents[1]/"challenge/checker.py").read_text()
values=ast.literal_eval(re.search(r'expected = (\[[^\n]+\])',txt).group(1))
print(''.join(chr(((v-9)&255)^0x35) for v in values))
