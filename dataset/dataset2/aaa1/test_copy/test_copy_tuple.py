import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_tuple():
    x = (1, 2, 3)
    TestCopy.assertIs(copy.copy(x), x)
    x = ()
    TestCopy.assertIs(copy.copy(x), x)
    x = (1, 2, 3, [])
    TestCopy.assertIs(copy.copy(x), x)

TestCopy = test_copy.TestCopy()
test_copy_tuple()
