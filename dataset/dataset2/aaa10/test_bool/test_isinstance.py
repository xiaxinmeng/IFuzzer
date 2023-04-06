import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_isinstance():
    BoolTest.assertIs(isinstance(True, bool), True)
    BoolTest.assertIs(isinstance(False, bool), True)
    BoolTest.assertIs(isinstance(True, int), True)
    BoolTest.assertIs(isinstance(False, int), True)
    BoolTest.assertIs(isinstance(1, bool), False)
    BoolTest.assertIs(isinstance(0, bool), False)

BoolTest = test_bool.BoolTest()
test_isinstance()
