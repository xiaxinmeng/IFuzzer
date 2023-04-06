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

def test_reinsert():
    OrderedDict = OrderedDictTests.OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    del od['a']
    OrderedDictTests.assertEqual(list(od.items()), [('b', 2)])
    od['a'] = 1
    OrderedDictTests.assertEqual(list(od.items()), [('b', 2), ('a', 1)])

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_reinsert()
