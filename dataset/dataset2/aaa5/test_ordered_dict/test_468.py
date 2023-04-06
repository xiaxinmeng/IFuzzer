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

def test_468():
    OrderedDict = OrderedDictTests.OrderedDict
    items = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7)]
    shuffle(items)
    argdict = OrderedDict(items)
    d = OrderedDict(**argdict)
    OrderedDictTests.assertEqual(list(d.items()), items)

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_468()
