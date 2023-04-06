import _gdbm
import sys
from pathlib import Path

print(sys.version)
path = '/tmp/tmp.db'

db = _gdbm.open(path, 'c')
print("Opened with string path")
db.close()

db = _gdbm.open(Path(path), 'c')
print("Opened with path-like")
db.close()