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

def test_proxy_matmul():

    class C:

        def __matmul__(ReferencesTestCase, other):
            return 1729

        def __rmatmul__(ReferencesTestCase, other):
            return -163

        def __imatmul__(ReferencesTestCase, other):
            return 561
    o = C()
    p = weakref.proxy(o)
    ReferencesTestCase.assertEqual(p @ 5, 1729)
    ReferencesTestCase.assertEqual(5 @ p, -163)
    p @= 5
    ReferencesTestCase.assertEqual(p, 561)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_matmul()
