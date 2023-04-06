import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_ixor():
    TestWeakSet.s ^= set(TestWeakSet.items2)
    for c in TestWeakSet.items + TestWeakSet.items2:
        if (c in TestWeakSet.items) ^ (c in TestWeakSet.items2):
            TestWeakSet.assertIn(c, TestWeakSet.s)
        else:
            TestWeakSet.assertNotIn(c, TestWeakSet.s)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_ixor()
