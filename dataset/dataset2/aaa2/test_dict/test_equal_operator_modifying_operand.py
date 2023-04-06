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

def test_equal_operator_modifying_operand():

    class X:

        def __del__(DictTest):
            dict_b.clear()

        def __eq__(DictTest, other):
            dict_a.clear()
            return True

        def __hash__(DictTest):
            return 13
    dict_a = {X(): 0}
    dict_b = {X(): X()}
    DictTest.assertTrue(dict_a == dict_b)

    class Y:

        def __eq__(DictTest, other):
            dict_d.clear()
            return True
    dict_c = {0: Y()}
    dict_d = {0: set()}
    DictTest.assertTrue(dict_c == dict_d)

DictTest = test_dict.DictTest()
test_equal_operator_modifying_operand()
