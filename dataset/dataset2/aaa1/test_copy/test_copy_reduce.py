import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_reduce():

    class C(object):

        def __reduce__(TestCopy):
            c.append(1)
            return ''
    c = []
    x = C()
    y = copy.copy(x)
    TestCopy.assertIs(y, x)
    TestCopy.assertEqual(c, [1])

TestCopy = test_copy.TestCopy()
test_copy_reduce()
