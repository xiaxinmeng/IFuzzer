import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_remove():
    x = ustr('a')
    TestWeakSet.s.remove(x)
    TestWeakSet.assertNotIn(x, TestWeakSet.s)
    TestWeakSet.assertRaises(KeyError, TestWeakSet.s.remove, x)
    TestWeakSet.assertRaises(TypeError, TestWeakSet.s.remove, [])

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_remove()
