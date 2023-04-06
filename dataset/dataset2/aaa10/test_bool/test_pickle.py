import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_pickle():
    import pickle
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        BoolTest.assertIs(pickle.loads(pickle.dumps(True, proto)), True)
        BoolTest.assertIs(pickle.loads(pickle.dumps(False, proto)), False)

BoolTest = test_bool.BoolTest()
test_pickle()
