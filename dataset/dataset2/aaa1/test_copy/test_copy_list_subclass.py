import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_list_subclass():

    class C(list):
        pass
    x = C([[1, 2], 3])
    x.foo = [4, 5]
    y = copy.copy(x)
    TestCopy.assertEqual(list(x), list(y))
    TestCopy.assertEqual(x.foo, y.foo)
    TestCopy.assertIs(x[0], y[0])
    TestCopy.assertIs(x.foo, y.foo)

TestCopy = test_copy.TestCopy()
test_copy_list_subclass()
