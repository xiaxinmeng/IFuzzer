import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_pop():
    for i in range(len(TestWeakSet.s)):
        elem = TestWeakSet.s.pop()
        TestWeakSet.assertNotIn(elem, TestWeakSet.s)
    TestWeakSet.assertRaises(KeyError, TestWeakSet.s.pop)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_pop()
