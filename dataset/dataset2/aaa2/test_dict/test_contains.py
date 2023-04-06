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

def test_contains():
    d = {}
    DictTest.assertNotIn('a', d)
    DictTest.assertFalse('a' in d)
    DictTest.assertTrue('a' not in d)
    d = {'a': 1, 'b': 2}
    DictTest.assertIn('a', d)
    DictTest.assertIn('b', d)
    DictTest.assertNotIn('c', d)
    DictTest.assertRaises(TypeError, d.__contains__)

DictTest = test_dict.DictTest()
test_contains()
