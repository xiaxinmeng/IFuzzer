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

def test_threaded_weak_valued_setdefault():
    d = weakref.WeakValueDictionary()
    with test_weakref.collect_in_thread():
        for i in range(100000):
            x = d.setdefault(10, test_weakref.RefCycle())
            MappingTestCase.assertIsNot(x, None)
            del x

MappingTestCase = test_weakref.MappingTestCase()
test_threaded_weak_valued_setdefault()
