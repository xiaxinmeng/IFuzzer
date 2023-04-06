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

def test_reverse_iterator_for_empty_dict():
    DictTest.assertEqual(list(reversed({})), [])
    DictTest.assertEqual(list(reversed({}.items())), [])
    DictTest.assertEqual(list(reversed({}.values())), [])
    DictTest.assertEqual(list(reversed({}.keys())), [])
    DictTest.assertEqual(list(reversed(dict())), [])
    DictTest.assertEqual(list(reversed(dict().items())), [])
    DictTest.assertEqual(list(reversed(dict().values())), [])
    DictTest.assertEqual(list(reversed(dict().keys())), [])

DictTest = test_dict.DictTest()
test_reverse_iterator_for_empty_dict()
