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

def test_free_after_iterating():
    support.check_free_after_iterating(DictTest, iter, dict)
    support.check_free_after_iterating(DictTest, lambda d: iter(d.keys()), dict)
    support.check_free_after_iterating(DictTest, lambda d: iter(d.values()), dict)
    support.check_free_after_iterating(DictTest, lambda d: iter(d.items()), dict)

DictTest = test_dict.DictTest()
test_free_after_iterating()
