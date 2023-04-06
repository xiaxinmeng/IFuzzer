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
def test_weakref_list_is_not_traversed():
    gc.collect()
    x = CPythonOrderedDictTests.OrderedDict()
    x.cycle = x
    cycle = []
    cycle.append(cycle)
    x_ref = weakref.ref(x)
    cycle.append(x_ref)
    del x, cycle, x_ref
    gc.collect()

CPythonOrderedDictTests = test_ordered_dict.CPythonOrderedDictTests()
test_weakref_list_is_not_traversed()
