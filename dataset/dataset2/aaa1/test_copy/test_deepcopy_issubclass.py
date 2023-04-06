import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_issubclass():

    class Meta(type):
        pass

    class C(metaclass=Meta):
        pass
    TestCopy.assertEqual(copy.deepcopy(C), C)

TestCopy = test_copy.TestCopy()
test_deepcopy_issubclass()
