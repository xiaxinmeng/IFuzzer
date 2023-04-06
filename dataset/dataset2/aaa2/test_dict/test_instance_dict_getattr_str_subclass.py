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

def test_instance_dict_getattr_str_subclass():

    class Foo:

        def __init__(DictTest, msg):
            DictTest.msg = msg
    f = Foo('123')

    class _str(str):
        pass
    DictTest.assertEqual(f.msg, getattr(f, _str('msg')))
    DictTest.assertEqual(f.msg, f.__dict__[_str('msg')])

DictTest = test_dict.DictTest()
test_instance_dict_getattr_str_subclass()
