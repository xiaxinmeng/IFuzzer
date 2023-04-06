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

def test_callback_in_cycle_2():
    import gc

    class J(object):
        pass

    class II:

        def acallback(ReferencesTestCase, ignore):
            ReferencesTestCase.J
    I = II()
    I.J = J
    I.wr = weakref.ref(J, I.acallback)
    del I, J, II
    gc.collect()

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_callback_in_cycle_2()
