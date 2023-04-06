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

def test_newstyle_number_ops():

    class F(float):
        pass
    f = F(2.0)
    p = weakref.proxy(f)
    ReferencesTestCase.assertEqual(p + 1.0, 3.0)
    ReferencesTestCase.assertEqual(1.0 + p, 3.0)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_newstyle_number_ops()
