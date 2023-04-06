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

def test_object_set_item_single_instance_non_str_key():

    class Foo:
        pass
    f = Foo()
    f.__dict__[1] = 1
    f.a = 'a'
    DictTest.assertEqual(f.__dict__, {1: 1, 'a': 'a'})

DictTest = test_dict.DictTest()
test_object_set_item_single_instance_non_str_key()
