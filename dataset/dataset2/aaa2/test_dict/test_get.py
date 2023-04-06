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

def test_get():
    d = {}
    DictTest.assertIs(d.get('c'), None)
    DictTest.assertEqual(d.get('c', 3), 3)
    d = {'a': 1, 'b': 2}
    DictTest.assertIs(d.get('c'), None)
    DictTest.assertEqual(d.get('c', 3), 3)
    DictTest.assertEqual(d.get('a'), 1)
    DictTest.assertEqual(d.get('a', 3), 1)
    DictTest.assertRaises(TypeError, d.get)
    DictTest.assertRaises(TypeError, d.get, None, None, None)

DictTest = test_dict.DictTest()
test_get()
