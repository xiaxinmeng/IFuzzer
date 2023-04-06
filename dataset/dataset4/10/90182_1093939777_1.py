from pathlib import Path
from zipfile import Path as ZipPath

for item in Path("logs").iterdir():
    if item.is_dir():
        path = next(item.iterdir())
        print(ZipPath(path).name)
