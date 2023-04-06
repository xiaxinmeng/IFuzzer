import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_truth():
    super().test_truth()
    ListTest.assertTrue(not [])
    ListTest.assertTrue([42])

ListTest = test_list.ListTest()
test_truth()
