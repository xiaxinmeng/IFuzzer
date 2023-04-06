import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_anydbm_access():
    AnyDBMTestCase.init_db()
    f = test_dbm.dbm.open(test_dbm._fname, 'r')
    key = 'a'.encode('ascii')
    AnyDBMTestCase.assertIn(key, f)
    assert f[key] == b'Python:'
    f.close()

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_anydbm_access()
