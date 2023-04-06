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

def test_proxy_div():

    class C:

        def __floordiv__(ReferencesTestCase, other):
            return 42

        def __ifloordiv__(ReferencesTestCase, other):
            return 21
    o = C()
    p = weakref.proxy(o)
    ReferencesTestCase.assertEqual(p // 5, 42)
    p //= 5
    ReferencesTestCase.assertEqual(p, 21)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_div()
