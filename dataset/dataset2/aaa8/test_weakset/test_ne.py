import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_ne():
    TestWeakSet.assertTrue(TestWeakSet.s != set(TestWeakSet.items))
    s1 = WeakSet()
    s2 = WeakSet()
    TestWeakSet.assertFalse(s1 != s2)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_ne()
