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

def test_reversed():
    d = {'a': 1, 'b': 2, 'foo': 0, 'c': 3, 'd': 4}
    del d['foo']
    r = reversed(d)
    DictTest.assertEqual(list(r), list('dcba'))
    DictTest.assertRaises(StopIteration, next, r)

DictTest = test_dict.DictTest()
test_reversed()
