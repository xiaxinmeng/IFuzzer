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

def test_issue24348():
    OrderedDict = OrderedDictTests.OrderedDict

    class Key:

        def __hash__(OrderedDictTests):
            return 1
    od = OrderedDict()
    od[Key()] = 0
    od.popitem()

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_issue24348()
