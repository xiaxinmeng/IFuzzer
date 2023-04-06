import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_weakvaluedict():
    TestCopy._check_copy_weakdict(weakref.WeakValueDictionary)

TestCopy = test_copy.TestCopy()
test_copy_weakvaluedict()
