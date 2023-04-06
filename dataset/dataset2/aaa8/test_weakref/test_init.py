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

def test_init():
    r = weakref.ref(Exception)
    ReferencesTestCase.assertRaises(TypeError, r.__init__, 0, 0, 0, 0, 0)
    gc.collect()

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_init()
