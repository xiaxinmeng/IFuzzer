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

def test_setdefault():
    OrderedDict = OrderedDictTests.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    shuffle(pairs)
    od = OrderedDict(pairs)
    pair_order = list(od.items())
    OrderedDictTests.assertEqual(od.setdefault('a', 10), 3)
    OrderedDictTests.assertEqual(list(od.items()), pair_order)
    OrderedDictTests.assertEqual(od.setdefault('x', 10), 10)
    OrderedDictTests.assertEqual(list(od.items())[-1], ('x', 10))
    OrderedDictTests.assertEqual(od.setdefault('g', default=9), 9)

    class Missing(OrderedDict):

        def __missing__(OrderedDictTests, key):
            return 0
    OrderedDictTests.assertEqual(Missing().setdefault(5, 9), 9)

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_setdefault()
