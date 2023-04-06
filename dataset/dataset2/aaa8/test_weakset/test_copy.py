import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_copy():
    dup = TestWeakSet.s.copy()
    TestWeakSet.assertEqual(TestWeakSet.s, dup)
    TestWeakSet.assertNotEqual(id(TestWeakSet.s), id(dup))

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_copy()
