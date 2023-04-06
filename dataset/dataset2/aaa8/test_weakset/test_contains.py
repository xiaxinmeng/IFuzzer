import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_contains():
    for c in TestWeakSet.letters:
        TestWeakSet.assertEqual(c in TestWeakSet.s, c in TestWeakSet.d)
    TestWeakSet.assertNotIn(1, TestWeakSet.s)
    TestWeakSet.assertIn(TestWeakSet.obj, TestWeakSet.fs)
    del TestWeakSet.obj
    TestWeakSet.assertNotIn(ustr('F'), TestWeakSet.fs)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_contains()
