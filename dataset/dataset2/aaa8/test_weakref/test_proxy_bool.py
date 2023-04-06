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

def test_proxy_bool():

    class List(list):
        pass
    lyst = List()
    ReferencesTestCase.assertEqual(bool(weakref.proxy(lyst)), bool(lyst))

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_bool()
