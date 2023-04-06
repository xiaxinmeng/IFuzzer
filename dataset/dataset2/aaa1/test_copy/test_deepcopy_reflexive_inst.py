import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_reflexive_inst():

    class C:
        pass
    x = C()
    x.foo = x
    y = copy.deepcopy(x)
    TestCopy.assertIsNot(y, x)
    TestCopy.assertIs(y.foo, y)

TestCopy = test_copy.TestCopy()
test_deepcopy_reflexive_inst()
