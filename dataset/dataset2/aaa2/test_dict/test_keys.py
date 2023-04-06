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

def test_keys():
    d = {}
    DictTest.assertEqual(set(d.keys()), set())
    d = {'a': 1, 'b': 2}
    k = d.keys()
    DictTest.assertEqual(set(k), {'a', 'b'})
    DictTest.assertIn('a', k)
    DictTest.assertIn('b', k)
    DictTest.assertIn('a', d)
    DictTest.assertIn('b', d)
    DictTest.assertRaises(TypeError, d.keys, None)
    DictTest.assertEqual(repr(dict(a=1).keys()), "dict_keys(['a'])")

DictTest = test_dict.DictTest()
test_keys()
