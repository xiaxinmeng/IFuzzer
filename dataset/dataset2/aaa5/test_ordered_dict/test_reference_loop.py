import builtins
import contextlib
import copy
import gc
import pickle
from random import randrange, shuffle
import struct
import sys
import unittest
import weakref
from collections.abc import MutableMapping
from test import mapping_tests, support
from test.support import import_helper
import test_ordered_dict

def test_reference_loop():
    OrderedDict = OrderedDictTests.OrderedDict

    class A:
        od = OrderedDict()
    A.od[A] = None
    r = weakref.ref(A)
    del A
    gc.collect()
    OrderedDictTests.assertIsNone(r())

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_reference_loop()
