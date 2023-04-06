import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_convert():
    BoolTest.assertRaises(TypeError, bool, 42, 42)
    BoolTest.assertIs(bool(10), True)
    BoolTest.assertIs(bool(1), True)
    BoolTest.assertIs(bool(-1), True)
    BoolTest.assertIs(bool(0), False)
    BoolTest.assertIs(bool('hello'), True)
    BoolTest.assertIs(bool(''), False)
    BoolTest.assertIs(bool(), False)

BoolTest = test_bool.BoolTest()
test_convert()
