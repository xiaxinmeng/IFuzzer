import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_dict_mixed_keys_items():
    d = {(1, 1): 11, (2, 2): 22}
    e = {1: 1, 2: 2}
    DictSetTest.assertEqual(d.keys(), e.items())
    DictSetTest.assertNotEqual(d.items(), e.keys())

DictSetTest = test_dictviews.DictSetTest()
test_dict_mixed_keys_items()
