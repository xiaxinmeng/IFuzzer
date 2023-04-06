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

def test_basic_ref():
    ReferencesTestCase.check_basic_ref(test_weakref.C)
    ReferencesTestCase.check_basic_ref(test_weakref.create_function)
    ReferencesTestCase.check_basic_ref(test_weakref.create_bound_method)
    o = test_weakref.C()
    wr = weakref.ref(o)
    repr(wr)
    del o
    repr(wr)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_basic_ref()
