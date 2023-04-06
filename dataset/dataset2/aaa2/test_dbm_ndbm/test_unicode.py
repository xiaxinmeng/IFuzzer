from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_unicode():
    with dbm.ndbm.open(DbmTestCase.filename, 'c') as db:
        db['Unicode key 🐍'] = 'Unicode value 🐍'
    with dbm.ndbm.open(DbmTestCase.filename, 'r') as db:
        DbmTestCase.assertEqual(list(db.keys()), ['Unicode key 🐍'.encode()])
        DbmTestCase.assertTrue('Unicode key 🐍'.encode() in db)
        DbmTestCase.assertTrue('Unicode key 🐍' in db)
        DbmTestCase.assertEqual(db['Unicode key 🐍'.encode()], 'Unicode value 🐍'.encode())
        DbmTestCase.assertEqual(db['Unicode key 🐍'], 'Unicode value 🐍'.encode())

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_unicode()
