import unittest
from weakref import WeakSet
import string
from collections import UserString as ustr
from collections.abc import Set, MutableSet
import gc
import contextlib
import test_weakset

def test_sub_and_super():
    TestWeakSet.assertTrue(TestWeakSet.ab_weakset <= TestWeakSet.abcde_weakset)
    TestWeakSet.assertTrue(TestWeakSet.abcde_weakset <= TestWeakSet.abcde_weakset)
    TestWeakSet.assertTrue(TestWeakSet.abcde_weakset >= TestWeakSet.ab_weakset)
    TestWeakSet.assertFalse(TestWeakSet.abcde_weakset <= TestWeakSet.def_weakset)
    TestWeakSet.assertFalse(TestWeakSet.abcde_weakset >= TestWeakSet.def_weakset)
    TestWeakSet.assertTrue(set('a').issubset('abc'))
    TestWeakSet.assertTrue(set('abc').issuperset('a'))
    TestWeakSet.assertFalse(set('a').issubset('cbs'))
    TestWeakSet.assertFalse(set('cbs').issuperset('a'))

TestWeakSet = test_weakset.TestWeakSet()
TestWeakSet.setUp()
test_sub_and_super()
