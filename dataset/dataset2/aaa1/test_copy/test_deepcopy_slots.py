import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_slots():

    class C(object):
        __slots__ = ['foo']
    x = C()
    x.foo = [42]
    y = copy.deepcopy(x)
    TestCopy.assertEqual(x.foo, y.foo)
    TestCopy.assertIsNot(x.foo, y.foo)

TestCopy = test_copy.TestCopy()
test_deepcopy_slots()
