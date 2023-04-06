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

def test_dumbdbm_keys():
    DumbDBMTestCase.init_db()
    with contextlib.closing(dumbdbm.open(test_dbm_dumb._fname)) as f:
        keys = DumbDBMTestCase.keys_helper(f)

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_dumbdbm_keys()
