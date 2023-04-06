import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_clear():
    TestWeakSet.s.clear()
    TestWeakSet.assertEqual(TestWeakSet.s, WeakSet([]))
    TestWeakSet.assertEqual(len(TestWeakSet.s), 0)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_clear()
