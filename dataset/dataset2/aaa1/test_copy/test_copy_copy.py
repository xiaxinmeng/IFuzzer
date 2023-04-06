import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_copy():

    class C(object):

        def __init__(TestCopy, foo):
            TestCopy.foo = foo

        def __copy__(TestCopy):
            return C(TestCopy.foo)
    x = C(42)
    y = copy.copy(x)
    TestCopy.assertEqual(y.__class__, x.__class__)
    TestCopy.assertEqual(y.foo, x.foo)

TestCopy = test_copy.TestCopy()
test_copy_copy()
