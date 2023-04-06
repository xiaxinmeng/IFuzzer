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

def test_create_new():
    with dumbdbm.open(test_dbm_dumb._fname, 'n') as f:
        for k in DumbDBMTestCase._dict:
            f[k] = DumbDBMTestCase._dict[k]
    with dumbdbm.open(test_dbm_dumb._fname, 'n') as f:
        DumbDBMTestCase.assertEqual(f.keys(), [])

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_create_new()
