import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_len():
    super().test_len()
    ListTest.assertEqual(len([]), 0)
    ListTest.assertEqual(len([0]), 1)
    ListTest.assertEqual(len([0, 1, 2]), 3)

ListTest = test_list.ListTest()
test_len()
