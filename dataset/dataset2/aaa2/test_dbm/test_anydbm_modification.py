import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_anydbm_modification():
    AnyDBMTestCase.init_db()
    f = test_dbm.dbm.open(test_dbm._fname, 'c')
    AnyDBMTestCase._dict['g'] = f[b'g'] = b'indented'
    AnyDBMTestCase.read_helper(f)
    AnyDBMTestCase.assertEqual(f.setdefault(b'xxx', b'foo'), b'foo')
    AnyDBMTestCase.assertEqual(f[b'xxx'], b'foo')
    f.close()

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_anydbm_modification()
