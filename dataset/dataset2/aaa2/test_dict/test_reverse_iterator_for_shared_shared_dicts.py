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

def test_reverse_iterator_for_shared_shared_dicts():

    class A:

        def __init__(DictTest, x, y):
            if x:
                DictTest.x = x
            if y:
                DictTest.y = y
    DictTest.assertEqual(list(reversed(A(1, 2).__dict__)), ['y', 'x'])
    DictTest.assertEqual(list(reversed(A(1, 0).__dict__)), ['x'])
    DictTest.assertEqual(list(reversed(A(0, 1).__dict__)), ['y'])

DictTest = test_dict.DictTest()
test_reverse_iterator_for_shared_shared_dicts()
