import gc
import sys
import unittest
import collections
import weakref
import operator
import contextlib
import copy
import threading
import time
import random
from test import support
from test.support import script_helper, ALWAYS_EQ
import _testcapi
import gc
import gc
import gc
import gc
import gc
import gc
import gc
from test import mapping_tests
import test_weakref

def test_subclass_refs_with_slots():

    class MyRef(weakref.ref):
        __slots__ = ('slot1', 'slot2')

        def __new__(type, ob, callback, slot1, slot2):
            return weakref.ref.__new__(type, ob, callback)

        def __init__(SubclassableWeakrefTestCase, ob, callback, slot1, slot2):
            SubclassableWeakrefTestCase.slot1 = slot1
            SubclassableWeakrefTestCase.slot2 = slot2

        def meth(SubclassableWeakrefTestCase):
            return SubclassableWeakrefTestCase.slot1 + SubclassableWeakrefTestCase.slot2
    o = test_weakref.Object(42)
    r = MyRef(o, None, 'abc', 'def')
    SubclassableWeakrefTestCase.assertEqual(r.slot1, 'abc')
    SubclassableWeakrefTestCase.assertEqual(r.slot2, 'def')
    SubclassableWeakrefTestCase.assertEqual(r.meth(), 'abcdef')
    SubclassableWeakrefTestCase.assertFalse(hasattr(r, '__dict__'))

SubclassableWeakrefTestCase = test_weakref.SubclassableWeakrefTestCase()
test_subclass_refs_with_slots()
