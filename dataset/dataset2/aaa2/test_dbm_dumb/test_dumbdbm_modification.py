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

def test_dumbdbm_modification():
    DumbDBMTestCase.init_db()
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname, 'w')) as f:
        DumbDBMTestCase._dict[b'g'] = f[b'g'] = b'indented'
        DumbDBMTestCase.read_helper(f)
        DumbDBMTestCase.assertEqual(f.setdefault(b'xxx', b'foo'), b'foo')
        DumbDBMTestCase.assertEqual(f[b'xxx'], b'foo')

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_dumbdbm_modification()
