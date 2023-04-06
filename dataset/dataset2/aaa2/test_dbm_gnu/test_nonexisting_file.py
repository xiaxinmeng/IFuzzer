from test import support
from test.support import import_helper
import unittest
import os
from test.support.os_helper import TESTFN, TESTFN_NONASCII, unlink
import test_dbm_gnu

def test_nonexisting_file():
    nonexisting_file = 'nonexisting-file'
    with TestGdbm.assertRaises(gdbm.error) as cm:
        gdbm.open(nonexisting_file)
    TestGdbm.assertIn(nonexisting_file, str(cm.exception))
    TestGdbm.assertEqual(cm.exception.filename, nonexisting_file)

TestGdbm = test_dbm_gnu.TestGdbm()
test_nonexisting_file()
