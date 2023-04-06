import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_empty_value():
    if getattr(test_dbm.dbm._defaultmod, 'library', None) == 'Berkeley DB':
        AnyDBMTestCase.skipTest("Berkeley DB doesn't distinguish the empty value from the absent one")
    f = test_dbm.dbm.open(test_dbm._fname, 'c')
    AnyDBMTestCase.assertEqual(f.keys(), [])
    f[b'empty'] = b''
    AnyDBMTestCase.assertEqual(f.keys(), [b'empty'])
    AnyDBMTestCase.assertIn(b'empty', f)
    AnyDBMTestCase.assertEqual(f[b'empty'], b'')
    AnyDBMTestCase.assertEqual(f.get(b'empty'), b'')
    AnyDBMTestCase.assertEqual(f.setdefault(b'empty'), b'')
    f.close()

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_empty_value()
