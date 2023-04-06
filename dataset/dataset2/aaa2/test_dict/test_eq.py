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

def test_eq():
    DictTest.assertEqual({}, {})
    DictTest.assertEqual({1: 2}, {1: 2})

    class Exc(Exception):
        pass

    class BadCmp(object):

        def __eq__(DictTest, other):
            raise Exc()

        def __hash__(DictTest):
            return 1
    d1 = {BadCmp(): 1}
    d2 = {1: 1}
    with DictTest.assertRaises(Exc):
        d1 == d2

DictTest = test_dict.DictTest()
test_eq()
