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

def test_str_write_contains():
    DumbDBMTestCase.init_db()
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname)) as f:
        f['ü'] = b'!'
        f['1'] = 'a'
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname, 'r')) as f:
        DumbDBMTestCase.assertIn('ü', f)
        DumbDBMTestCase.assertEqual(f['ü'.encode('utf-8')], DumbDBMTestCase._dict['ü'.encode('utf-8')])
        DumbDBMTestCase.assertEqual(f[b'1'], b'a')

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_str_write_contains()
