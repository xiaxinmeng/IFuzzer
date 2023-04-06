import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_empty_tuple():
    x = ()
    y = copy.deepcopy(x)
    TestCopy.assertIs(x, y)

TestCopy = test_copy.TestCopy()
test_deepcopy_empty_tuple()
