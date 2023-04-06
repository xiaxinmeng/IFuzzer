import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_exceptions():
    TestCopy.assertIs(copy.Error, copy.error)
    TestCopy.assertTrue(issubclass(copy.Error, Exception))

TestCopy = test_copy.TestCopy()
test_exceptions()
