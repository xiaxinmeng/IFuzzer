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

def test_callback_in_cycle_3():
    import gc

    class C:

        def cb(ReferencesTestCase, ignore):
            ReferencesTestCase.me
            ReferencesTestCase.c1
            ReferencesTestCase.wr
    (c1, c2) = (C(), C())
    c2.me = c2
    c2.c1 = c1
    c2.wr = weakref.ref(c1, c2.cb)
    del c1, c2
    gc.collect()

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_callback_in_cycle_3()
