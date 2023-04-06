import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_real_and_imag():
    BoolTest.assertEqual(True .real, 1)
    BoolTest.assertEqual(True .imag, 0)
    BoolTest.assertIs(type(True .real), int)
    BoolTest.assertIs(type(True .imag), int)
    BoolTest.assertEqual(False .real, 0)
    BoolTest.assertEqual(False .imag, 0)
    BoolTest.assertIs(type(False .real), int)
    BoolTest.assertIs(type(False .imag), int)

BoolTest = test_bool.BoolTest()
test_real_and_imag()
