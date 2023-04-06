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

def test_reentrant_insertion():

    def mutate(d):
        d['b'] = 5
    DictTest.check_reentrant_insertion(mutate)

    def mutate(d):
        d.update(DictTest.__dict__)
        d.clear()
    DictTest.check_reentrant_insertion(mutate)

    def mutate(d):
        while d:
            d.popitem()
    DictTest.check_reentrant_insertion(mutate)

DictTest = test_dict.DictTest()
test_reentrant_insertion()
