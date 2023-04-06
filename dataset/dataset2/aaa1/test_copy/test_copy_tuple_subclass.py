import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_tuple_subclass():

    class C(tuple):
        pass
    x = C([1, 2, 3])
    TestCopy.assertEqual(tuple(x), (1, 2, 3))
    y = copy.copy(x)
    TestCopy.assertEqual(tuple(y), (1, 2, 3))

TestCopy = test_copy.TestCopy()
test_copy_tuple_subclass()
