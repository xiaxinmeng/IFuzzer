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

def test_dumbdbm_creation():
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname, 'c')) as f:
        DumbDBMTestCase.assertEqual(list(f.keys()), [])
        for key in DumbDBMTestCase._dict:
            f[key] = DumbDBMTestCase._dict[key]
        DumbDBMTestCase.read_helper(f)

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_dumbdbm_creation()
