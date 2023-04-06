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

def test_abc():
    OrderedDict = OrderedDictTests.OrderedDict
    OrderedDictTests.assertIsInstance(OrderedDict(), MutableMapping)
    OrderedDictTests.assertTrue(issubclass(OrderedDict, MutableMapping))

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_abc()
