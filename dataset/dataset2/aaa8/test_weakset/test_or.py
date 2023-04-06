import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_or():
    i = TestWeakSet.s.union(TestWeakSet.items2)
    TestWeakSet.assertEqual(TestWeakSet.s | set(TestWeakSet.items2), i)
    TestWeakSet.assertEqual(TestWeakSet.s | frozenset(TestWeakSet.items2), i)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_or()
