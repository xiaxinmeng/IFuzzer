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

def test_invalid_flag():
    for flag in ('x', 'rf', None):
        with DumbDBMTestCase.assertRaisesRegex(ValueError, "Flag must be one of 'r', 'w', 'c', or 'n'"):
            dumbdbm.open(test_dbm_dumb._fname, flag)

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_invalid_flag()
