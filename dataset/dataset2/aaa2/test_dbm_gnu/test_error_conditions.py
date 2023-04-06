from test import support
from test.support import import_helper
import unittest
import os
from test.support.os_helper import TESTFN, TESTFN_NONASCII, unlink
import test_dbm_gnu

def test_error_conditions():
    unlink(filename)
    TestGdbm.assertRaises(gdbm.error, gdbm.open, filename, 'r')
    TestGdbm.g = gdbm.open(filename, 'c')
    TestGdbm.g.close()
    TestGdbm.assertRaises(gdbm.error, lambda : TestGdbm.g['a'])
    TestGdbm.assertRaises(gdbm.error, lambda : gdbm.open(filename, 'rx').close())

TestGdbm = test_dbm_gnu.TestGdbm()
test_error_conditions()
