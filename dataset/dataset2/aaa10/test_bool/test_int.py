import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_int():
    BoolTest.assertEqual(int(False), 0)
    BoolTest.assertIsNot(int(False), False)
    BoolTest.assertEqual(int(True), 1)
    BoolTest.assertIsNot(int(True), True)

BoolTest = test_bool.BoolTest()
test_int()
