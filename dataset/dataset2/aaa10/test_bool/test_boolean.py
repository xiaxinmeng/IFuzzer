import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_boolean():
    BoolTest.assertEqual(True & 1, 1)
    BoolTest.assertNotIsInstance(True & 1, bool)
    BoolTest.assertIs(True & True, True)
    BoolTest.assertEqual(True | 1, 1)
    BoolTest.assertNotIsInstance(True | 1, bool)
    BoolTest.assertIs(True | True, True)
    BoolTest.assertEqual(True ^ 1, 0)
    BoolTest.assertNotIsInstance(True ^ 1, bool)
    BoolTest.assertIs(True ^ True, False)

BoolTest = test_bool.BoolTest()
test_boolean()
