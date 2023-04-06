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
def test_dict_items_result_gc():
    it = reversed({None: []}.items())
    gc.collect()
    DictTest.assertTrue(gc.is_tracked(next(it)))

DictTest = test_dict.DictTest()
test_dict_items_result_gc()
