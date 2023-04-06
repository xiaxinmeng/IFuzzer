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

def test_fromkeys_operator_modifying_set_operand():

    class X(int):

        def __hash__(DictTest):
            return 13

        def __eq__(DictTest, other):
            if len(d) > 1:
                d.clear()
            return False
    d = {}
    d = {X(1), X(2)}
    try:
        dict.fromkeys(d)
    except RuntimeError:
        pass

DictTest = test_dict.DictTest()
test_fromkeys_operator_modifying_set_operand()
