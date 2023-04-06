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

def test_empty_presized_dict_in_freelist():
    with DictTest.assertRaises(ZeroDivisionError):
        d = {'a': 1 // 0, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None}
    d = {}

DictTest = test_dict.DictTest()
test_empty_presized_dict_in_freelist()
