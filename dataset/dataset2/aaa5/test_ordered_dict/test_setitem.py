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

def test_setitem():
    OrderedDict = OrderedDictTests.OrderedDict
    od = OrderedDict([('d', 1), ('b', 2), ('c', 3), ('a', 4), ('e', 5)])
    od['c'] = 10
    od['f'] = 20
    OrderedDictTests.assertEqual(list(od.items()), [('d', 1), ('b', 2), ('c', 10), ('a', 4), ('e', 5), ('f', 20)])

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_setitem()
