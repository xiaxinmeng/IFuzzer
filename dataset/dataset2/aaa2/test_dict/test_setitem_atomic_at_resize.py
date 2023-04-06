import collections
import collections.abc
import gc
import pickle
import random
import string
import sys
import unittest
import weakref
from test import support
import _testcapi
from _testcapi import dict_getitem_knownhash
from test import mapping_tests
import test_dict

def test_setitem_atomic_at_resize():

    class Hashed(object):

        def __init__(DictTest):
            DictTest.hash_count = 0
            DictTest.eq_count = 0

        def __hash__(DictTest):
            DictTest.hash_count += 1
            return 42

        def __eq__(DictTest, other):
            DictTest.eq_count += 1
            return id(DictTest) == id(other)
    hashed1 = Hashed()
    y = {hashed1: 5, 0: 0, 1: 1, 2: 2, 3: 3}
    hashed2 = Hashed()
    y[hashed2] = []
    DictTest.assertEqual(hashed1.hash_count, 1)
    DictTest.assertEqual(hashed2.hash_count, 1)
    DictTest.assertEqual(hashed1.eq_count + hashed2.eq_count, 1)

DictTest = test_dict.DictTest()
test_setitem_atomic_at_resize()
