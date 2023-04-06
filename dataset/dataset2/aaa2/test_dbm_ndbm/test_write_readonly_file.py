from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_write_readonly_file():
    with dbm.ndbm.open(DbmTestCase.filename, 'c') as db:
        db[b'bytes key'] = b'bytes value'
    with dbm.ndbm.open(DbmTestCase.filename, 'r') as db:
        with DbmTestCase.assertRaises(error):
            del db[b'not exist key']
        with DbmTestCase.assertRaises(error):
            del db[b'bytes key']
        with DbmTestCase.assertRaises(error):
            db[b'not exist key'] = b'not exist value'

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_write_readonly_file()
