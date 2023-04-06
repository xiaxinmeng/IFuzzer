from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_nonexisting_file():
    nonexisting_file = 'nonexisting-file'
    with DbmTestCase.assertRaises(dbm.ndbm.error) as cm:
        dbm.ndbm.open(nonexisting_file)
    DbmTestCase.assertIn(nonexisting_file, str(cm.exception))
    DbmTestCase.assertEqual(cm.exception.filename, nonexisting_file)

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_nonexisting_file()
