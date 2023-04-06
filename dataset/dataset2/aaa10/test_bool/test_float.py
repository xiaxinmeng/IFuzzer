import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_float():
    BoolTest.assertEqual(float(False), 0.0)
    BoolTest.assertIsNot(float(False), False)
    BoolTest.assertEqual(float(True), 1.0)
    BoolTest.assertIsNot(float(True), True)

BoolTest = test_bool.BoolTest()
test_float()
