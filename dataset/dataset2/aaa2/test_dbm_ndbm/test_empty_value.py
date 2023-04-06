from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_empty_value():
    if dbm.ndbm.library == 'Berkeley DB':
        DbmTestCase.skipTest("Berkeley DB doesn't distinguish the empty value from the absent one")
    DbmTestCase.d = dbm.ndbm.open(DbmTestCase.filename, 'c')
    DbmTestCase.assertEqual(DbmTestCase.d.keys(), [])
    DbmTestCase.d['empty'] = ''
    DbmTestCase.assertEqual(DbmTestCase.d.keys(), [b'empty'])
    DbmTestCase.assertIn(b'empty', DbmTestCase.d)
    DbmTestCase.assertEqual(DbmTestCase.d[b'empty'], b'')
    DbmTestCase.assertEqual(DbmTestCase.d.get(b'empty'), b'')
    DbmTestCase.assertEqual(DbmTestCase.d.setdefault(b'empty'), b'')
    DbmTestCase.d.close()

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_empty_value()
