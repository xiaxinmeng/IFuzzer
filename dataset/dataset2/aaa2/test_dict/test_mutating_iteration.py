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

def test_mutating_iteration():
    d = {}
    d[1] = 1
    with DictTest.assertRaises(RuntimeError):
        for i in d:
            d[i + 1] = 1

DictTest = test_dict.DictTest()
test_mutating_iteration()
