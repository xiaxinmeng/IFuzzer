import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_identity():
    ListTest.assertTrue([] is not [])

ListTest = test_list.ListTest()
test_identity()
