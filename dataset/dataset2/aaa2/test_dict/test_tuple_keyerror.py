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

def test_tuple_keyerror():
    d = {}
    with DictTest.assertRaises(KeyError) as c:
        d[1,]
    DictTest.assertEqual(c.exception.args, ((1,),))

DictTest = test_dict.DictTest()
test_tuple_keyerror()
