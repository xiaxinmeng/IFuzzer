from pathlib import Path
while True:
    Path("foo").touch(); Path("foo").unlink()