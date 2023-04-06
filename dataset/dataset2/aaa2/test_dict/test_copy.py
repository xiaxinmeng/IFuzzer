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

def test_copy():
    d = {1: 1, 2: 2, 3: 3}
    DictTest.assertIsNot(d.copy(), d)
    DictTest.assertEqual(d.copy(), d)
    DictTest.assertEqual(d.copy(), {1: 1, 2: 2, 3: 3})
    copy = d.copy()
    d[4] = 4
    DictTest.assertNotEqual(copy, d)
    DictTest.assertEqual({}.copy(), {})
    DictTest.assertRaises(TypeError, d.copy, None)

DictTest = test_dict.DictTest()
test_copy()
