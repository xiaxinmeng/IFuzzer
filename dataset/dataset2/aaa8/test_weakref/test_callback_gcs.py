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

def test_callback_gcs():

    class ObjectWithDel(test_weakref.Object):

        def __del__(ReferencesTestCase):
            pass
    x = ObjectWithDel(1)
    ref1 = weakref.ref(x, lambda ref: support.gc_collect())
    del x
    support.gc_collect()

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_callback_gcs()
