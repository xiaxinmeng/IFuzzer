import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_anydbm_creation_n_file_exists_with_invalid_contents():
    os_helper.create_empty_file(test_dbm._fname)
    with test_dbm.dbm.open(test_dbm._fname, 'n') as f:
        AnyDBMTestCase.assertEqual(len(f), 0)

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_anydbm_creation_n_file_exists_with_invalid_contents()
