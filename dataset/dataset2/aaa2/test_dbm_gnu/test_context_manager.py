from test import support
from test.support import import_helper
import unittest
import os
from test.support.os_helper import TESTFN, TESTFN_NONASCII, unlink
import test_dbm_gnu

def test_context_manager():
    with gdbm.open(filename, 'c') as db:
        db['gdbm context manager'] = 'context manager'
    with gdbm.open(filename, 'r') as db:
        TestGdbm.assertEqual(list(db.keys()), [b'gdbm context manager'])
    with TestGdbm.assertRaises(gdbm.error) as cm:
        db.keys()
    TestGdbm.assertEqual(str(cm.exception), 'GDBM object has already been closed')

TestGdbm = test_dbm_gnu.TestGdbm()
test_context_manager()
