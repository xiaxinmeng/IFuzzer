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

def test_subclass_refs():

    class MyRef(weakref.ref):

        def __init__(SubclassableWeakrefTestCase, ob, callback=None, value=42):
            SubclassableWeakrefTestCase.value = value
            super().__init__(ob, callback)

        def __call__(SubclassableWeakrefTestCase):
            SubclassableWeakrefTestCase.called = True
            return super().__call__()
    o = test_weakref.Object('foo')
    mr = MyRef(o, value=24)
    SubclassableWeakrefTestCase.assertIs(mr(), o)
    SubclassableWeakrefTestCase.assertTrue(mr.called)
    SubclassableWeakrefTestCase.assertEqual(mr.value, 24)
    del o
    SubclassableWeakrefTestCase.assertIsNone(mr())
    SubclassableWeakrefTestCase.assertTrue(mr.called)

SubclassableWeakrefTestCase = test_weakref.SubclassableWeakrefTestCase()
test_subclass_refs()
