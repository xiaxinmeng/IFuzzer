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

def test_init_use_after_free():

    class X:

        def __hash__(DictTest):
            pair[:] = []
            return 13
    pair = [X(), 123]
    dict([pair])

DictTest = test_dict.DictTest()
test_init_use_after_free()
