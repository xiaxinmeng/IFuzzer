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

def test_repr_recursive():
    OrderedDict = OrderedDictTests.OrderedDict
    od = OrderedDict.fromkeys('abc')
    od['x'] = od
    OrderedDictTests.assertEqual(repr(od), "OrderedDict([('a', None), ('b', None), ('c', None), ('x', ...)])")

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_repr_recursive()
