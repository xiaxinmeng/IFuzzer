import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_marshal():
    import marshal
    BoolTest.assertIs(marshal.loads(marshal.dumps(True)), True)
    BoolTest.assertIs(marshal.loads(marshal.dumps(False)), False)

BoolTest = test_bool.BoolTest()
test_marshal()
