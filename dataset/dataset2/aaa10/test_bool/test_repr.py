import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_repr():
    BoolTest.assertEqual(repr(False), 'False')
    BoolTest.assertEqual(repr(True), 'True')
    BoolTest.assertIs(eval(repr(False)), False)
    BoolTest.assertIs(eval(repr(True)), True)

BoolTest = test_bool.BoolTest()
test_repr()
