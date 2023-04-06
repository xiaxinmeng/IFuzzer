import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_inst_deepcopy():

    class C:

        def __init__(TestCopy, foo):
            TestCopy.foo = foo

        def __deepcopy__(TestCopy, memo):
            return C(copy.deepcopy(TestCopy.foo, memo))

        def __eq__(TestCopy, other):
            return TestCopy.foo == other.foo
    x = C([42])
    y = copy.deepcopy(x)
    TestCopy.assertEqual(y, x)
    TestCopy.assertIsNot(y, x)
    TestCopy.assertIsNot(y.foo, x.foo)

TestCopy = test_copy.TestCopy()
test_deepcopy_inst_deepcopy()
