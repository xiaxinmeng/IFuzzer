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

@support.cpython_only
def test_no_cycles():
    o = test_weakref.Object(1)

    def cb(_):
        pass
    r = weakref.WeakMethod(o.some_method, cb)
    wr = weakref.ref(r)
    del r
    WeakMethodTestCase.assertIs(wr(), None)

WeakMethodTestCase = test_weakref.WeakMethodTestCase()
test_no_cycles()
