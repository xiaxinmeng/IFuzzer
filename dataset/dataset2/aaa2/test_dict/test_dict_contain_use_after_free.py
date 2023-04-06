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

def test_dict_contain_use_after_free():

    class S(str):

        def __eq__(DictTest, other):
            d.clear()
            return NotImplemented

        def __hash__(DictTest):
            return hash('test')
    d = {S(): 'value'}
    DictTest.assertFalse('test' in d)

DictTest = test_dict.DictTest()
test_dict_contain_use_after_free()
