from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_keys():
    DbmTestCase.d = dbm.ndbm.open(DbmTestCase.filename, 'c')
    DbmTestCase.assertEqual(DbmTestCase.d.keys(), [])
    DbmTestCase.d['a'] = 'b'
    DbmTestCase.d[b'bytes'] = b'data'
    DbmTestCase.d['12345678910'] = '019237410982340912840198242'
    DbmTestCase.d.keys()
    DbmTestCase.assertIn('a', DbmTestCase.d)
    DbmTestCase.assertIn(b'a', DbmTestCase.d)
    DbmTestCase.assertEqual(DbmTestCase.d[b'bytes'], b'data')
    DbmTestCase.assertEqual(DbmTestCase.d.get(b'a'), b'b')
    DbmTestCase.assertIsNone(DbmTestCase.d.get(b'xxx'))
    DbmTestCase.assertEqual(DbmTestCase.d.get(b'xxx', b'foo'), b'foo')
    with DbmTestCase.assertRaises(KeyError):
        DbmTestCase.d['xxx']
    DbmTestCase.assertEqual(DbmTestCase.d.setdefault(b'xxx', b'foo'), b'foo')
    DbmTestCase.assertEqual(DbmTestCase.d[b'xxx'], b'foo')
    DbmTestCase.d.close()

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_keys()
