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

def test_proxy_hash():
    cool_hash = 299792458

    class MyObj:

        def __hash__(ReferencesTestCase):
            return cool_hash
    obj = MyObj()
    ReferencesTestCase.assertEqual(hash(weakref.proxy(obj)), cool_hash)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_hash()
