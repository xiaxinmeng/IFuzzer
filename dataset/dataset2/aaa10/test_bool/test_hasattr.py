import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_hasattr():
    BoolTest.assertIs(hasattr([], 'append'), True)
    BoolTest.assertIs(hasattr([], 'wobble'), False)

BoolTest = test_bool.BoolTest()
test_hasattr()
