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

def test_highly_nested():
    OrderedDict = OrderedDictTests.OrderedDict
    obj = None
    for _ in range(1000):
        obj = OrderedDict([(None, obj)])
    del obj
    support.gc_collect()

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_highly_nested()
