from test import support
from test.support import import_helper
import unittest
import os
from test.support.os_helper import TESTFN, TESTFN_NONASCII, unlink
import test_dbm_gnu

def test_write_readonly_file():
    with gdbm.open(filename, 'c') as db:
        db[b'bytes key'] = b'bytes value'
    with gdbm.open(filename, 'r') as db:
        with TestGdbm.assertRaises(gdbm.error):
            del db[b'not exist key']
        with TestGdbm.assertRaises(gdbm.error):
            del db[b'bytes key']
        with TestGdbm.assertRaises(gdbm.error):
            db[b'not exist key'] = b'not exist value'

TestGdbm = test_dbm_gnu.TestGdbm()
test_write_readonly_file()
