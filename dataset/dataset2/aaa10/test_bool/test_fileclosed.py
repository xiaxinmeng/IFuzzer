import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_fileclosed():
    try:
        with open(os_helper.TESTFN, 'w') as f:
            BoolTest.assertIs(f.closed, False)
        BoolTest.assertIs(f.closed, True)
    finally:
        os.remove(os_helper.TESTFN)

BoolTest = test_bool.BoolTest()
test_fileclosed()
