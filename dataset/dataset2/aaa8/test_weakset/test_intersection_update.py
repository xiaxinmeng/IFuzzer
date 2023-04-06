import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_intersection_update():
    retval = TestWeakSet.s.intersection_update(TestWeakSet.items2)
    TestWeakSet.assertEqual(retval, None)
    for c in TestWeakSet.items + TestWeakSet.items2:
        if c in TestWeakSet.items2 and c in TestWeakSet.items:
            TestWeakSet.assertIn(c, TestWeakSet.s)
        else:
            TestWeakSet.assertNotIn(c, TestWeakSet.s)
    TestWeakSet.assertRaises(TypeError, TestWeakSet.s.intersection_update, [[]])

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_intersection_update()
