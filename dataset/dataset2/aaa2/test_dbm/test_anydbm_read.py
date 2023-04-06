import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_anydbm_read():
    AnyDBMTestCase.init_db()
    f = test_dbm.dbm.open(test_dbm._fname, 'r')
    AnyDBMTestCase.read_helper(f)
    AnyDBMTestCase.assertEqual(f.get(b'a'), AnyDBMTestCase._dict['a'])
    AnyDBMTestCase.assertEqual(f.get(b'xxx', b'foo'), b'foo')
    AnyDBMTestCase.assertIsNone(f.get(b'xxx'))
    with AnyDBMTestCase.assertRaises(KeyError):
        f[b'xxx']
    f.close()

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_anydbm_read()
