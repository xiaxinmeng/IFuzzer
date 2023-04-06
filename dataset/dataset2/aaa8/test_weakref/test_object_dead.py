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

def test_object_dead():
    o = test_weakref.Object(1)
    r = weakref.WeakMethod(o.some_method)
    del o
    gc.collect()
    WeakMethodTestCase.assertIs(r(), None)

WeakMethodTestCase = test_weakref.WeakMethodTestCase()
test_object_dead()
