import fileinput
from pathlib import Path
path = Path(252 * "x")
path.write_text("")
for line in fileinput.input(path, inplace=True):
    pass