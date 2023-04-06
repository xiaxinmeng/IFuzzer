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

def test_values():
    d = {}
    DictTest.assertEqual(set(d.values()), set())
    d = {1: 2}
    DictTest.assertEqual(set(d.values()), {2})
    DictTest.assertRaises(TypeError, d.values, None)
    DictTest.assertEqual(repr(dict(a=1).values()), 'dict_values([1])')

DictTest = test_dict.DictTest()
test_values()
