import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_basic():
    x = 42
    y = copy.copy(x)
    TestCopy.assertEqual(x, y)

TestCopy = test_copy.TestCopy()
test_copy_basic()
