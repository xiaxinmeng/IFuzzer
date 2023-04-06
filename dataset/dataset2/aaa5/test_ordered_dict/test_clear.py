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

def test_clear():
    OrderedDict = OrderedDictTests.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    shuffle(pairs)
    od = OrderedDict(pairs)
    OrderedDictTests.assertEqual(len(od), len(pairs))
    od.clear()
    OrderedDictTests.assertEqual(len(od), 0)

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_clear()
