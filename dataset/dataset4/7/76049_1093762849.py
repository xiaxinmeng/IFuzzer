
import dbm.ndbm

with dbm.ndbm.open('db', 'n') as db:
    print(db.get('missing-key'))
