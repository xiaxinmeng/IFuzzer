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
def test_splittable_setattr_after_pop():
    """setattr() must not convert combined table into split table."""
    import _testcapi

    class C:
        pass
    a = C()
    a.a = 1
    DictTest.assertTrue(_testcapi.dict_hassplittable(a.__dict__))
    a.__dict__.pop('a')
    DictTest.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
    a.a = 1
    DictTest.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
    a = C()
    a.a = 2
    DictTest.assertTrue(_testcapi.dict_hassplittable(a.__dict__))
    a.__dict__.popitem()
    DictTest.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
    a.a = 3
    DictTest.assertFalse(_testcapi.dict_hassplittable(a.__dict__))

DictTest = test_dict.DictTest()
test_splittable_setattr_after_pop()
