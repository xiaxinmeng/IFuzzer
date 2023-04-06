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

def test_proxy_iter():
    obj = None

    class MyObj:

        def __iter__(ReferencesTestCase):
            nonlocal obj
            del obj
            return NotImplemented
    obj = MyObj()
    p = weakref.proxy(obj)
    with ReferencesTestCase.assertRaises(TypeError):
        'blech' in p

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_iter()
