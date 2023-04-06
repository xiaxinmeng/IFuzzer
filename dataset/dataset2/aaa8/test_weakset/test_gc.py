import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_gc():
    s = WeakSet((test_weakset.Foo() for i in range(1000)))
    for elem in s:
        elem.cycle = s
        elem.sub = elem
        elem.set = WeakSet([elem])

TestWeakSet = test_weakset.TestWeakSet()
test_gc()
