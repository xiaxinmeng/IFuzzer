import dbm.gnu
from pathlib import Path

db_path = Path("/tmp/test.dbm")
db_path.unlink(missing_ok=True)
f = dbm.gnu.open(db_path, 'c')
print("f is an", repr(f))
print("The next line runs fine:")
f.keys()