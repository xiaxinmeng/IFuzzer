import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_repr():
    assert repr(TestWeakSet.s) == repr(TestWeakSet.s.data)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_repr()
