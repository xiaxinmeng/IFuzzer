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

def test_move_to_end_issue25406():
    OrderedDict = OrderedDictTests.OrderedDict
    od = OrderedDict.fromkeys('abc')
    od.move_to_end('c', last=False)
    OrderedDictTests.assertEqual(list(od), list('cab'))
    od.move_to_end('a', last=False)
    OrderedDictTests.assertEqual(list(od), list('acb'))
    od = OrderedDict.fromkeys('abc')
    od.move_to_end('a')
    OrderedDictTests.assertEqual(list(od), list('bca'))
    od.move_to_end('c')
    OrderedDictTests.assertEqual(list(od), list('bac'))

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_move_to_end_issue25406()
