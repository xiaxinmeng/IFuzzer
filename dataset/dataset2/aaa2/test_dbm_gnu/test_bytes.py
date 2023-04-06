from test import support
from test.support import import_helper
import unittest
import os
from test.support.os_helper import TESTFN, TESTFN_NONASCII, unlink
import test_dbm_gnu

def test_bytes():
    with gdbm.open(filename, 'c') as db:
        db[b'bytes key \xbd'] = b'bytes value \xbd'
    with gdbm.open(filename, 'r') as db:
        TestGdbm.assertEqual(list(db.keys()), [b'bytes key \xbd'])
        TestGdbm.assertTrue(b'bytes key \xbd' in db)
        TestGdbm.assertEqual(db[b'bytes key \xbd'], b'bytes value \xbd')

TestGdbm = test_dbm_gnu.TestGdbm()
test_bytes()
