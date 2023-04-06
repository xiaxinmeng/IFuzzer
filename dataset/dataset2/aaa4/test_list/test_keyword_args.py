import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_keyword_args():
    with ListTest.assertRaisesRegex(TypeError, 'keyword argument'):
        list(sequence=[])

ListTest = test_list.ListTest()
test_keyword_args()
