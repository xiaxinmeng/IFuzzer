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

def test_callback_attribute_after_deletion():
    x = test_weakref.Object(1)
    ref = weakref.ref(x, ReferencesTestCase.callback)
    ReferencesTestCase.assertIsNotNone(ref.__callback__)
    del x
    support.gc_collect()
    ReferencesTestCase.assertIsNone(ref.__callback__)

ReferencesTestCase = test_weakref.ReferencesTestCase()
ReferencesTestCase.setUp()
test_callback_attribute_after_deletion()
