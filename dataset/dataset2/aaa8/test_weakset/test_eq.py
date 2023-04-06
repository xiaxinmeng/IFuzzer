import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_eq():
    TestWeakSet.assertTrue(TestWeakSet.s == TestWeakSet.s)
    TestWeakSet.assertTrue(TestWeakSet.s == WeakSet(TestWeakSet.items))
    TestWeakSet.assertFalse(TestWeakSet.s == set(TestWeakSet.items))
    TestWeakSet.assertFalse(TestWeakSet.s == list(TestWeakSet.items))
    TestWeakSet.assertFalse(TestWeakSet.s == tuple(TestWeakSet.items))
    TestWeakSet.assertFalse(TestWeakSet.s == WeakSet([test_weakset.Foo]))
    TestWeakSet.assertFalse(TestWeakSet.s == 1)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_eq()
