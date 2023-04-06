import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_lt():
    TestWeakSet.assertTrue(TestWeakSet.ab_weakset < TestWeakSet.abcde_weakset)
    TestWeakSet.assertFalse(TestWeakSet.abcde_weakset < TestWeakSet.def_weakset)
    TestWeakSet.assertFalse(TestWeakSet.ab_weakset < TestWeakSet.ab_weakset)
    TestWeakSet.assertFalse(WeakSet() < WeakSet())

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_lt()
