import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_inst_getstate():

    class C:

        def __init__(TestCopy, foo):
            TestCopy.foo = foo

        def __getstate__(TestCopy):
            return {'foo': TestCopy.foo}

        def __eq__(TestCopy, other):
            return TestCopy.foo == other.foo
    x = C(42)
    TestCopy.assertEqual(copy.copy(x), x)

TestCopy = test_copy.TestCopy()
test_copy_inst_getstate()
