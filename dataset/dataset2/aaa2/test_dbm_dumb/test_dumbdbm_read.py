import contextlib
import io
import operator
import os
import stat
import unittest
import dbm.dumb as dumbdbm
from test import support
from test.support import os_helper
from functools import partial
import stat
import random
import test_dbm_dumb

def test_dumbdbm_read():
    DumbDBMTestCase.init_db()
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname, 'r')) as f:
        DumbDBMTestCase.read_helper(f)
        with DumbDBMTestCase.assertRaisesRegex(dumbdbm.error, 'The database is opened for reading only'):
            f[b'g'] = b'x'
        with DumbDBMTestCase.assertRaisesRegex(dumbdbm.error, 'The database is opened for reading only'):
            del f[b'a']
        DumbDBMTestCase.assertEqual(f.get(b'a'), DumbDBMTestCase._dict[b'a'])
        DumbDBMTestCase.assertEqual(f.get(b'xxx', b'foo'), b'foo')
        DumbDBMTestCase.assertIsNone(f.get(b'xxx'))
        with DumbDBMTestCase.assertRaises(KeyError):
            f[b'xxx']

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_dumbdbm_read()
