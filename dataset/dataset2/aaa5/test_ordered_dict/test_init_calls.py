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

def test_init_calls():
    calls = []

    class Spam:

        def keys(OrderedDictTests):
            calls.append('keys')
            return ()

        def items(OrderedDictTests):
            calls.append('items')
            return ()
    OrderedDictTests.OrderedDict(Spam())
    OrderedDictTests.assertEqual(calls, ['keys'])

OrderedDictTests = test_ordered_dict.OrderedDictTests()
test_init_calls()
