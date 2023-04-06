import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_update_set():
    TestWeakSet.s.update(set(TestWeakSet.items2))
    for c in TestWeakSet.items + TestWeakSet.items2:
        TestWeakSet.assertIn(c, TestWeakSet.s)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_update_set()
