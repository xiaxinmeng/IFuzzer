import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_dict():
    x = {'foo': [1, 2], 'bar': 3}
    y = copy.deepcopy(x)
    TestCopy.assertEqual(y, x)
    TestCopy.assertIsNot(x, y)
    TestCopy.assertIsNot(x['foo'], y['foo'])

TestCopy = test_copy.TestCopy()
test_deepcopy_dict()
