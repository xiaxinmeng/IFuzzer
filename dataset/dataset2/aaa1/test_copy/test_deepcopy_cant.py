import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_cant():

    class C(object):

        def __getattribute__(TestCopy, name):
            if name.startswith('__reduce'):
                raise AttributeError(name)
            return object.__getattribute__(TestCopy, name)
    x = C()
    TestCopy.assertRaises(copy.Error, copy.deepcopy, x)

TestCopy = test_copy.TestCopy()
test_deepcopy_cant()
