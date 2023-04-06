import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_reconstruct_nostate():

    class C(object):

        def __reduce__(TestCopy):
            return (C, ())
    x = C()
    x.foo = 42
    y = copy.copy(x)
    TestCopy.assertIs(y.__class__, x.__class__)
    y = copy.deepcopy(x)
    TestCopy.assertIs(y.__class__, x.__class__)

TestCopy = test_copy.TestCopy()
test_reconstruct_nostate()
