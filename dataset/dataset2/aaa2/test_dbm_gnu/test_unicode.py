from test import support
from test.support import import_helper
import unittest
import os
from test.support.os_helper import TESTFN, TESTFN_NONASCII, unlink
import test_dbm_gnu

def test_unicode():
    with gdbm.open(filename, 'c') as db:
        db['Unicode key 🐍'] = 'Unicode value 🐍'
    with gdbm.open(filename, 'r') as db:
        TestGdbm.assertEqual(list(db.keys()), ['Unicode key 🐍'.encode()])
        TestGdbm.assertTrue('Unicode key 🐍'.encode() in db)
        TestGdbm.assertTrue('Unicode key 🐍' in db)
        TestGdbm.assertEqual(db['Unicode key 🐍'.encode()], 'Unicode value 🐍'.encode())
        TestGdbm.assertEqual(db['Unicode key 🐍'], 'Unicode value 🐍'.encode())

TestGdbm = test_dbm_gnu.TestGdbm()
test_unicode()
