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

def test_eval():
    with open(test_dbm_dumb._fname + '.dir', 'w') as stream:
        stream.write("str(print('Hacked!')), 0\n")
    with support.captured_stdout() as stdout:
        with DumbDBMTestCase.assertRaises(ValueError):
            with dumbdbm.open(test_dbm_dumb._fname) as f:
                pass
        DumbDBMTestCase.assertEqual(stdout.getvalue(), '')

DumbDBMTestCase = test_dbm_dumb.DumbDBMTestCase()
test_eval()
