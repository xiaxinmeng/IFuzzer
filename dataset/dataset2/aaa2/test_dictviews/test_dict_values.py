import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_dict_values():
    d = {1: 10, 'a': 'ABC'}
    values = d.values()
    DictSetTest.assertEqual(set(values), {10, 'ABC'})
    DictSetTest.assertEqual(len(values), 2)

DictSetTest = test_dictviews.DictSetTest()
test_dict_values()
