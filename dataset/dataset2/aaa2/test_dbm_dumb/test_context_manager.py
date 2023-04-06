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

def test_context_manager():
    with dumbdbm.open(test_dbm_dumb._fname, 'c') as db:
        db['dumbdbm context manager'] = 'context manager'
    with dumbdbm.open(test_dbm_dumb._fname, 'r') as db:
        DumbDBMTestCase.assertEqual(list(db.keys()), [b'dumbdbm context manager'])
    with DumbDBMTestCase.assertRaises(dumbdbm.error):
        db.keys()

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_context_manager()
