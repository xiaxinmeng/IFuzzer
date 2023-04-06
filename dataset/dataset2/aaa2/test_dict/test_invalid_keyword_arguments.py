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

def test_invalid_keyword_arguments():

    class Custom(dict):
        pass
    for invalid in ({1: 2}, Custom({1: 2})):
        with DictTest.assertRaises(TypeError):
            dict(**invalid)
        with DictTest.assertRaises(TypeError):
            {}.update(**invalid)

DictTest = test_dict.DictTest()
test_invalid_keyword_arguments()
