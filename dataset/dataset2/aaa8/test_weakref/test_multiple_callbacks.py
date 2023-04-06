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

def test_multiple_callbacks():
    o = test_weakref.C()
    ref1 = weakref.ref(o, ReferencesTestCase.callback)
    ref2 = weakref.ref(o, ReferencesTestCase.callback)
    del o
    ReferencesTestCase.assertIsNone(ref1(), 'expected reference to be invalidated')
    ReferencesTestCase.assertIsNone(ref2(), 'expected reference to be invalidated')
    ReferencesTestCase.assertEqual(ReferencesTestCase.cbcalled, 2, 'callback not called the right number of times')

ReferencesTestCase = test_weakref.ReferencesTestCase()
ReferencesTestCase.setUp()
test_multiple_callbacks()
