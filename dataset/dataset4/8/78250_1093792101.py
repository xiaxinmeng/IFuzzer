from shutil import move
from pathlib import Path

a = Path("s")
b = Path("a.txt")

move(b, a)