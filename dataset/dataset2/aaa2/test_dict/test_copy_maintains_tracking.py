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

def test_copy_maintains_tracking():

    class A:
        pass
    key = A()
    for d in ({}, {'a': 1}, {key: 'val'}):
        d2 = d.copy()
        DictTest.assertEqual(gc.is_tracked(d), gc.is_tracked(d2))

DictTest = test_dict.DictTest()
test_copy_maintains_tracking()
