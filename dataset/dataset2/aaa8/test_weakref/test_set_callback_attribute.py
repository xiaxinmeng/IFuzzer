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

def test_set_callback_attribute():
    x = test_weakref.Object(1)
    callback = lambda ref: None
    ref1 = weakref.ref(x, callback)
    with ReferencesTestCase.assertRaises(AttributeError):
        ref1.__callback__ = lambda ref: None

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_set_callback_attribute()
