import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_update():
    retval = TestWeakSet.s.update(TestWeakSet.items2)
    TestWeakSet.assertEqual(retval, None)
    for c in TestWeakSet.items + TestWeakSet.items2:
        TestWeakSet.assertIn(c, TestWeakSet.s)
    TestWeakSet.assertRaises(TypeError, TestWeakSet.s.update, [[]])

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_update()
