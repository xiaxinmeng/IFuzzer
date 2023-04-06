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

def test_write_contains():
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname)) as f:
        f[b'1'] = b'hello'
        DumbDBMTestCase.assertIn(b'1', f)

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_write_contains()
