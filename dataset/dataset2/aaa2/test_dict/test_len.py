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

def test_len():
    d = {}
    DictTest.assertEqual(len(d), 0)
    d = {'a': 1, 'b': 2}
    DictTest.assertEqual(len(d), 2)

DictTest = test_dict.DictTest()
test_len()
