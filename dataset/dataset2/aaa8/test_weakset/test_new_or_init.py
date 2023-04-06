import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_new_or_init():
    TestWeakSet.assertRaises(TypeError, WeakSet, [], 2)

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_new_or_init()
