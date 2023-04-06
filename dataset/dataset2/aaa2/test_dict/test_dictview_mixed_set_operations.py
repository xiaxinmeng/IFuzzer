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

def test_dictview_mixed_set_operations():
    DictTest.assertTrue({1: 1}.keys() == {1})
    DictTest.assertTrue({1} == {1: 1}.keys())
    DictTest.assertEqual({1: 1}.keys() | {2}, {1, 2})
    DictTest.assertEqual({2} | {1: 1}.keys(), {1, 2})
    DictTest.assertTrue({1: 1}.items() == {(1, 1)})
    DictTest.assertTrue({(1, 1)} == {1: 1}.items())
    DictTest.assertEqual({1: 1}.items() | {2}, {(1, 1), 2})
    DictTest.assertEqual({2} | {1: 1}.items(), {(1, 1), 2})

DictTest = test_dict.DictTest()
test_dictview_mixed_set_operations()
