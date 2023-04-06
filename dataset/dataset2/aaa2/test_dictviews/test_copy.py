import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_copy():
    d = {1: 10, 'a': 'ABC'}
    DictSetTest.assertRaises(TypeError, copy.copy, d.keys())
    DictSetTest.assertRaises(TypeError, copy.copy, d.values())
    DictSetTest.assertRaises(TypeError, copy.copy, d.items())

DictSetTest = test_dictviews.DictSetTest()
test_copy()
