import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_add():
    x = ustr('Q')
    TestWeakSet.s.add(x)
    TestWeakSet.assertIn(x, TestWeakSet.s)
    dup = TestWeakSet.s.copy()
    TestWeakSet.s.add(x)
    TestWeakSet.assertEqual(TestWeakSet.s, dup)
    TestWeakSet.assertRaises(TypeError, TestWeakSet.s.add, [])
    TestWeakSet.fs.add(test_weakset.Foo())
    TestWeakSet.assertTrue(len(TestWeakSet.fs) == 1)
    TestWeakSet.fs.add(TestWeakSet.obj)
    TestWeakSet.assertTrue(len(TestWeakSet.fs) == 1)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_add()
