
import dbm.gnu as dbm
db = dbm.open('x.db', 'nx')
db.gdbm_failure_atomic('even_snapshot.bin', 'odd_snapshot.bin')
for k, v in zip('abcdef', 'ghijkl'):
    db[k] = v
    db.sync()
db.close()
