from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_context_manager():
    with dbm.ndbm.open(DbmTestCase.filename, 'c') as db:
        db['ndbm context manager'] = 'context manager'
    with dbm.ndbm.open(DbmTestCase.filename, 'r') as db:
        DbmTestCase.assertEqual(list(db.keys()), [b'ndbm context manager'])
    with DbmTestCase.assertRaises(dbm.ndbm.error) as cm:
        db.keys()
    DbmTestCase.assertEqual(str(cm.exception), 'DBM object has already been closed')

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_context_manager()
