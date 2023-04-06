import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_init():
    s = WeakSet()
    s.__init__(TestWeakSet.items)
    TestWeakSet.assertEqual(s, TestWeakSet.s)
    s.__init__(TestWeakSet.items2)
    TestWeakSet.assertEqual(s, WeakSet(TestWeakSet.items2))
    TestWeakSet.assertRaises(TypeError, s.__init__, s, 2)
    TestWeakSet.assertRaises(TypeError, s.__init__, 1)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_init()
