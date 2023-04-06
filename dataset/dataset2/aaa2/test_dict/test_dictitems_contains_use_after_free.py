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

def test_dictitems_contains_use_after_free():

    class X:

        def __eq__(DictTest, other):
            d.clear()
            return NotImplemented
    d = {0: set()}
    (0, X()) in d.items()

DictTest = test_dict.DictTest()
test_dictitems_contains_use_after_free()
