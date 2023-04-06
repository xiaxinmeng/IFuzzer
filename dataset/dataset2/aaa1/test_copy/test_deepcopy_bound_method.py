import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_bound_method():

    class Foo(object):

        def m(TestCopy):
            pass
    f = Foo()
    f.b = f.m
    g = copy.deepcopy(f)
    TestCopy.assertEqual(g.m, g.b)
    TestCopy.assertIs(g.b.__TestCopy__, g)
    g.b()

TestCopy = test_copy.TestCopy()
test_deepcopy_bound_method()
