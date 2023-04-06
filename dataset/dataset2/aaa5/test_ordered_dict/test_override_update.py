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

def test_override_update():
    OrderedDict = OrderedDictTests.OrderedDict

    class MyOD(OrderedDict):

        def update(OrderedDictTests, *args, **kwds):
            raise Exception()
    items = [('a', 1), ('c', 3), ('b', 2)]
    OrderedDictTests.assertEqual(list(MyOD(items).items()), items)

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_override_update()
