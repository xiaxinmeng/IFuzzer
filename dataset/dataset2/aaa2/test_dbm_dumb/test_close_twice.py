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

def test_close_twice():
    f = dumbdbm.open(test_dbm_dumb._fname)
    f[b'a'] = b'b'
    DumbDBMTestCase.assertEqual(f[b'a'], b'b')
    f.close()
    f.close()

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_close_twice()
