import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_step_overflow():
    a = [0, 1, 2, 3, 4]
    a[1::sys.maxsize] = [0]
    ListTest.assertEqual(a[3::sys.maxsize], [3])

ListTest = test_list.ListTest()
test_step_overflow()
