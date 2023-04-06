import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_anydbm_not_existing():
    AnyDBMTestCase.assertRaises(test_dbm.dbm.error, test_dbm.dbm.open, test_dbm._fname)

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_anydbm_not_existing()
