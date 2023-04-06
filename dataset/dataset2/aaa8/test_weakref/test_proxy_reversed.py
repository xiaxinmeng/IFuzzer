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

def test_proxy_reversed():

    class MyObj:

        def __len__(ReferencesTestCase):
            return 3

        def __reversed__(ReferencesTestCase):
            return iter('cba')
    obj = MyObj()
    ReferencesTestCase.assertEqual(''.join(reversed(weakref.proxy(obj))), 'cba')

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_reversed()
