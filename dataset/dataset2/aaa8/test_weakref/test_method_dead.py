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

def test_method_dead():
    C = WeakMethodTestCase._subclass()
    o = C(1)
    r = weakref.WeakMethod(o.some_method)
    del C.some_method
    gc.collect()
    WeakMethodTestCase.assertIs(r(), None)

WeakMethodTestCase = test_weakref.WeakMethodTestCase()
test_method_dead()
