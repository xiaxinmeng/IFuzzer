import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_len():
    TestWeakSet.assertEqual(len(TestWeakSet.s), len(TestWeakSet.d))
    TestWeakSet.assertEqual(len(TestWeakSet.fs), 1)
    del TestWeakSet.obj
    TestWeakSet.assertEqual(len(TestWeakSet.fs), 0)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_len()
