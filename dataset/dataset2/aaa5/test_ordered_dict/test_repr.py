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

def test_repr():
    OrderedDict = OrderedDictTests.OrderedDict
    od = OrderedDict([('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)])
    OrderedDictTests.assertEqual(repr(od), "OrderedDict([('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)])")
    OrderedDictTests.assertEqual(eval(repr(od)), od)
    OrderedDictTests.assertEqual(repr(OrderedDict()), 'OrderedDict()')

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_repr()
