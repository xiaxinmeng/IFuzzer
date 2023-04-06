from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_bytes():
    with dbm.ndbm.open(DbmTestCase.filename, 'c') as db:
        db[b'bytes key \xbd'] = b'bytes value \xbd'
    with dbm.ndbm.open(DbmTestCase.filename, 'r') as db:
        DbmTestCase.assertEqual(list(db.keys()), [b'bytes key \xbd'])
        DbmTestCase.assertTrue(b'bytes key \xbd' in db)
        DbmTestCase.assertEqual(db[b'bytes key \xbd'], b'bytes value \xbd')

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_bytes()
