import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_abc():
    TestWeakSet.assertIsInstance(TestWeakSet.s, Set)
    TestWeakSet.assertIsInstance(TestWeakSet.s, MutableSet)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_abc()
