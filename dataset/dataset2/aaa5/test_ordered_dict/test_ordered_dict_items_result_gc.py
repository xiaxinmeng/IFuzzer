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

@support.cpython_only
def test_ordered_dict_items_result_gc():
    it = iter(OrderedDictTests.OrderedDict({None: []}).items())
    gc.collect()
    OrderedDictTests.assertTrue(gc.is_tracked(next(it)))

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_ordered_dict_items_result_gc()
