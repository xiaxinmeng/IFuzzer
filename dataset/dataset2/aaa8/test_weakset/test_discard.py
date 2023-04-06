import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_discard():
    (a, q) = (ustr('a'), ustr('Q'))
    TestWeakSet.s.discard(a)
    TestWeakSet.assertNotIn(a, TestWeakSet.s)
    TestWeakSet.s.discard(q)
    TestWeakSet.assertRaises(TypeError, TestWeakSet.s.discard, [])

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_discard()
