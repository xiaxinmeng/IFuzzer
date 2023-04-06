import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_constructor_identity():
    s = WeakSet(TestWeakSet.items)
    t = WeakSet(s)
    TestWeakSet.assertNotEqual(id(s), id(t))

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_constructor_identity()
