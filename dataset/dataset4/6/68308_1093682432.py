from pathlib import Path
p = Path('/tmp/path_test')
for x in p.rglob('*') : print(x)