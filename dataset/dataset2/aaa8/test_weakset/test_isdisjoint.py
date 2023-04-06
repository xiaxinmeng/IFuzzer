import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_isdisjoint():
    TestWeakSet.assertTrue(TestWeakSet.s.isdisjoint(WeakSet(TestWeakSet.items2)))
    TestWeakSet.assertTrue(not TestWeakSet.s.isdisjoint(WeakSet(TestWeakSet.letters)))

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_isdisjoint()
