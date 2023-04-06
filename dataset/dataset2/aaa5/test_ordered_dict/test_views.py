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

def test_views():
    OrderedDict = OrderedDictTests.OrderedDict
    s = 'the quick brown fox jumped over a lazy dog yesterday before dawn'.split()
    od = OrderedDict.fromkeys(s)
    OrderedDictTests.assertEqual(od.keys(), dict(od).keys())
    OrderedDictTests.assertEqual(od.items(), dict(od).items())

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_views()
