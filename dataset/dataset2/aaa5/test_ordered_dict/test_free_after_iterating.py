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

def test_free_after_iterating():
    support.check_free_after_iterating(OrderedDictTests, iter, OrderedDictTests.OrderedDict)
    support.check_free_after_iterating(OrderedDictTests, lambda d: iter(d.keys()), OrderedDictTests.OrderedDict)
    support.check_free_after_iterating(OrderedDictTests, lambda d: iter(d.values()), OrderedDictTests.OrderedDict)
    support.check_free_after_iterating(OrderedDictTests, lambda d: iter(d.items()), OrderedDictTests.OrderedDict)

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_free_after_iterating()
