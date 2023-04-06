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

def test_reduce_not_too_fat():
    OrderedDict = OrderedDictTests.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    od = OrderedDict(pairs)
    OrderedDictTests.assertIsInstance(od.__dict__, dict)
    OrderedDictTests.assertIsNone(od.__reduce__()[2])
    od.x = 10
    OrderedDictTests.assertEqual(od.__dict__['x'], 10)
    OrderedDictTests.assertEqual(od.__reduce__()[2], {'x': 10})

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_reduce_not_too_fat()
