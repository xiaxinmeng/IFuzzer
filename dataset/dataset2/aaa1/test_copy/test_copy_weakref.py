import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_weakref():
    TestCopy._check_weakref(copy.copy)

TestCopy = test_copy.TestCopy()
test_copy_weakref()
