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

@support.cpython_only
def test_splittable_pop_pending():
    """pop a pending key in a splitted table should not crash"""
    (a, b) = DictTest.make_shared_key_dict(2)
    a['a'] = 4
    with DictTest.assertRaises(KeyError):
        b.pop('a')

DictTest = test_dict.DictTest()
test_splittable_pop_pending()
