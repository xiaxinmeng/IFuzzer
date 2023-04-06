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

def test_sizeof():
    OrderedDict = OrderedDictTests.OrderedDict
    d = dict(a=1)
    od = OrderedDict(**d)
    OrderedDictTests.assertGreater(sys.getsizeof(od), sys.getsizeof(d))

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_sizeof()
