import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_copy_weakkeydict():
    TestCopy._check_copy_weakdict(weakref.WeakKeyDictionary)

TestCopy = test_copy.TestCopy()
test_copy_weakkeydict()
