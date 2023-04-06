import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_reduce_ex():

    class C(object):

        def __reduce_ex__(TestCopy, proto):
            c.append(1)
            return ''

        def __reduce__(TestCopy):
            TestCopy.fail("shouldn't call this")
    c = []
    x = C()
    y = copy.deepcopy(x)
    TestCopy.assertIs(y, x)
    TestCopy.assertEqual(c, [1])

TestCopy = test_copy.TestCopy()
test_deepcopy_reduce_ex()
