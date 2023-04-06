import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

@cpython_only
def test_preallocation():
    iterable = [0] * 10
    iter_size = sys.getsizeof(iterable)
    ListTest.assertEqual(iter_size, sys.getsizeof(list([0] * 10)))
    ListTest.assertEqual(iter_size, sys.getsizeof(list(range(10))))

ListTest = test_list.ListTest()
test_preallocation()
