import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_anydbm_keys():
    AnyDBMTestCase.init_db()
    f = test_dbm.dbm.open(test_dbm._fname, 'r')
    keys = AnyDBMTestCase.keys_helper(f)
    f.close()

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_anydbm_keys()
