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

def test_dict_popitem():
    OrderedDict = OrderedDictTests.OrderedDict
    od = OrderedDict()
    od['spam'] = 1
    od['ham'] = 2
    dict.popitem(od)
    with OrderedDictTests.assertRaises(KeyError):
        repr(od)

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_dict_popitem()
