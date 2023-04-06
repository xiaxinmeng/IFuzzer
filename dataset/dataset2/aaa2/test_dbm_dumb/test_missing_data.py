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

def test_missing_data():
    for value in ('r', 'w'):
        test_dbm_dumb._delete_files()
        with DumbDBMTestCase.assertRaises(FileNotFoundError):
            dumbdbm.open(test_dbm_dumb._fname, value)
        DumbDBMTestCase.assertFalse(os.path.exists(test_dbm_dumb._fname + '.dir'))
        DumbDBMTestCase.assertFalse(os.path.exists(test_dbm_dumb._fname + '.bak'))

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_missing_data()
