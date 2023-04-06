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

def test_proxy_unicode():

    class C(object):

        def __str__(ReferencesTestCase):
            return 'string'

        def __bytes__(ReferencesTestCase):
            return b'bytes'
    instance = C()
    ReferencesTestCase.assertIn('__bytes__', dir(weakref.proxy(instance)))
    ReferencesTestCase.assertEqual(bytes(weakref.proxy(instance)), b'bytes')

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_proxy_unicode()
