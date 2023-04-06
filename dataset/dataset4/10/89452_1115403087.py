import dbm.ndbm
from pathlib import Path

db_path = Path("/tmp/test.dbm")
db_path.unlink(missing_ok=True)
f = dbm.ndbm.open(db_path, 'c')
print("Underlying lib:", dbm.ndbm.library)
print("f is an", repr(f))
print("The next line segfaults:")
f.keys()