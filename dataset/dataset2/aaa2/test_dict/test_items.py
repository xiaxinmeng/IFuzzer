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

def test_items():
    d = {}
    DictTest.assertEqual(set(d.items()), set())
    d = {1: 2}
    DictTest.assertEqual(set(d.items()), {(1, 2)})
    DictTest.assertRaises(TypeError, d.items, None)
    DictTest.assertEqual(repr(dict(a=1).items()), "dict_items([('a', 1)])")

DictTest = test_dict.DictTest()
test_items()
